# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
import pulumi_aws

__all__ = ['AttachedNodeGroupArgs', 'AttachedNodeGroup']

@pulumi.input_type
class AttachedNodeGroupArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 capacity_type: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[float]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 scaling_config: Optional[pulumi.Input['pulumi_aws.eks.NodeGroupScalingConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.eks.NodeGroupTaintArgs']]]] = None):
        """
        The set of arguments for constructing a AttachedNodeGroup resource.
        :param pulumi.Input[str] cluster_name: The cluster name to attach the nodegroup tp.
        :param pulumi.Input[str] capacity_type: The capacity type of the nodegroup.
        :param pulumi.Input[float] disk_size: The size of the disk to attach to the nodes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to apply to the nodegroup.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if capacity_type is None:
            capacity_type = 'ON_DEMAND'
        if capacity_type is not None:
            pulumi.set(__self__, "capacity_type", capacity_type)
        if disk_size is None:
            disk_size = 20
        if disk_size is not None:
            pulumi.set(__self__, "disk_size", disk_size)
        if instance_types is not None:
            pulumi.set(__self__, "instance_types", instance_types)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if scaling_config is not None:
            pulumi.set(__self__, "scaling_config", scaling_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The cluster name to attach the nodegroup tp.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="capacityType")
    def capacity_type(self) -> Optional[pulumi.Input[str]]:
        """
        The capacity type of the nodegroup.
        """
        return pulumi.get(self, "capacity_type")

    @capacity_type.setter
    def capacity_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity_type", value)

    @property
    @pulumi.getter(name="diskSize")
    def disk_size(self) -> Optional[pulumi.Input[float]]:
        """
        The size of the disk to attach to the nodes.
        """
        return pulumi.get(self, "disk_size")

    @disk_size.setter
    def disk_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "disk_size", value)

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "instance_types")

    @instance_types.setter
    def instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "instance_types", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="scalingConfig")
    def scaling_config(self) -> Optional[pulumi.Input['pulumi_aws.eks.NodeGroupScalingConfigArgs']]:
        return pulumi.get(self, "scaling_config")

    @scaling_config.setter
    def scaling_config(self, value: Optional[pulumi.Input['pulumi_aws.eks.NodeGroupScalingConfigArgs']]):
        pulumi.set(self, "scaling_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of tags to apply to the nodegroup.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def taints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.eks.NodeGroupTaintArgs']]]]:
        return pulumi.get(self, "taints")

    @taints.setter
    def taints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.eks.NodeGroupTaintArgs']]]]):
        pulumi.set(self, "taints", value)


class AttachedNodeGroup(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_type: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[float]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 scaling_config: Optional[pulumi.Input[pulumi.InputType['pulumi_aws.eks.NodeGroupScalingConfigArgs']]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.eks.NodeGroupTaintArgs']]]]] = None,
                 __props__=None):
        """
        Create a AttachedNodeGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] capacity_type: The capacity type of the nodegroup.
        :param pulumi.Input[str] cluster_name: The cluster name to attach the nodegroup tp.
        :param pulumi.Input[float] disk_size: The size of the disk to attach to the nodes.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value map of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to apply to the nodegroup.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttachedNodeGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AttachedNodeGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AttachedNodeGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttachedNodeGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capacity_type: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 disk_size: Optional[pulumi.Input[float]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 scaling_config: Optional[pulumi.Input[pulumi.InputType['pulumi_aws.eks.NodeGroupScalingConfigArgs']]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 taints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.eks.NodeGroupTaintArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttachedNodeGroupArgs.__new__(AttachedNodeGroupArgs)

            if capacity_type is None:
                capacity_type = 'ON_DEMAND'
            __props__.__dict__["capacity_type"] = capacity_type
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if disk_size is None:
                disk_size = 20
            __props__.__dict__["disk_size"] = disk_size
            __props__.__dict__["instance_types"] = instance_types
            __props__.__dict__["labels"] = labels
            __props__.__dict__["scaling_config"] = scaling_config
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["taints"] = taints
            __props__.__dict__["node_group"] = None
            __props__.__dict__["node_role"] = None
        super(AttachedNodeGroup, __self__).__init__(
            'lbrlabs-eks:index:AttachedNodeGroup',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="nodeGroup")
    def node_group(self) -> pulumi.Output['pulumi_aws.eks.NodeGroup']:
        return pulumi.get(self, "node_group")

    @property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> pulumi.Output['pulumi_aws.iam.Role']:
        return pulumi.get(self, "node_role")

