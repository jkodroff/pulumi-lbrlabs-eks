// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Eks
{
    [EksResourceType("lbrlabs-eks:index:AttachedNodeGroup")]
    public partial class AttachedNodeGroup : global::Pulumi.ComponentResource
    {
        [Output("nodeGroup")]
        public Output<Pulumi.Aws.Eks.NodeGroup> NodeGroup { get; private set; } = null!;

        [Output("nodeRole")]
        public Output<Pulumi.Aws.Iam.Role> NodeRole { get; private set; } = null!;


        /// <summary>
        /// Create a AttachedNodeGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AttachedNodeGroup(string name, AttachedNodeGroupArgs args, ComponentResourceOptions? options = null)
            : base("lbrlabs-eks:index:AttachedNodeGroup", name, args ?? new AttachedNodeGroupArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/lbrlabs",
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class AttachedNodeGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The AMI Type for the nodegroup.
        /// </summary>
        [Input("amiType")]
        public Input<string>? AmiType { get; set; }

        /// <summary>
        /// The capacity type of the nodegroup.
        /// </summary>
        [Input("capacityType")]
        public Input<string>? CapacityType { get; set; }

        /// <summary>
        /// The cluster name to attach the nodegroup tp.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        /// <summary>
        /// The size of the disk to attach to the nodes.
        /// </summary>
        [Input("diskSize")]
        public Input<double>? DiskSize { get; set; }

        [Input("instanceTypes")]
        private InputList<string>? _instanceTypes;
        public InputList<string> InstanceTypes
        {
            get => _instanceTypes ?? (_instanceTypes = new InputList<string>());
            set => _instanceTypes = value;
        }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The release version for the nodegroup.
        /// </summary>
        [Input("releaseVersion")]
        public Input<string>? ReleaseVersion { get; set; }

        [Input("scalingConfig")]
        public Input<Pulumi.Aws.Eks.Inputs.NodeGroupScalingConfigArgs>? ScalingConfig { get; set; }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Key-value map of tags to apply to the nodegroup.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        [Input("taints")]
        private InputList<Pulumi.Aws.Eks.Inputs.NodeGroupTaintArgs>? _taints;
        public InputList<Pulumi.Aws.Eks.Inputs.NodeGroupTaintArgs> Taints
        {
            get => _taints ?? (_taints = new InputList<Pulumi.Aws.Eks.Inputs.NodeGroupTaintArgs>());
            set => _taints = value;
        }

        public AttachedNodeGroupArgs()
        {
            CapacityType = "ON_DEMAND";
            DiskSize = 20;
        }
        public static new AttachedNodeGroupArgs Empty => new AttachedNodeGroupArgs();
    }
}
