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

type AttachedNodeGroup struct {
	pulumi.ResourceState

	NodeGroup pulumix.GPtrOutput[eks.NodeGroup, eks.NodeGroupOutput] `pulumi:"nodeGroup"`
	NodeRole  pulumix.GPtrOutput[iam.Role, iam.RoleOutput]           `pulumi:"nodeRole"`
}

// NewAttachedNodeGroup registers a new resource with the given unique name, arguments, and options.
func NewAttachedNodeGroup(ctx *pulumi.Context,
	name string, args *AttachedNodeGroupArgs, opts ...pulumi.ResourceOption) (*AttachedNodeGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterName == nil {
		return nil, errors.New("invalid value for required argument 'ClusterName'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AttachedNodeGroup
	err := ctx.RegisterRemoteComponentResource("lbrlabs-eks:index:AttachedNodeGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type attachedNodeGroupArgs struct {
	// The cluster name to attach the nodegroup tp.
	ClusterName string `pulumi:"clusterName"`
	// Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
	Labels            map[string]string           `pulumi:"labels"`
	NodeInstanceTypes []string                    `pulumi:"nodeInstanceTypes"`
	ScalingConfig     *eks.NodeGroupScalingConfig `pulumi:"scalingConfig"`
	SubnetIds         []string                    `pulumi:"subnetIds"`
	// Key-value map of tags to apply to the nodegroup.
	Tags   map[string]string    `pulumi:"tags"`
	Taints []eks.NodeGroupTaint `pulumi:"taints"`
}

// The set of arguments for constructing a AttachedNodeGroup resource.
type AttachedNodeGroupArgs struct {
	// The cluster name to attach the nodegroup tp.
	ClusterName pulumix.Input[string]
	// Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
	Labels            pulumix.Input[map[string]string]
	NodeInstanceTypes pulumix.Input[[]string]
	ScalingConfig     pulumix.Input[*eks.NodeGroupScalingConfigArgs]
	SubnetIds         pulumix.Input[[]string]
	// Key-value map of tags to apply to the nodegroup.
	Tags   pulumix.Input[map[string]string]
	Taints pulumix.Input[[]*eks.NodeGroupTaintArgs]
}

func (AttachedNodeGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*attachedNodeGroupArgs)(nil)).Elem()
}

type AttachedNodeGroupOutput struct{ *pulumi.OutputState }

func (AttachedNodeGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AttachedNodeGroup)(nil)).Elem()
}

func (o AttachedNodeGroupOutput) ToAttachedNodeGroupOutput() AttachedNodeGroupOutput {
	return o
}

func (o AttachedNodeGroupOutput) ToAttachedNodeGroupOutputWithContext(ctx context.Context) AttachedNodeGroupOutput {
	return o
}

func (o AttachedNodeGroupOutput) ToOutput(ctx context.Context) pulumix.Output[AttachedNodeGroup] {
	return pulumix.Output[AttachedNodeGroup]{
		OutputState: o.OutputState,
	}
}

func (o AttachedNodeGroupOutput) NodeGroup() pulumix.GPtrOutput[eks.NodeGroup, eks.NodeGroupOutput] {
	value := pulumix.Apply[AttachedNodeGroup](o, func(v AttachedNodeGroup) pulumix.GPtrOutput[eks.NodeGroup, eks.NodeGroupOutput] { return v.NodeGroup })
	unwrapped := pulumix.Flatten[*eks.NodeGroup, pulumix.GPtrOutput[eks.NodeGroup, eks.NodeGroupOutput]](value)
	return pulumix.GPtrOutput[eks.NodeGroup, eks.NodeGroupOutput]{OutputState: unwrapped.OutputState}
}

func (o AttachedNodeGroupOutput) NodeRole() pulumix.GPtrOutput[iam.Role, iam.RoleOutput] {
	value := pulumix.Apply[AttachedNodeGroup](o, func(v AttachedNodeGroup) pulumix.GPtrOutput[iam.Role, iam.RoleOutput] { return v.NodeRole })
	unwrapped := pulumix.Flatten[*iam.Role, pulumix.GPtrOutput[iam.Role, iam.RoleOutput]](value)
	return pulumix.GPtrOutput[iam.Role, iam.RoleOutput]{OutputState: unwrapped.OutputState}
}

func init() {
	pulumi.RegisterOutputType(AttachedNodeGroupOutput{})
}
