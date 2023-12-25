// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package eks

import (
	"context"
	"reflect"

	"errors"
	"github.com/lbrlabs/pulumi-lbrlabs-eks/sdk/go/eks/internal"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/eks"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type Cluster struct {
	pulumi.ResourceState

	// The cluster name
	ClusterName pulumi.StringOutput `pulumi:"clusterName"`
	// The Cluster control plane
	ControlPlane eks.ClusterOutput `pulumi:"controlPlane"`
	// The kubeconfig for this cluster.
	Kubeconfig pulumi.StringOutput `pulumi:"kubeconfig"`
	// The OIDC provider for this cluster.
	OidcProvider iam.OpenIdConnectProviderOutput `pulumi:"oidcProvider"`
	// The system node group.
	SystemNodes eks.NodeGroupOutput `pulumi:"systemNodes"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterSubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'ClusterSubnetIds'")
	}
	if args.SystemNodeSubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SystemNodeSubnetIds'")
	}
	if args.EnableCertManager == nil {
		enableCertManager_ := true
		args.EnableCertManager = &enableCertManager_
	}
	if args.EnableCloudWatchAgent == nil {
		enableCloudWatchAgent_ := false
		args.EnableCloudWatchAgent = &enableCloudWatchAgent_
	}
	if args.EnableExternalDns == nil {
		enableExternalDns_ := true
		args.EnableExternalDns = &enableExternalDns_
	}
	if args.EnableOtel == nil {
		enableOtel_ := false
		args.EnableOtel = &enableOtel_
	}
	if args.HttpsTargetPort == nil {
		args.HttpsTargetPort = pulumi.StringPtr("https")
	}
	if args.LbType == nil {
		args.LbType = pulumi.StringPtr("nlb")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Cluster
	err := ctx.RegisterRemoteComponentResource("lbrlabs-eks:index:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type clusterArgs struct {
	// The ARN of the certificate to use for the ingress controller.
	CertificateArn   *string  `pulumi:"certificateArn"`
	ClusterSubnetIds []string `pulumi:"clusterSubnetIds"`
	// Whether to enable cert-manager with route 53 integration.
	EnableCertManager *bool `pulumi:"enableCertManager"`
	// Whether to enable cloudwatch container insights for EKS.
	EnableCloudWatchAgent *bool `pulumi:"enableCloudWatchAgent"`
	// Whether to enable external dns with route 53 integration.
	EnableExternalDns *bool `pulumi:"enableExternalDns"`
	// Whether to enable the OTEL Distro for EKS.
	EnableOtel *bool `pulumi:"enableOtel"`
	// The ARN of the certificate to use for the ingress controller.
	HttpsTargetPort *string `pulumi:"httpsTargetPort"`
	// The type of loadbalancer to provision.
	LbType *string `pulumi:"lbType"`
	// The email address to use to issue certificates from Lets Encrypt.
	LetsEncryptEmail *string `pulumi:"letsEncryptEmail"`
	// The initial number of nodes in the system autoscaling group.
	SystemNodeDesiredCount  *float64 `pulumi:"systemNodeDesiredCount"`
	SystemNodeInstanceTypes []string `pulumi:"systemNodeInstanceTypes"`
	// The maximum number of nodes in the system autoscaling group.
	SystemNodeMaxCount *float64 `pulumi:"systemNodeMaxCount"`
	// The minimum number of nodes in the system autoscaling group.
	SystemNodeMinCount  *float64 `pulumi:"systemNodeMinCount"`
	SystemNodeSubnetIds []string `pulumi:"systemNodeSubnetIds"`
	// Key-value map of tags to apply to the cluster.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	// The ARN of the certificate to use for the ingress controller.
	CertificateArn   pulumi.StringPtrInput
	ClusterSubnetIds pulumi.StringArrayInput
	// Whether to enable cert-manager with route 53 integration.
	EnableCertManager *bool
	// Whether to enable cloudwatch container insights for EKS.
	EnableCloudWatchAgent *bool
	// Whether to enable external dns with route 53 integration.
	EnableExternalDns *bool
	// Whether to enable the OTEL Distro for EKS.
	EnableOtel *bool
	// The ARN of the certificate to use for the ingress controller.
	HttpsTargetPort pulumi.StringPtrInput
	// The type of loadbalancer to provision.
	LbType pulumi.StringPtrInput
	// The email address to use to issue certificates from Lets Encrypt.
	LetsEncryptEmail pulumi.StringPtrInput
	// The initial number of nodes in the system autoscaling group.
	SystemNodeDesiredCount  pulumi.Float64PtrInput
	SystemNodeInstanceTypes pulumi.StringArrayInput
	// The maximum number of nodes in the system autoscaling group.
	SystemNodeMaxCount pulumi.Float64PtrInput
	// The minimum number of nodes in the system autoscaling group.
	SystemNodeMinCount  pulumi.Float64PtrInput
	SystemNodeSubnetIds pulumi.StringArrayInput
	// Key-value map of tags to apply to the cluster.
	Tags pulumi.StringMapInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

type ClusterInput interface {
	pulumi.Input

	ToClusterOutput() ClusterOutput
	ToClusterOutputWithContext(ctx context.Context) ClusterOutput
}

func (*Cluster) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (i *Cluster) ToClusterOutput() ClusterOutput {
	return i.ToClusterOutputWithContext(context.Background())
}

func (i *Cluster) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterOutput)
}

func (i *Cluster) ToOutput(ctx context.Context) pulumix.Output[*Cluster] {
	return pulumix.Output[*Cluster]{
		OutputState: i.ToClusterOutputWithContext(ctx).OutputState,
	}
}

// ClusterArrayInput is an input type that accepts ClusterArray and ClusterArrayOutput values.
// You can construct a concrete instance of `ClusterArrayInput` via:
//
//	ClusterArray{ ClusterArgs{...} }
type ClusterArrayInput interface {
	pulumi.Input

	ToClusterArrayOutput() ClusterArrayOutput
	ToClusterArrayOutputWithContext(context.Context) ClusterArrayOutput
}

type ClusterArray []ClusterInput

func (ClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Cluster)(nil)).Elem()
}

func (i ClusterArray) ToClusterArrayOutput() ClusterArrayOutput {
	return i.ToClusterArrayOutputWithContext(context.Background())
}

func (i ClusterArray) ToClusterArrayOutputWithContext(ctx context.Context) ClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterArrayOutput)
}

func (i ClusterArray) ToOutput(ctx context.Context) pulumix.Output[[]*Cluster] {
	return pulumix.Output[[]*Cluster]{
		OutputState: i.ToClusterArrayOutputWithContext(ctx).OutputState,
	}
}

// ClusterMapInput is an input type that accepts ClusterMap and ClusterMapOutput values.
// You can construct a concrete instance of `ClusterMapInput` via:
//
//	ClusterMap{ "key": ClusterArgs{...} }
type ClusterMapInput interface {
	pulumi.Input

	ToClusterMapOutput() ClusterMapOutput
	ToClusterMapOutputWithContext(context.Context) ClusterMapOutput
}

type ClusterMap map[string]ClusterInput

func (ClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Cluster)(nil)).Elem()
}

func (i ClusterMap) ToClusterMapOutput() ClusterMapOutput {
	return i.ToClusterMapOutputWithContext(context.Background())
}

func (i ClusterMap) ToClusterMapOutputWithContext(ctx context.Context) ClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterMapOutput)
}

func (i ClusterMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Cluster] {
	return pulumix.Output[map[string]*Cluster]{
		OutputState: i.ToClusterMapOutputWithContext(ctx).OutputState,
	}
}

type ClusterOutput struct{ *pulumi.OutputState }

func (ClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (o ClusterOutput) ToClusterOutput() ClusterOutput {
	return o
}

func (o ClusterOutput) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return o
}

func (o ClusterOutput) ToOutput(ctx context.Context) pulumix.Output[*Cluster] {
	return pulumix.Output[*Cluster]{
		OutputState: o.OutputState,
	}
}

// The cluster name
func (o ClusterOutput) ClusterName() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.ClusterName }).(pulumi.StringOutput)
}

// The Cluster control plane
func (o ClusterOutput) ControlPlane() eks.ClusterOutput {
	return o.ApplyT(func(v *Cluster) eks.ClusterOutput { return v.ControlPlane }).(eks.ClusterOutput)
}

// The kubeconfig for this cluster.
func (o ClusterOutput) Kubeconfig() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.Kubeconfig }).(pulumi.StringOutput)
}

// The OIDC provider for this cluster.
func (o ClusterOutput) OidcProvider() iam.OpenIdConnectProviderOutput {
	return o.ApplyT(func(v *Cluster) iam.OpenIdConnectProviderOutput { return v.OidcProvider }).(iam.OpenIdConnectProviderOutput)
}

// The system node group.
func (o ClusterOutput) SystemNodes() eks.NodeGroupOutput {
	return o.ApplyT(func(v *Cluster) eks.NodeGroupOutput { return v.SystemNodes }).(eks.NodeGroupOutput)
}

type ClusterArrayOutput struct{ *pulumi.OutputState }

func (ClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Cluster)(nil)).Elem()
}

func (o ClusterArrayOutput) ToClusterArrayOutput() ClusterArrayOutput {
	return o
}

func (o ClusterArrayOutput) ToClusterArrayOutputWithContext(ctx context.Context) ClusterArrayOutput {
	return o
}

func (o ClusterArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Cluster] {
	return pulumix.Output[[]*Cluster]{
		OutputState: o.OutputState,
	}
}

func (o ClusterArrayOutput) Index(i pulumi.IntInput) ClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Cluster {
		return vs[0].([]*Cluster)[vs[1].(int)]
	}).(ClusterOutput)
}

type ClusterMapOutput struct{ *pulumi.OutputState }

func (ClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Cluster)(nil)).Elem()
}

func (o ClusterMapOutput) ToClusterMapOutput() ClusterMapOutput {
	return o
}

func (o ClusterMapOutput) ToClusterMapOutputWithContext(ctx context.Context) ClusterMapOutput {
	return o
}

func (o ClusterMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Cluster] {
	return pulumix.Output[map[string]*Cluster]{
		OutputState: o.OutputState,
	}
}

func (o ClusterMapOutput) MapIndex(k pulumi.StringInput) ClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Cluster {
		return vs[0].(map[string]*Cluster)[vs[1].(string)]
	}).(ClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterInput)(nil)).Elem(), &Cluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterArrayInput)(nil)).Elem(), ClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterMapInput)(nil)).Elem(), ClusterMap{})
	pulumi.RegisterOutputType(ClusterOutput{})
	pulumi.RegisterOutputType(ClusterArrayOutput{})
	pulumi.RegisterOutputType(ClusterMapOutput{})
}
