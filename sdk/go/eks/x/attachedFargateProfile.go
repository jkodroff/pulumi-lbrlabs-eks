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

type AttachedFargateProfile struct {
	pulumi.ResourceState

	Profile pulumix.GPtrOutput[eks.FargateProfile, eks.FargateProfileOutput] `pulumi:"profile"`
	Role    pulumix.GPtrOutput[iam.Role, iam.RoleOutput]                     `pulumi:"role"`
}

// NewAttachedFargateProfile registers a new resource with the given unique name, arguments, and options.
func NewAttachedFargateProfile(ctx *pulumi.Context,
	name string, args *AttachedFargateProfileArgs, opts ...pulumi.ResourceOption) (*AttachedFargateProfile, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterName == nil {
		return nil, errors.New("invalid value for required argument 'ClusterName'")
	}
	if args.Selectors == nil {
		return nil, errors.New("invalid value for required argument 'Selectors'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AttachedFargateProfile
	err := ctx.RegisterRemoteComponentResource("lbrlabs-eks:index:AttachedFargateProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type attachedFargateProfileArgs struct {
	// The name of the cluster to assign the fargate profile to.
	ClusterName string                       `pulumi:"clusterName"`
	Selectors   []eks.FargateProfileSelector `pulumi:"selectors"`
	// The subnet IDs to use for the fargate profile.
	SubnetIds []string `pulumi:"subnetIds"`
}

// The set of arguments for constructing a AttachedFargateProfile resource.
type AttachedFargateProfileArgs struct {
	// The name of the cluster to assign the fargate profile to.
	ClusterName pulumix.Input[string]
	Selectors   pulumix.Input[[]*eks.FargateProfileSelectorArgs]
	// The subnet IDs to use for the fargate profile.
	SubnetIds pulumix.Input[[]string]
}

func (AttachedFargateProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*attachedFargateProfileArgs)(nil)).Elem()
}

type AttachedFargateProfileOutput struct{ *pulumi.OutputState }

func (AttachedFargateProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AttachedFargateProfile)(nil)).Elem()
}

func (o AttachedFargateProfileOutput) ToAttachedFargateProfileOutput() AttachedFargateProfileOutput {
	return o
}

func (o AttachedFargateProfileOutput) ToAttachedFargateProfileOutputWithContext(ctx context.Context) AttachedFargateProfileOutput {
	return o
}

func (o AttachedFargateProfileOutput) ToOutput(ctx context.Context) pulumix.Output[AttachedFargateProfile] {
	return pulumix.Output[AttachedFargateProfile]{
		OutputState: o.OutputState,
	}
}

func (o AttachedFargateProfileOutput) Profile() pulumix.GPtrOutput[eks.FargateProfile, eks.FargateProfileOutput] {
	value := pulumix.Apply[AttachedFargateProfile](o, func(v AttachedFargateProfile) pulumix.GPtrOutput[eks.FargateProfile, eks.FargateProfileOutput] {
		return v.Profile
	})
	unwrapped := pulumix.Flatten[*eks.FargateProfile, pulumix.GPtrOutput[eks.FargateProfile, eks.FargateProfileOutput]](value)
	return pulumix.GPtrOutput[eks.FargateProfile, eks.FargateProfileOutput]{OutputState: unwrapped.OutputState}
}

func (o AttachedFargateProfileOutput) Role() pulumix.GPtrOutput[iam.Role, iam.RoleOutput] {
	value := pulumix.Apply[AttachedFargateProfile](o, func(v AttachedFargateProfile) pulumix.GPtrOutput[iam.Role, iam.RoleOutput] { return v.Role })
	unwrapped := pulumix.Flatten[*iam.Role, pulumix.GPtrOutput[iam.Role, iam.RoleOutput]](value)
	return pulumix.GPtrOutput[iam.Role, iam.RoleOutput]{OutputState: unwrapped.OutputState}
}

func init() {
	pulumi.RegisterOutputType(AttachedFargateProfileOutput{})
}