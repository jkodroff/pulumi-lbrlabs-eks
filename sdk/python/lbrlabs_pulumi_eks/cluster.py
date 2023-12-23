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
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 enable_cert_manager: Optional[bool] = None,
                 enable_cloud_watch_agent: Optional[bool] = None,
                 enable_external_dns: Optional[bool] = None,
                 enable_otel: Optional[bool] = None,
                 lets_encrypt_email: Optional[pulumi.Input[str]] = None,
                 system_node_desired_count: Optional[pulumi.Input[float]] = None,
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_max_count: Optional[pulumi.Input[float]] = None,
                 system_node_min_count: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] certificate_arn: The ARN of the certificate to use for the ingress controller.
        :param bool enable_cert_manager: Whether to enable cert-manager with route 53 integration.
        :param bool enable_cloud_watch_agent: Whether to enable cloudwatch container insights for EKS.
        :param bool enable_external_dns: Whether to enable external dns with route 53 integration.
        :param bool enable_otel: Whether to enable the OTEL Distro for EKS.
        :param pulumi.Input[str] lets_encrypt_email: The email address to use to issue certificates from Lets Encrypt.
        :param pulumi.Input[float] system_node_desired_count: The initial number of nodes in the system autoscaling group.
        :param pulumi.Input[float] system_node_max_count: The maximum number of nodes in the system autoscaling group.
        :param pulumi.Input[float] system_node_min_count: The minimum number of nodes in the system autoscaling group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to apply to the cluster.
        """
        pulumi.set(__self__, "cluster_subnet_ids", cluster_subnet_ids)
        pulumi.set(__self__, "system_node_subnet_ids", system_node_subnet_ids)
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if enable_cert_manager is None:
            enable_cert_manager = True
        if enable_cert_manager is not None:
            pulumi.set(__self__, "enable_cert_manager", enable_cert_manager)
        if enable_cloud_watch_agent is None:
            enable_cloud_watch_agent = False
        if enable_cloud_watch_agent is not None:
            pulumi.set(__self__, "enable_cloud_watch_agent", enable_cloud_watch_agent)
        if enable_external_dns is None:
            enable_external_dns = True
        if enable_external_dns is not None:
            pulumi.set(__self__, "enable_external_dns", enable_external_dns)
        if enable_otel is None:
            enable_otel = False
        if enable_otel is not None:
            pulumi.set(__self__, "enable_otel", enable_otel)
        if lets_encrypt_email is not None:
            pulumi.set(__self__, "lets_encrypt_email", lets_encrypt_email)
        if system_node_desired_count is not None:
            pulumi.set(__self__, "system_node_desired_count", system_node_desired_count)
        if system_node_instance_types is not None:
            pulumi.set(__self__, "system_node_instance_types", system_node_instance_types)
        if system_node_max_count is not None:
            pulumi.set(__self__, "system_node_max_count", system_node_max_count)
        if system_node_min_count is not None:
            pulumi.set(__self__, "system_node_min_count", system_node_min_count)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the certificate to use for the ingress controller.
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="enableCertManager")
    def enable_cert_manager(self) -> Optional[bool]:
        """
        Whether to enable cert-manager with route 53 integration.
        """
        return pulumi.get(self, "enable_cert_manager")

    @enable_cert_manager.setter
    def enable_cert_manager(self, value: Optional[bool]):
        pulumi.set(self, "enable_cert_manager", value)

    @property
    @pulumi.getter(name="enableCloudWatchAgent")
    def enable_cloud_watch_agent(self) -> Optional[bool]:
        """
        Whether to enable cloudwatch container insights for EKS.
        """
        return pulumi.get(self, "enable_cloud_watch_agent")

    @enable_cloud_watch_agent.setter
    def enable_cloud_watch_agent(self, value: Optional[bool]):
        pulumi.set(self, "enable_cloud_watch_agent", value)

    @property
    @pulumi.getter(name="enableExternalDns")
    def enable_external_dns(self) -> Optional[bool]:
        """
        Whether to enable external dns with route 53 integration.
        """
        return pulumi.get(self, "enable_external_dns")

    @enable_external_dns.setter
    def enable_external_dns(self, value: Optional[bool]):
        pulumi.set(self, "enable_external_dns", value)

    @property
    @pulumi.getter(name="enableOtel")
    def enable_otel(self) -> Optional[bool]:
        """
        Whether to enable the OTEL Distro for EKS.
        """
        return pulumi.get(self, "enable_otel")

    @enable_otel.setter
    def enable_otel(self, value: Optional[bool]):
        pulumi.set(self, "enable_otel", value)

    @property
    @pulumi.getter(name="letsEncryptEmail")
    def lets_encrypt_email(self) -> Optional[pulumi.Input[str]]:
        """
        The email address to use to issue certificates from Lets Encrypt.
        """
        return pulumi.get(self, "lets_encrypt_email")

    @lets_encrypt_email.setter
    def lets_encrypt_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lets_encrypt_email", value)

    @property
    @pulumi.getter(name="systemNodeDesiredCount")
    def system_node_desired_count(self) -> Optional[pulumi.Input[float]]:
        """
        The initial number of nodes in the system autoscaling group.
        """
        return pulumi.get(self, "system_node_desired_count")

    @system_node_desired_count.setter
    def system_node_desired_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "system_node_desired_count", value)

    @property
    @pulumi.getter(name="systemNodeInstanceTypes")
    def system_node_instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "system_node_instance_types")

    @system_node_instance_types.setter
    def system_node_instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "system_node_instance_types", value)

    @property
    @pulumi.getter(name="systemNodeMaxCount")
    def system_node_max_count(self) -> Optional[pulumi.Input[float]]:
        """
        The maximum number of nodes in the system autoscaling group.
        """
        return pulumi.get(self, "system_node_max_count")

    @system_node_max_count.setter
    def system_node_max_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "system_node_max_count", value)

    @property
    @pulumi.getter(name="systemNodeMinCount")
    def system_node_min_count(self) -> Optional[pulumi.Input[float]]:
        """
        The minimum number of nodes in the system autoscaling group.
        """
        return pulumi.get(self, "system_node_min_count")

    @system_node_min_count.setter
    def system_node_min_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "system_node_min_count", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value map of tags to apply to the cluster.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Cluster(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 cluster_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_cert_manager: Optional[bool] = None,
                 enable_cloud_watch_agent: Optional[bool] = None,
                 enable_external_dns: Optional[bool] = None,
                 enable_otel: Optional[bool] = None,
                 lets_encrypt_email: Optional[pulumi.Input[str]] = None,
                 system_node_desired_count: Optional[pulumi.Input[float]] = None,
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_max_count: Optional[pulumi.Input[float]] = None,
                 system_node_min_count: Optional[pulumi.Input[float]] = None,
                 system_node_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a Cluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_arn: The ARN of the certificate to use for the ingress controller.
        :param bool enable_cert_manager: Whether to enable cert-manager with route 53 integration.
        :param bool enable_cloud_watch_agent: Whether to enable cloudwatch container insights for EKS.
        :param bool enable_external_dns: Whether to enable external dns with route 53 integration.
        :param bool enable_otel: Whether to enable the OTEL Distro for EKS.
        :param pulumi.Input[str] lets_encrypt_email: The email address to use to issue certificates from Lets Encrypt.
        :param pulumi.Input[float] system_node_desired_count: The initial number of nodes in the system autoscaling group.
        :param pulumi.Input[float] system_node_max_count: The maximum number of nodes in the system autoscaling group.
        :param pulumi.Input[float] system_node_min_count: The minimum number of nodes in the system autoscaling group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to apply to the cluster.
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
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 cluster_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enable_cert_manager: Optional[bool] = None,
                 enable_cloud_watch_agent: Optional[bool] = None,
                 enable_external_dns: Optional[bool] = None,
                 enable_otel: Optional[bool] = None,
                 lets_encrypt_email: Optional[pulumi.Input[str]] = None,
                 system_node_desired_count: Optional[pulumi.Input[float]] = None,
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_max_count: Optional[pulumi.Input[float]] = None,
                 system_node_min_count: Optional[pulumi.Input[float]] = None,
                 system_node_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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

            __props__.__dict__["certificate_arn"] = certificate_arn
            if cluster_subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_subnet_ids'")
            __props__.__dict__["cluster_subnet_ids"] = cluster_subnet_ids
            if enable_cert_manager is None:
                enable_cert_manager = True
            __props__.__dict__["enable_cert_manager"] = enable_cert_manager
            if enable_cloud_watch_agent is None:
                enable_cloud_watch_agent = False
            __props__.__dict__["enable_cloud_watch_agent"] = enable_cloud_watch_agent
            if enable_external_dns is None:
                enable_external_dns = True
            __props__.__dict__["enable_external_dns"] = enable_external_dns
            if enable_otel is None:
                enable_otel = False
            __props__.__dict__["enable_otel"] = enable_otel
            __props__.__dict__["lets_encrypt_email"] = lets_encrypt_email
            __props__.__dict__["system_node_desired_count"] = system_node_desired_count
            __props__.__dict__["system_node_instance_types"] = system_node_instance_types
            __props__.__dict__["system_node_max_count"] = system_node_max_count
            __props__.__dict__["system_node_min_count"] = system_node_min_count
            if system_node_subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'system_node_subnet_ids'")
            __props__.__dict__["system_node_subnet_ids"] = system_node_subnet_ids
            __props__.__dict__["tags"] = tags
            __props__.__dict__["cluster_name"] = None
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
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        The cluster name
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="controlPlane")
    def control_plane(self) -> pulumi.Output['pulumi_aws.eks.Cluster']:
        """
        The Cluster control plane
        """
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
        """
        The OIDC provider for this cluster.
        """
        return pulumi.get(self, "oidc_provider")

    @property
    @pulumi.getter(name="systemNodes")
    def system_nodes(self) -> pulumi.Output['pulumi_aws.eks.NodeGroup']:
        """
        The system node group.
        """
        return pulumi.get(self, "system_nodes")

