# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .cluster import *
from .provider import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "lbrlabs-eks",
  "mod": "index",
  "fqn": "lbrlabs_pulumi_eks",
  "classes": {
   "lbrlabs-eks:index:Cluster": "Cluster"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "lbrlabs-eks",
  "token": "pulumi:providers:lbrlabs-eks",
  "fqn": "lbrlabs_pulumi_eks",
  "class": "Provider"
 }
]
"""
)