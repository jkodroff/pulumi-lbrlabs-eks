// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

import * as pulumiAws from "@pulumi/aws";

export class AttachedNodeGroup extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'lbrlabs-eks:index:AttachedNodeGroup';

    /**
     * Returns true if the given object is an instance of AttachedNodeGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AttachedNodeGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AttachedNodeGroup.__pulumiType;
    }

    public /*out*/ readonly nodeGroup!: pulumi.Output<pulumiAws.eks.NodeGroup>;
    public /*out*/ readonly nodeRole!: pulumi.Output<pulumiAws.iam.Role>;

    /**
     * Create a AttachedNodeGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AttachedNodeGroupArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.clusterName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterName'");
            }
            if ((!args || args.subnetIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetIds'");
            }
            resourceInputs["capacityType"] = (args ? args.capacityType : undefined) ?? "ON_DEMAND";
            resourceInputs["clusterName"] = args ? args.clusterName : undefined;
            resourceInputs["diskSize"] = (args ? args.diskSize : undefined) ?? 20;
            resourceInputs["instanceTypes"] = args ? args.instanceTypes : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["scalingConfig"] = args ? args.scalingConfig : undefined;
            resourceInputs["subnetIds"] = args ? args.subnetIds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["taints"] = args ? args.taints : undefined;
            resourceInputs["nodeGroup"] = undefined /*out*/;
            resourceInputs["nodeRole"] = undefined /*out*/;
        } else {
            resourceInputs["nodeGroup"] = undefined /*out*/;
            resourceInputs["nodeRole"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AttachedNodeGroup.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a AttachedNodeGroup resource.
 */
export interface AttachedNodeGroupArgs {
    /**
     * The capacity type of the nodegroup.
     */
    capacityType?: pulumi.Input<string>;
    /**
     * The cluster name to attach the nodegroup tp.
     */
    clusterName: pulumi.Input<string>;
    /**
     * The size of the disk to attach to the nodes.
     */
    diskSize?: pulumi.Input<number>;
    instanceTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    scalingConfig?: pulumi.Input<pulumiAws.types.input.eks.NodeGroupScalingConfig>;
    subnetIds: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Key-value map of tags to apply to the nodegroup.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    taints?: pulumi.Input<pulumi.Input<pulumiAws.types.input.eks.NodeGroupTaint>[]>;
}
