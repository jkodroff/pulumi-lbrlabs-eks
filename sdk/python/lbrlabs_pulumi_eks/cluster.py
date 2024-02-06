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
                 cert_manager_version: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 eks_iam_auth_controller_version: Optional[pulumi.Input[str]] = None,
                 enable_cert_manager: Optional[bool] = None,
                 enable_cloud_watch_agent: Optional[bool] = None,
                 enable_external_dns: Optional[bool] = None,
                 enable_external_ingress: Optional[bool] = None,
                 enable_internal_ingress: Optional[bool] = None,
                 enable_karpenter: Optional[bool] = None,
                 enable_otel: Optional[bool] = None,
                 enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 external_dns_version: Optional[pulumi.Input[str]] = None,
                 lb_type: Optional[pulumi.Input[str]] = None,
                 lets_encrypt_email: Optional[str] = None,
                 nginx_ingress_version: Optional[pulumi.Input[str]] = None,
                 system_node_desired_count: Optional[pulumi.Input[float]] = None,
                 system_node_instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 system_node_max_count: Optional[pulumi.Input[float]] = None,
                 system_node_min_count: Optional[pulumi.Input[float]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] cert_manager_version: The version of the cert-manager helm chart to deploy.
        :param pulumi.Input[str] certificate_arn: The ARN of the certificate to use for the ingress controller.
        :param pulumi.Input[str] cluster_version: The version of the EKS cluster to create.
        :param pulumi.Input[str] eks_iam_auth_controller_version: The version of the eks-iam-auth-controller helm chart to deploy.
        :param bool enable_cert_manager: Whether to enable cert-manager with route 53 integration.
        :param bool enable_cloud_watch_agent: Whether to enable cloudwatch container insights for EKS.
        :param bool enable_external_dns: Whether to enable external dns with route 53 integration.
        :param bool enable_external_ingress: Whether to create an ingress controller for external traffic.
        :param bool enable_internal_ingress: Whether to create an ingress controller for internal traffic.
        :param bool enable_karpenter: Whether to enable karpenter.
        :param bool enable_otel: Whether to enable the OTEL Distro for EKS.
        :param pulumi.Input[str] external_dns_version: The version of the external-dns helm chart to deploy.
        :param pulumi.Input[str] lb_type: The type of loadbalancer to provision.
        :param str lets_encrypt_email: The email address to use to issue certificates from Lets Encrypt.
        :param pulumi.Input[str] nginx_ingress_version: The version of the nginx ingress controller helm chart to deploy.
        :param pulumi.Input[float] system_node_desired_count: The initial number of nodes in the system autoscaling group.
        :param pulumi.Input[float] system_node_max_count: The maximum number of nodes in the system autoscaling group.
        :param pulumi.Input[float] system_node_min_count: The minimum number of nodes in the system autoscaling group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of tags to apply to the cluster.
        """
        pulumi.set(__self__, "cluster_subnet_ids", cluster_subnet_ids)
        pulumi.set(__self__, "system_node_subnet_ids", system_node_subnet_ids)
        if cert_manager_version is not None:
            pulumi.set(__self__, "cert_manager_version", cert_manager_version)
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if cluster_version is not None:
            pulumi.set(__self__, "cluster_version", cluster_version)
        if eks_iam_auth_controller_version is not None:
            pulumi.set(__self__, "eks_iam_auth_controller_version", eks_iam_auth_controller_version)
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
        if enable_external_ingress is None:
            enable_external_ingress = True
        if enable_external_ingress is not None:
            pulumi.set(__self__, "enable_external_ingress", enable_external_ingress)
        if enable_internal_ingress is None:
            enable_internal_ingress = True
        if enable_internal_ingress is not None:
            pulumi.set(__self__, "enable_internal_ingress", enable_internal_ingress)
        if enable_karpenter is None:
            enable_karpenter = True
        if enable_karpenter is not None:
            pulumi.set(__self__, "enable_karpenter", enable_karpenter)
        if enable_otel is None:
            enable_otel = False
        if enable_otel is not None:
            pulumi.set(__self__, "enable_otel", enable_otel)
        if enabled_cluster_log_types is not None:
            pulumi.set(__self__, "enabled_cluster_log_types", enabled_cluster_log_types)
        if external_dns_version is not None:
            pulumi.set(__self__, "external_dns_version", external_dns_version)
        if lb_type is None:
            lb_type = 'nlb'
        if lb_type is not None:
            pulumi.set(__self__, "lb_type", lb_type)
        if lets_encrypt_email is not None:
            pulumi.set(__self__, "lets_encrypt_email", lets_encrypt_email)
        if nginx_ingress_version is not None:
            pulumi.set(__self__, "nginx_ingress_version", nginx_ingress_version)
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
    @pulumi.getter(name="certManagerVersion")
    def cert_manager_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the cert-manager helm chart to deploy.
        """
        return pulumi.get(self, "cert_manager_version")

    @cert_manager_version.setter
    def cert_manager_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_manager_version", value)

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
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the EKS cluster to create.
        """
        return pulumi.get(self, "cluster_version")

    @cluster_version.setter
    def cluster_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_version", value)

    @property
    @pulumi.getter(name="eksIamAuthControllerVersion")
    def eks_iam_auth_controller_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the eks-iam-auth-controller helm chart to deploy.
        """
        return pulumi.get(self, "eks_iam_auth_controller_version")

    @eks_iam_auth_controller_version.setter
    def eks_iam_auth_controller_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eks_iam_auth_controller_version", value)

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
    @pulumi.getter(name="enableExternalIngress")
    def enable_external_ingress(self) -> Optional[bool]:
        """
        Whether to create an ingress controller for external traffic.
        """
        return pulumi.get(self, "enable_external_ingress")

    @enable_external_ingress.setter
    def enable_external_ingress(self, value: Optional[bool]):
        pulumi.set(self, "enable_external_ingress", value)

    @property
    @pulumi.getter(name="enableInternalIngress")
    def enable_internal_ingress(self) -> Optional[bool]:
        """
        Whether to create an ingress controller for internal traffic.
        """
        return pulumi.get(self, "enable_internal_ingress")

    @enable_internal_ingress.setter
    def enable_internal_ingress(self, value: Optional[bool]):
        pulumi.set(self, "enable_internal_ingress", value)

    @property
    @pulumi.getter(name="enableKarpenter")
    def enable_karpenter(self) -> Optional[bool]:
        """
        Whether to enable karpenter.
        """
        return pulumi.get(self, "enable_karpenter")

    @enable_karpenter.setter
    def enable_karpenter(self, value: Optional[bool]):
        pulumi.set(self, "enable_karpenter", value)

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
    @pulumi.getter(name="enabledClusterLogTypes")
    def enabled_cluster_log_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "enabled_cluster_log_types")

    @enabled_cluster_log_types.setter
    def enabled_cluster_log_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "enabled_cluster_log_types", value)

    @property
    @pulumi.getter(name="externalDNSVersion")
    def external_dns_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the external-dns helm chart to deploy.
        """
        return pulumi.get(self, "external_dns_version")

    @external_dns_version.setter
    def external_dns_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_dns_version", value)

    @property
    @pulumi.getter(name="lbType")
    def lb_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of loadbalancer to provision.
        """
        return pulumi.get(self, "lb_type")

    @lb_type.setter
    def lb_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lb_type", value)

    @property
    @pulumi.getter(name="letsEncryptEmail")
    def lets_encrypt_email(self) -> Optional[str]:
        """
        The email address to use to issue certificates from Lets Encrypt.
        """
        return pulumi.get(self, "lets_encrypt_email")

    @lets_encrypt_email.setter
    def lets_encrypt_email(self, value: Optional[str]):
        pulumi.set(self, "lets_encrypt_email", value)

    @property
    @pulumi.getter(name="nginxIngressVersion")
    def nginx_ingress_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the nginx ingress controller helm chart to deploy.
        """
        return pulumi.get(self, "nginx_ingress_version")

    @nginx_ingress_version.setter
    def nginx_ingress_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nginx_ingress_version", value)

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
                 cert_manager_version: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 cluster_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 eks_iam_auth_controller_version: Optional[pulumi.Input[str]] = None,
                 enable_cert_manager: Optional[bool] = None,
                 enable_cloud_watch_agent: Optional[bool] = None,
                 enable_external_dns: Optional[bool] = None,
                 enable_external_ingress: Optional[bool] = None,
                 enable_internal_ingress: Optional[bool] = None,
                 enable_karpenter: Optional[bool] = None,
                 enable_otel: Optional[bool] = None,
                 enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 external_dns_version: Optional[pulumi.Input[str]] = None,
                 lb_type: Optional[pulumi.Input[str]] = None,
                 lets_encrypt_email: Optional[str] = None,
                 nginx_ingress_version: Optional[pulumi.Input[str]] = None,
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
        :param pulumi.Input[str] cert_manager_version: The version of the cert-manager helm chart to deploy.
        :param pulumi.Input[str] certificate_arn: The ARN of the certificate to use for the ingress controller.
        :param pulumi.Input[str] cluster_version: The version of the EKS cluster to create.
        :param pulumi.Input[str] eks_iam_auth_controller_version: The version of the eks-iam-auth-controller helm chart to deploy.
        :param bool enable_cert_manager: Whether to enable cert-manager with route 53 integration.
        :param bool enable_cloud_watch_agent: Whether to enable cloudwatch container insights for EKS.
        :param bool enable_external_dns: Whether to enable external dns with route 53 integration.
        :param bool enable_external_ingress: Whether to create an ingress controller for external traffic.
        :param bool enable_internal_ingress: Whether to create an ingress controller for internal traffic.
        :param bool enable_karpenter: Whether to enable karpenter.
        :param bool enable_otel: Whether to enable the OTEL Distro for EKS.
        :param pulumi.Input[str] external_dns_version: The version of the external-dns helm chart to deploy.
        :param pulumi.Input[str] lb_type: The type of loadbalancer to provision.
        :param str lets_encrypt_email: The email address to use to issue certificates from Lets Encrypt.
        :param pulumi.Input[str] nginx_ingress_version: The version of the nginx ingress controller helm chart to deploy.
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
                 cert_manager_version: Optional[pulumi.Input[str]] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 cluster_subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cluster_version: Optional[pulumi.Input[str]] = None,
                 eks_iam_auth_controller_version: Optional[pulumi.Input[str]] = None,
                 enable_cert_manager: Optional[bool] = None,
                 enable_cloud_watch_agent: Optional[bool] = None,
                 enable_external_dns: Optional[bool] = None,
                 enable_external_ingress: Optional[bool] = None,
                 enable_internal_ingress: Optional[bool] = None,
                 enable_karpenter: Optional[bool] = None,
                 enable_otel: Optional[bool] = None,
                 enabled_cluster_log_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 external_dns_version: Optional[pulumi.Input[str]] = None,
                 lb_type: Optional[pulumi.Input[str]] = None,
                 lets_encrypt_email: Optional[str] = None,
                 nginx_ingress_version: Optional[pulumi.Input[str]] = None,
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

            __props__.__dict__["cert_manager_version"] = cert_manager_version
            __props__.__dict__["certificate_arn"] = certificate_arn
            if cluster_subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_subnet_ids'")
            __props__.__dict__["cluster_subnet_ids"] = cluster_subnet_ids
            __props__.__dict__["cluster_version"] = cluster_version
            __props__.__dict__["eks_iam_auth_controller_version"] = eks_iam_auth_controller_version
            if enable_cert_manager is None:
                enable_cert_manager = True
            __props__.__dict__["enable_cert_manager"] = enable_cert_manager
            if enable_cloud_watch_agent is None:
                enable_cloud_watch_agent = False
            __props__.__dict__["enable_cloud_watch_agent"] = enable_cloud_watch_agent
            if enable_external_dns is None:
                enable_external_dns = True
            __props__.__dict__["enable_external_dns"] = enable_external_dns
            if enable_external_ingress is None:
                enable_external_ingress = True
            __props__.__dict__["enable_external_ingress"] = enable_external_ingress
            if enable_internal_ingress is None:
                enable_internal_ingress = True
            __props__.__dict__["enable_internal_ingress"] = enable_internal_ingress
            if enable_karpenter is None:
                enable_karpenter = True
            __props__.__dict__["enable_karpenter"] = enable_karpenter
            if enable_otel is None:
                enable_otel = False
            __props__.__dict__["enable_otel"] = enable_otel
            __props__.__dict__["enabled_cluster_log_types"] = enabled_cluster_log_types
            __props__.__dict__["external_dns_version"] = external_dns_version
            if lb_type is None:
                lb_type = 'nlb'
            __props__.__dict__["lb_type"] = lb_type
            __props__.__dict__["lets_encrypt_email"] = lets_encrypt_email
            __props__.__dict__["nginx_ingress_version"] = nginx_ingress_version
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
            __props__.__dict__["karpenter_node_role"] = None
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
    @pulumi.getter(name="karpenterNodeRole")
    def karpenter_node_role(self) -> pulumi.Output[Optional['pulumi_aws.iam.Role']]:
        """
        The role created for karpenter nodes.
        """
        return pulumi.get(self, "karpenter_node_role")

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

