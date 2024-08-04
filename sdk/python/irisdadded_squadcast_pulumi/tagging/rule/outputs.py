# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'V2BasicExpression',
    'V2Tag',
]

@pulumi.output_type
class V2BasicExpression(dict):
    def __init__(__self__, *,
                 lhs: str,
                 op: str,
                 rhs: str):
        """
        :param str lhs: left hand side dropdown value
        :param str op: operator (is, is*not, matches, not*contains)
        :param str rhs: right hand side value
        """
        pulumi.set(__self__, "lhs", lhs)
        pulumi.set(__self__, "op", op)
        pulumi.set(__self__, "rhs", rhs)

    @property
    @pulumi.getter
    def lhs(self) -> str:
        """
        left hand side dropdown value
        """
        return pulumi.get(self, "lhs")

    @property
    @pulumi.getter
    def op(self) -> str:
        """
        operator (is, is*not, matches, not*contains)
        """
        return pulumi.get(self, "op")

    @property
    @pulumi.getter
    def rhs(self) -> str:
        """
        right hand side value
        """
        return pulumi.get(self, "rhs")


@pulumi.output_type
class V2Tag(dict):
    def __init__(__self__, *,
                 color: str,
                 key: str,
                 value: str):
        """
        :param str color: Tag color, hex values
        :param str key: key
        :param str value: value
        """
        pulumi.set(__self__, "color", color)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def color(self) -> str:
        """
        Tag color, hex values
        """
        return pulumi.get(self, "color")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        key
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        value
        """
        return pulumi.get(self, "value")


