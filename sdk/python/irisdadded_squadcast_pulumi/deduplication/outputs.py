# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'RulesRule',
    'RulesRuleBasicExpression',
]

@pulumi.output_type
class RulesRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "isBasic":
            suggest = "is_basic"
        elif key == "basicExpressions":
            suggest = "basic_expressions"
        elif key == "dependencyDeduplication":
            suggest = "dependency_deduplication"
        elif key == "timeUnit":
            suggest = "time_unit"
        elif key == "timeWindow":
            suggest = "time_window"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RulesRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RulesRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RulesRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 is_basic: bool,
                 basic_expressions: Optional[Sequence['outputs.RulesRuleBasicExpression']] = None,
                 dependency_deduplication: Optional[bool] = None,
                 description: Optional[str] = None,
                 expression: Optional[str] = None,
                 time_unit: Optional[str] = None,
                 time_window: Optional[int] = None):
        """
        :param bool is_basic: is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        :param Sequence['RulesRuleBasicExpressionArgs'] basic_expressions: The basic expression which needs to be evaluated to be true for this rule to apply.
        :param bool dependency_deduplication: Denotes if dependent services should also be deduplicated
        :param str description: description.
        :param str expression: The expression which needs to be evaluated to be true for this rule to apply.
        :param str time_unit: time unit (mins or hours)
        :param int time_window: integer for time_unit
        """
        pulumi.set(__self__, "is_basic", is_basic)
        if basic_expressions is not None:
            pulumi.set(__self__, "basic_expressions", basic_expressions)
        if dependency_deduplication is not None:
            pulumi.set(__self__, "dependency_deduplication", dependency_deduplication)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if time_unit is not None:
            pulumi.set(__self__, "time_unit", time_unit)
        if time_window is not None:
            pulumi.set(__self__, "time_window", time_window)

    @property
    @pulumi.getter(name="isBasic")
    def is_basic(self) -> bool:
        """
        is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        """
        return pulumi.get(self, "is_basic")

    @property
    @pulumi.getter(name="basicExpressions")
    def basic_expressions(self) -> Optional[Sequence['outputs.RulesRuleBasicExpression']]:
        """
        The basic expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "basic_expressions")

    @property
    @pulumi.getter(name="dependencyDeduplication")
    def dependency_deduplication(self) -> Optional[bool]:
        """
        Denotes if dependent services should also be deduplicated
        """
        return pulumi.get(self, "dependency_deduplication")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> Optional[str]:
        """
        The expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[str]:
        """
        time unit (mins or hours)
        """
        return pulumi.get(self, "time_unit")

    @property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[int]:
        """
        integer for time_unit
        """
        return pulumi.get(self, "time_window")


@pulumi.output_type
class RulesRuleBasicExpression(dict):
    def __init__(__self__, *,
                 lhs: str,
                 op: str,
                 rhs: str):
        """
        :param str lhs: left hand side dropdown value
        :param str op: operator
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
        operator
        """
        return pulumi.get(self, "op")

    @property
    @pulumi.getter
    def rhs(self) -> str:
        """
        right hand side value
        """
        return pulumi.get(self, "rhs")


