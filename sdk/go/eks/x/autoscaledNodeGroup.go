// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package eks

import (
	"context"
	"reflect"

	"errors"
	"github.com/lbrlabs/pulumi-lbrlabs-eks/sdk/go/eks/internal"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type AutoscaledNodeGroup struct {
	pulumi.ResourceState
}

// NewAutoscaledNodeGroup registers a new resource with the given unique name, arguments, and options.
func NewAutoscaledNodeGroup(ctx *pulumi.Context,
	name string, args *AutoscaledNodeGroupArgs, opts ...pulumi.ResourceOption) (*AutoscaledNodeGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.NodeRole == nil {
		return nil, errors.New("invalid value for required argument 'NodeRole'")
	}
	if args.Requirements == nil {
		return nil, errors.New("invalid value for required argument 'Requirements'")
	}
	if args.SecurityGroupIds == nil {
		return nil, errors.New("invalid value for required argument 'SecurityGroupIds'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	if args.DiskSize == nil {
		args.DiskSize = pulumix.Val("20Gi")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AutoscaledNodeGroup
	err := ctx.RegisterRemoteComponentResource("lbrlabs-eks:index:AutoscaledNodeGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type autoscaledNodeGroupArgs struct {
	// AMI family for the node group.
	AmiFamily *string `pulumi:"amiFamily"`
	// Annotations to apply to the node group.
	Annotations map[string]string `pulumi:"annotations"`
	// Disk size for the node group.
	DiskSize string `pulumi:"diskSize"`
	// Node role for the node group.
	NodeRole string `pulumi:"nodeRole"`
	// List of requirements for the node group.
	Requirements []Requirement `pulumi:"requirements"`
	// List of security group selector terms for the node group.
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	// List of subnet selector terms for the node group.
	SubnetIds []string `pulumi:"subnetIds"`
	// Optional node taints.
	Taints []corev1.Taint `pulumi:"taints"`
}

// The set of arguments for constructing a AutoscaledNodeGroup resource.
type AutoscaledNodeGroupArgs struct {
	// AMI family for the node group.
	AmiFamily pulumix.Input[*string]
	// Annotations to apply to the node group.
	Annotations pulumix.Input[map[string]string]
	// Disk size for the node group.
	DiskSize pulumix.Input[string]
	// Node role for the node group.
	NodeRole pulumix.Input[string]
	// List of requirements for the node group.
	Requirements pulumix.Input[[]*RequirementArgs]
	// List of security group selector terms for the node group.
	SecurityGroupIds pulumix.Input[[]string]
	// List of subnet selector terms for the node group.
	SubnetIds pulumix.Input[[]string]
	// Optional node taints.
	Taints pulumix.Input[[]*corev1.TaintArgs]
}

func (AutoscaledNodeGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*autoscaledNodeGroupArgs)(nil)).Elem()
}

type AutoscaledNodeGroupOutput struct{ *pulumi.OutputState }

func (AutoscaledNodeGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AutoscaledNodeGroup)(nil)).Elem()
}

func (o AutoscaledNodeGroupOutput) ToAutoscaledNodeGroupOutput() AutoscaledNodeGroupOutput {
	return o
}

func (o AutoscaledNodeGroupOutput) ToAutoscaledNodeGroupOutputWithContext(ctx context.Context) AutoscaledNodeGroupOutput {
	return o
}

func (o AutoscaledNodeGroupOutput) ToOutput(ctx context.Context) pulumix.Output[AutoscaledNodeGroup] {
	return pulumix.Output[AutoscaledNodeGroup]{
		OutputState: o.OutputState,
	}
}

func init() {
	pulumi.RegisterOutputType(AutoscaledNodeGroupOutput{})
}
