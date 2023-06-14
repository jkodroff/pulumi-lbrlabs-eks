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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cluster_subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 system_node_subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: pulumi.Input[str],
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] vpc_id: The VPC ID to create the cluster in.
        """
        pulumi.set(__self__, "cluster_subnet_ids", cluster_subnet_ids)
        pulumi.set(__self__, "system_node_subnet_ids", system_node_subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if system_node_instance_types is not None:
            pulumi.set(__self__, "system_node_instance_types", system_node_instance_types)

    @property
    @pulumi.getter(name="clusterSubnetIds")
    def cluster_subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "cluster_subnet_ids")

    @cluster_subnet_ids.setter
    def cluster_subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "cluster_subnet_ids", value)

    @property
    @pulumi.getter(name="systemNodeSubnetIds")
    def system_node_subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "system_node_subnet_ids")

    @system_node_subnet_ids.setter
    def system_node_subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "system_node_subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        """
        The VPC ID to create the cluster in.
        """
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="systemNodeInstanceTypes")
    def system_node_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "system_node_instance_types")

    @system_node_instance_types.setter
    def system_node_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "system_node_instance_types", value)


class Cluster(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] vpc_id: The VPC ID to create the cluster in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if cluster_subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_subnet_ids'")
            __props__.__dict__["cluster_subnet_ids"] = cluster_subnet_ids
            __props__.__dict__["system_node_instance_types"] = system_node_instance_types
            if system_node_subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'system_node_subnet_ids'")
            __props__.__dict__["system_node_subnet_ids"] = system_node_subnet_ids
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["control_plane"] = None
            __props__.__dict__["kubeconfig"] = None
            __props__.__dict__["oidc_provider"] = None
            __props__.__dict__["system_nodes"] = None
        super(Cluster, __self__).__init__(
            'lbrlabs-eks:index:Cluster',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output['pulumi_aws.eks.Cluster']:
        return pulumi.get(self, "control_plane")

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output[str]:
        """
        The kubeconfig for this cluster.
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter(name="oidcProvider")
    def oidc_provider(self) -> pulumi.Output['pulumi_aws.iam.OpenIdConnectProvider']:
        return pulumi.get(self, "oidc_provider")

    @property
    @pulumi.getter(name="systemNodes")
    def system_nodes(self) -> pulumi.Output['pulumi_aws.eks.NodeGroup']:
        return pulumi.get(self, "system_nodes")

