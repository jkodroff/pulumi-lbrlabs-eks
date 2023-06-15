package provider

import (
	"encoding/json"
	"fmt"

	"github.com/lbrlabs/pulumi-lbrlabs-eks/pkg/provider/irsa"
	"github.com/lbrlabs/pulumi-lbrlabs-eks/pkg/provider/kubeconfig"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/eks"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v5/go/aws/kms"
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	//corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	helm "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
	storagev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/storage/v1"

	tls "github.com/pulumi/pulumi-tls/sdk/v4/go/tls"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The set of arguments for creating a Cluster component resource.
type ClusterArgs struct {
	VpcId                   pulumi.StringInput       `pulumi:"vpcId"`
	ClusterSubnetIds        pulumi.StringArrayInput  `pulumi:"clusterSubnetIds"`
	SystemNodeSubnetIds     pulumi.StringArrayInput  `pulumi:"systemNodeSubnetIds"`
	SystemNodeInstanceTypes *pulumi.StringArrayInput `pulumi:"systemNodeInstanceTypes"`
	SystemNodeMaxCount      *pulumi.IntInput         `pulumi:"systemNodeMaxCount"`
	SystemNodeMinCount      *pulumi.IntInput         `pulumi:"systemNodeMinCount"`
	SystemNodeDesiredCount  *pulumi.IntInput         `pulumi:"systemNodeDesiredCount"`
	ClusterVersion          pulumi.StringPtrInput    `pulumi:"clusterVersion"`
}

// The Cluster component resource.
type Cluster struct {
	pulumi.ResourceState

	ControlPlane *eks.Cluster               `pulumi:"controlPlane"`
	SystemNodes  *eks.NodeGroup             `pulumi:"systemNodes"`
	OidcProvider *iam.OpenIdConnectProvider `pulumi:"oidcProvider"`
	KubeConfig   pulumi.StringOutput        `pulumi:"kubeconfig"`
}

// NewCluster creates a new EKS Cluster component resource.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		args = &ClusterArgs{}
	}

	component := &Cluster{}
	err := ctx.RegisterComponentResource("lbrlabs-eks:index:Cluster", name, component, opts...)
	if err != nil {
		return nil, err
	}

	// FIXME: make this strongly typed instead of using interfaces
	clusterRoleJSON, err := json.Marshal(map[string]interface{}{
		"Version": "2012-10-17",
		"Statement": []interface{}{
			map[string]interface{}{
				"Action": "sts:AssumeRole",
				"Principal": map[string]interface{}{
					"Service": []interface{}{
						"eks.amazonaws.com",
					},
				},
				"Effect": "Allow",
			},
		},
	})
	if err != nil {
		return nil, fmt.Errorf("error marshalling cluster role json: %w", err)
	}

	role, err := iam.NewRole(ctx, fmt.Sprintf("%s-cluster-role", name), &iam.RoleArgs{
		AssumeRolePolicy: pulumi.String(clusterRoleJSON),
	}, pulumi.Parent(component))
	if err != nil {
		return nil, fmt.Errorf("error creating cluster role: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-cluster-policy", name), &iam.RolePolicyAttachmentArgs{
		Role:      role.Name,
		PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"),
	}, pulumi.Parent(role))
	if err != nil {
		return nil, fmt.Errorf("error attaching cluster policy: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-cluster-policy-vpc", name), &iam.RolePolicyAttachmentArgs{
		Role:      role.Name,
		PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"),
	}, pulumi.Parent(role))
	if err != nil {
		return nil, fmt.Errorf("error attaching cluster policy for VPC: %w", err)
	}

	// clusterSecurityGroup, err := ec2.NewSecurityGroup(ctx, fmt.Sprintf("%s-cluster-sg", name), &ec2.SecurityGroupArgs{
	// 	VpcId: args.VpcId,
	// 	RevokeRulesOnDelete: pulumi.Bool(true),
	// }, pulumi.Parent(component))
	// if err != nil {
	// 	return nil, fmt.Errorf("error creating cluster security group: %w", err)
	// }

	// FIXME: ensure we have a key policy for this key that's sane
	kmsKey, err := kms.NewKey(ctx, fmt.Sprintf("%s-cluster-kms-key", name), &kms.KeyArgs{
		EnableKeyRotation: pulumi.Bool(true),
		Description:       pulumi.String("KMS key for EKS cluster secrets"),
	}, pulumi.Parent(component))
	if err != nil {
		return nil, fmt.Errorf("error creating cluster kms key: %w", err)
	}

	keyPolicyDocument := iam.GetPolicyDocumentOutput(ctx, iam.GetPolicyDocumentOutputArgs{
		Statements: iam.GetPolicyDocumentStatementArray{
			iam.GetPolicyDocumentStatementArgs{
				Sid: pulumi.String("AllowAccessToKmsKey"),
				Actions: pulumi.StringArray{
					pulumi.String("kms:Encrypt"),
					pulumi.String("kms:Decrypt"),
					pulumi.String("kms:ListGrants"),
					pulumi.String("kms:DescribeKey"),
				},
				Effect: pulumi.String("Allow"),
				Resources: pulumi.StringArray{
					kmsKey.Arn,
				},
			},
		},
	})

	clusterKmsPolicy, err := iam.NewPolicy(ctx, fmt.Sprintf("%s-cluster-kms-policy", name), &iam.PolicyArgs{
		Description: pulumi.String("KMS key policy for EKS cluster secrets"),
		Policy:      keyPolicyDocument.Json(),
	}, pulumi.Parent(role))
	if err != nil {
		return nil, fmt.Errorf("error creating KMS key policy: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-cluster-policy-kms", name), &iam.RolePolicyAttachmentArgs{
		Role:      role.Name,
		PolicyArn: clusterKmsPolicy.Arn,
	}, pulumi.Parent(role))
	if err != nil {
		return nil, fmt.Errorf("error attaching cluster policy for KMS: %w", err)
	}

	controlPlane, err := eks.NewCluster(ctx, name, &eks.ClusterArgs{
		RoleArn: role.Arn,
		Version: args.ClusterVersion,
		VpcConfig: &eks.ClusterVpcConfigArgs{
			SubnetIds: args.ClusterSubnetIds,
		},
		EncryptionConfig: &eks.ClusterEncryptionConfigArgs{
			Resources: pulumi.StringArray{
				pulumi.String("secrets"),
			},
			Provider: &eks.ClusterEncryptionConfigProviderArgs{
				KeyArn: kmsKey.Arn,
			},
		},
		EnabledClusterLogTypes: pulumi.StringArray{
			pulumi.String("api"),
			pulumi.String("audit"),
			pulumi.String("authenticator"),
			pulumi.String("controllerManager"),
			pulumi.String("scheduler"),
		},
	}, pulumi.Parent(component))
	if err != nil {
		return nil, fmt.Errorf("error creating cluster control plane: %w", err)
	}

	cert := tls.GetCertificateOutput(ctx, tls.GetCertificateOutputArgs{
		Url: controlPlane.Identities.Index(pulumi.Int(0)).Oidcs().Index(pulumi.Int(0)).Issuer().Elem(),
	}, pulumi.Parent(component))

	oidcProvider, err := iam.NewOpenIdConnectProvider(ctx, fmt.Sprintf("%s-oidc-provider", name), &iam.OpenIdConnectProviderArgs{
		ClientIdLists: pulumi.StringArray{
			pulumi.String("sts.amazonaws.com"),
		},
		Url: controlPlane.Identities.Index(pulumi.Int(0)).Oidcs().Index(pulumi.Int(0)).Issuer().Elem(),
		ThumbprintLists: pulumi.StringArray{
			cert.Certificates().Index(pulumi.Int(0)).Sha1Fingerprint(),
		},
	}, pulumi.Parent(controlPlane))
	if err != nil {
		return nil, fmt.Errorf("error creating OIDC provider: %w", err)
	}

	systemNodePolicyJSON, err := json.Marshal(map[string]interface{}{
		"Statement": []map[string]interface{}{
			{
				"Action": "sts:AssumeRole",
				"Effect": "Allow",
				"Principal": map[string]interface{}{
					"Service": "ec2.amazonaws.com",
				},
			},
		},
		"Version": "2012-10-17",
	})
	if err != nil {
		return nil, fmt.Errorf("error marshalling system node policy: %w", err)
	}

	systemNodeRole, err := iam.NewRole(ctx, fmt.Sprintf("%s-system-node-role", name), &iam.RoleArgs{
		AssumeRolePolicy: pulumi.String(systemNodePolicyJSON),
	}, pulumi.Parent(controlPlane))
	if err != nil {
		return nil, fmt.Errorf("error creating system node role: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-system-node-worker-policy", name), &iam.RolePolicyAttachmentArgs{
		PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"),
		Role:      systemNodeRole.Name,
	}, pulumi.Parent(systemNodeRole))
	if err != nil {
		return nil, fmt.Errorf("error attaching system node worker policy: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-system-node-ecr-policy", name), &iam.RolePolicyAttachmentArgs{
		PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"),
		Role:      systemNodeRole.Name,
	}, pulumi.Parent(systemNodeRole))
	if err != nil {
		return nil, fmt.Errorf("error attaching system node ecr policy: %w", err)
	}

	var instanceTypes pulumi.StringArrayInput

	if args.SystemNodeInstanceTypes == nil {
		instanceTypes = pulumi.StringArray{
			pulumi.String("t3.medium"),
		}
	} else {
		instanceTypes = *args.SystemNodeInstanceTypes
	}

	var systemNodeMaxCount pulumi.IntInput
	if args.SystemNodeMaxCount == nil {
		systemNodeMaxCount = pulumi.Int(10)
	} else {
		systemNodeMaxCount = *args.SystemNodeMaxCount
	}

	var systemNodeMinCount pulumi.IntInput
	if args.SystemNodeMinCount == nil {
		systemNodeMinCount = pulumi.Int(1)
	} else {
		systemNodeMinCount = *args.SystemNodeMinCount
	}

	var systemNodeDesiredCount pulumi.IntInput
	if args.SystemNodeDesiredCount == nil {
		systemNodeDesiredCount = pulumi.Int(1)
	} else {
		systemNodeDesiredCount = *args.SystemNodeDesiredCount
	}

	systemNodes, err := eks.NewNodeGroup(ctx, fmt.Sprintf("%s-system-nodes", name), &eks.NodeGroupArgs{
		ClusterName:   controlPlane.Name,
		SubnetIds:     args.SystemNodeSubnetIds,
		NodeRoleArn:   systemNodeRole.Arn,
		InstanceTypes: instanceTypes,
		Labels: pulumi.StringMap{
			"node.lbrlabs.com/system": pulumi.String("system"),
		},
		Taints: eks.NodeGroupTaintArray{
			eks.NodeGroupTaintArgs{
				Effect: pulumi.String("NO_SCHEDULE"),
				Key:    pulumi.String("node.lbrlabs.com/system"),
				Value:  pulumi.String("true"),
			},
		},
		ScalingConfig: &eks.NodeGroupScalingConfigArgs{
			MaxSize:     systemNodeMaxCount,
			MinSize:     systemNodeMinCount,
			DesiredSize: systemNodeDesiredCount,
		},
	}, pulumi.Parent(component), pulumi.IgnoreChanges([]string{"scalingConfig"}))
	if err != nil {
		return nil, fmt.Errorf("error creating system nodegroup provider: %w", err)
	}

	coreDnsConfig, err := json.Marshal(map[string]interface{}{
		"tolerations": []map[string]interface{}{
			{
				"key":      "node.lbrlabs.com/system",
				"operator": "Equal",
				"value":    "true",
				"effect":   "NoSchedule",
			},
		},
	})
	if err != nil {
		return nil, fmt.Errorf("error marshalling coredns config: %w", err)
	}

	_, err = eks.NewAddon(ctx, fmt.Sprintf("%s-coredns", name), &eks.AddonArgs{
		AddonName:           pulumi.String("coredns"),
		ClusterName:         controlPlane.Name,
		ResolveConflicts:    pulumi.String("OVERWRITE"),
		ConfigurationValues: pulumi.String(coreDnsConfig),
	}, pulumi.Parent(controlPlane), pulumi.DependsOn([]pulumi.Resource{systemNodes}))
	if err != nil {
		return nil, fmt.Errorf("error installing coredns: %w", err)
	}

	vpcCsiRole, err := irsa.NewIamServiceAccountRole(ctx, fmt.Sprintf("%s-vpc-csi-role", name), &irsa.IamServiceAccountRoleArgs{
		OidcProviderArn:    oidcProvider.Arn,
		OidcProviderUrl:    oidcProvider.Url,
		Namespace:          pulumi.String("kube-system"),
		ServiceAccountName: pulumi.String("aws-node"),
	}, pulumi.Parent(controlPlane))
	if err != nil {
		return nil, fmt.Errorf("error creating iam service account role for VPC CSI: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-vpc-csi-policy", name), &iam.RolePolicyAttachmentArgs{
		Role:      vpcCsiRole.Role.Name,
		PolicyArn: pulumi.String("arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"),
	}, pulumi.Parent(vpcCsiRole))
	if err != nil {
		return nil, fmt.Errorf("error attaching cni policy to role: %w", err)
	}

	_, err = eks.NewAddon(ctx, fmt.Sprintf("%s-vpc-cni", name), &eks.AddonArgs{
		AddonName:             pulumi.String("vpc-cni"),
		ClusterName:           controlPlane.Name,
		ResolveConflicts:      pulumi.String("OVERWRITE"),
		ServiceAccountRoleArn: vpcCsiRole.Role.Arn,
	}, pulumi.Parent(vpcCsiRole), pulumi.DependsOn([]pulumi.Resource{systemNodes}))
	if err != nil {
		return nil, fmt.Errorf("error installing vpc cni: %w", err)
	}

	ebsCsiRole, err := irsa.NewIamServiceAccountRole(ctx, fmt.Sprintf("%s-ebs-csi-role", name), &irsa.IamServiceAccountRoleArgs{
		OidcProviderArn:    oidcProvider.Arn,
		OidcProviderUrl:    oidcProvider.Url,
		Namespace:          pulumi.String("kube-system"),
		ServiceAccountName: pulumi.String("ebs-csi-controller-sa"),
	}, pulumi.Parent(controlPlane))
	if err != nil {
		return nil, fmt.Errorf("error creating iam service account role for EBS CSI: %w", err)
	}

	_, err = iam.NewRolePolicyAttachment(ctx, fmt.Sprintf("%s-ebs-csi-policy", name), &iam.RolePolicyAttachmentArgs{
		Role:      ebsCsiRole.Role.Name,
		PolicyArn: pulumi.String("arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"),
	}, pulumi.Parent(ebsCsiRole))
	if err != nil {
		return nil, fmt.Errorf("error attaching EBS policy to role: %w", err)
	}

	ebsCsiConfig, err := json.Marshal(map[string]interface{}{
		"controller": map[string]interface{}{
			"tolerations": []map[string]interface{}{
				{
					"key":      "node.lbrlabs.com/system",
					"operator": "Equal",
					"value":    "true",
					"effect":   "NoSchedule",
				},
			},
		},
	})
	if err != nil {
		return nil, fmt.Errorf("error marshalling EBS CSI config: %w", err)
	}

	_, err = eks.NewAddon(ctx, fmt.Sprintf("%s-ebs-csi", name), &eks.AddonArgs{
		AddonName:             pulumi.String("aws-ebs-csi-driver"),
		ClusterName:           controlPlane.Name,
		ResolveConflicts:      pulumi.String("OVERWRITE"),
		ServiceAccountRoleArn: ebsCsiRole.Role.Arn,
		ConfigurationValues:   pulumi.String(ebsCsiConfig),
	}, pulumi.Parent(ebsCsiRole), pulumi.DependsOn([]pulumi.Resource{systemNodes}))
	if err != nil {
		return nil, fmt.Errorf("error installing EBS csi: %w", err)
	}

	kc, err := kubeconfig.Generate(name, controlPlane.Endpoint, controlPlane.CertificateAuthorities.Index(pulumi.Int(0)).Data().Elem(), controlPlane.Name)
	if err != nil {
		return nil, fmt.Errorf("error generating kubeconfig: %w", err)
	}

	provider, err := kubernetes.NewProvider(ctx, fmt.Sprintf("%s-k8s-provider", name), &kubernetes.ProviderArgs{
		Kubeconfig: kc,
	}, pulumi.Parent(controlPlane))
	if err != nil {
		return nil, fmt.Errorf("error creating kubernetes provider: %w", err)
	}

	serverSideProvider, err := kubernetes.NewProvider(ctx, fmt.Sprintf("%s-k8s-ssa-provider", name), &kubernetes.ProviderArgs{
		Kubeconfig:            kc,
		EnableServerSideApply: pulumi.Bool(true),
	}, pulumi.Parent(controlPlane))
	if err != nil {
		return nil, fmt.Errorf("error creating server side apply kubernetes provider: %w", err)
	}

	// FIXME: this is a workaround for EKS creating a broken default storage class
	// FIXME: what we likely want to do here in future is delete this
	_, err = storagev1.NewStorageClass(ctx, fmt.Sprintf("%s-gp2-storage-class", name), &storagev1.StorageClassArgs{
		Metadata: &metav1.ObjectMetaArgs{
			Name: pulumi.String("gp2"),
			Annotations: pulumi.StringMap{
				"pulumi.com/patchForce":                       pulumi.String("true"),
				"storageclass.kubernetes.io/is-default-class": pulumi.String("false"),
			},
		},
		VolumeBindingMode: pulumi.String("WaitForFirstConsumer"),
		Provisioner:       pulumi.String("kubernetes.io/aws-ebs"),
		ReclaimPolicy:     pulumi.String("Delete"),
	}, pulumi.Parent(serverSideProvider), pulumi.Provider(serverSideProvider))
	if err != nil {
		return nil, fmt.Errorf("error creating gp2 storage class: %w", err)
	}

	_, err = storagev1.NewStorageClass(ctx, fmt.Sprintf("%s-gp3-storage-class", name), &storagev1.StorageClassArgs{
		Metadata: &metav1.ObjectMetaArgs{
			Name: pulumi.String("gp3"),
			Annotations: pulumi.StringMap{
				"storageclass.kubernetes.io/is-default-class": pulumi.String("true"),
			},
		},
		Provisioner:       pulumi.String("ebs.csi.aws.com"),
		VolumeBindingMode: pulumi.String("WaitForFirstConsumer"),
		ReclaimPolicy:     pulumi.String("Delete"),
		Parameters: pulumi.StringMap{
			"csi.storage.k8s.io/fstype": pulumi.String("ext4"),
			"type":                      pulumi.String("gp3"),
		},
	}, pulumi.Parent(provider), pulumi.Provider(provider), pulumi.DeleteBeforeReplace(true))
	if err != nil {
		return nil, fmt.Errorf("error creating gp3 storage class: %w", err)
	}

	nginxIngressExternal, err := helm.NewRelease(ctx, fmt.Sprintf("%s-nginx-ext", name), &helm.ReleaseArgs{
		Chart:     pulumi.String("ingress-nginx"),
		Namespace: pulumi.String("kube-system"),
		RepositoryOpts: &helm.RepositoryOptsArgs{
			Repo: pulumi.String("https://kubernetes.github.io/ingress-nginx"),
		},
		Values: pulumi.Map{
			"controller": pulumi.Map{
				"admissionWebhooks": pulumi.Map{
					"patch": pulumi.Map{
						"tolerations": pulumi.MapArray{
							pulumi.Map{
								"key":      pulumi.String("node.lbrlabs.com/system"),
								"operator": pulumi.String("Equal"),
								"value":    pulumi.String("true"),
								"effect":   pulumi.String("NoSchedule"),
							},
						},
					},
				},
				"tolerations": pulumi.MapArray{
					pulumi.Map{
						"key":      pulumi.String("node.lbrlabs.com/system"),
						"operator": pulumi.String("Equal"),
						"value":    pulumi.String("true"),
						"effect":   pulumi.String("NoSchedule"),
					},
				},
				"ingressClassResource": pulumi.Map{
					"name":    pulumi.String("external"),
					"default":         pulumi.Bool(true),
					"controllerValue": pulumi.String("k8s.io/ingress-nginx/external"),
				},
				"ingressClass": pulumi.String("external"),
				"service": pulumi.Map{
					"annotations": pulumi.Map{
						"service.beta.kubernetes.io/aws-load-balancer-ssl-ports": pulumi.String("https"),
						"service.beta.kubernetes.io/aws-load-balancer-backend-protocol": pulumi.String("tcp"),
					},
				},
			},
			"defaultBackend": pulumi.Map{
				"tolerations": pulumi.MapArray{
					pulumi.Map{
						"key":      pulumi.String("node.lbrlabs.com/system"),
						"operator": pulumi.String("Equal"),
						"value":    pulumi.String("true"),
						"effect":   pulumi.String("NoSchedule"),
					},
				},
			},
		},
	}, pulumi.Parent(controlPlane), pulumi.Provider(provider), pulumi.DependsOn([]pulumi.Resource{systemNodes}))
	if err != nil {
		return nil, fmt.Errorf("error installing nginx ingress helm release: %w", err)
	}

	nginxIngressInternal, err := helm.NewRelease(ctx, fmt.Sprintf("%s-nginx-int", name), &helm.ReleaseArgs{
		Chart:     pulumi.String("ingress-nginx"),
		Namespace: pulumi.String("kube-system"),
		RepositoryOpts: &helm.RepositoryOptsArgs{
			Repo: pulumi.String("https://kubernetes.github.io/ingress-nginx"),
		},
		Values: pulumi.Map{
			"controller": pulumi.Map{
				"admissionWebhooks": pulumi.Map{
					"patch": pulumi.Map{
						"tolerations": pulumi.MapArray{
							pulumi.Map{
								"key":      pulumi.String("node.lbrlabs.com/system"),
								"operator": pulumi.String("Equal"),
								"value":    pulumi.String("true"),
								"effect":   pulumi.String("NoSchedule"),
							},
						},
					},
				},
				"tolerations": pulumi.MapArray{
					pulumi.Map{
						"key":      pulumi.String("node.lbrlabs.com/system"),
						"operator": pulumi.String("Equal"),
						"value":    pulumi.String("true"),
						"effect":   pulumi.String("NoSchedule"),
					},
				},
				"ingressClassResource": pulumi.Map{
					"name":    pulumi.String("internal"),
					"default":         pulumi.Bool(true),
					"controllerValue": pulumi.String("k8s.io/ingress-nginx/internal"),
				},
				"ingressClass": pulumi.String("internal"),
				"service": pulumi.Map{
					"annotations": pulumi.Map{
						"service.beta.kubernetes.io/aws-load-balancer-ssl-ports": pulumi.String("https"),
						"service.beta.kubernetes.io/aws-load-balancer-internal": pulumi.Bool(true),
						"service.beta.kubernetes.io/aws-load-balancer-backend-protocol": pulumi.String("tcp"),
					},
				},
			},
			"defaultBackend": pulumi.Map{
				"tolerations": pulumi.MapArray{
					pulumi.Map{
						"key":      pulumi.String("node.lbrlabs.com/system"),
						"operator": pulumi.String("Equal"),
						"value":    pulumi.String("true"),
						"effect":   pulumi.String("NoSchedule"),
					},
				},
			},
		},
	}, pulumi.Parent(controlPlane), pulumi.Provider(provider), pulumi.DependsOn([]pulumi.Resource{systemNodes}))
	if err != nil {
		return nil, fmt.Errorf("error installing nginx ingress helm release: %w", err)
	}

	_ = nginxIngressExternal
	_ = nginxIngressInternal

	component.ControlPlane = controlPlane
	component.OidcProvider = oidcProvider
	component.SystemNodes = systemNodes
	component.KubeConfig = kc

	if err := ctx.RegisterResourceOutputs(component, pulumi.Map{
		"controlPlane": controlPlane,
		"oidcProvider": oidcProvider,
		"systemNodes":  systemNodes,
		"kubeconfig":   kc,
	}); err != nil {
		return nil, err
	}

	return component, nil
}