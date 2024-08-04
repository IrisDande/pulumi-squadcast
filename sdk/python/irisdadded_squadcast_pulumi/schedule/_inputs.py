# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'V2EntityOwnerArgs',
    'V2TagArgs',
]

@pulumi.input_type
class V2EntityOwnerArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] id: Schedule owner id.
        :param pulumi.Input[str] type: Schedule owner type. Supported values are 'user' or 'squad'.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Schedule owner id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Schedule owner type. Supported values are 'user' or 'squad'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class V2TagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str],
                 color: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key: Schedule tag key.
        :param pulumi.Input[str] value: Schedule tag value.
        :param pulumi.Input[str] color: Schedule tag color.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)
        if color is not None:
            pulumi.set(__self__, "color", color)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Schedule tag key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Schedule tag value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def color(self) -> Optional[pulumi.Input[str]]:
        """
        Schedule tag color.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color", value)


