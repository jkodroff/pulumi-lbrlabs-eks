// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

import * as pulumiAws from "@pulumi/aws";

export class AttachedFargateProfile extends pulumi.ComponentResource {
    /** @internal */
    public static readonly __pulumiType = 'lbrlabs-eks:index:AttachedFargateProfile';

    /**
     * Returns true if the given object is an instance of AttachedFargateProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AttachedFargateProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AttachedFargateProfile.__pulumiType;
    }

    public /*out*/ readonly profile!: pulumi.Output<pulumiAws.eks.FargateProfile>;
    public /*out*/ readonly role!: pulumi.Output<pulumiAws.iam.Role>;

    /**
     * Create a AttachedFargateProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AttachedFargateProfileArgs, opts?: pulumi.ComponentResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.clusterName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterName'");
            }
            if ((!args || args.selectors === undefined) && !opts.urn) {
                throw new Error("Missing required property 'selectors'");
            }
            if ((!args || args.subnetIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetIds'");
            }
            resourceInputs["clusterName"] = args ? args.clusterName : undefined;
            resourceInputs["selectors"] = args ? args.selectors : undefined;
            resourceInputs["subnetIds"] = args ? args.subnetIds : undefined;
            resourceInputs["profile"] = undefined /*out*/;
            resourceInputs["role"] = undefined /*out*/;
        } else {
            resourceInputs["profile"] = undefined /*out*/;
            resourceInputs["role"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AttachedFargateProfile.__pulumiType, name, resourceInputs, opts, true /*remote*/);
    }
}

/**
 * The set of arguments for constructing a AttachedFargateProfile resource.
 */
export interface AttachedFargateProfileArgs {
    /**
     * The name of the cluster to assign the fargate profile to.
     */
    clusterName: pulumi.Input<string>;
    /**
     * The selectors for the fargate profile.
     */
    selectors: pulumi.Input<pulumiAws.types.input.eks.FargateProfileSelector>;
    /**
     * The subnet IDs to use for the fargate profile.
     */
    subnetIds: pulumi.Input<pulumi.Input<string>[]>;
}
