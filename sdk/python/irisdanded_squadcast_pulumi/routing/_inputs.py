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
    'RulesRuleArgs',
    'RulesRuleBasicExpressionArgs',
]

@pulumi.input_type
class RulesRuleArgs:
    def __init__(__self__, *,
                 is_basic: pulumi.Input[bool],
                 route_to_id: pulumi.Input[str],
                 route_to_type: pulumi.Input[str],
                 basic_expressions: Optional[pulumi.Input[Sequence[pulumi.Input['RulesRuleBasicExpressionArgs']]]] = None,
                 expression: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] is_basic: is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        :param pulumi.Input[str] route_to_id: The id of the entity (user, escalation policy, squad) for which we are routing this incident.
        :param pulumi.Input[str] route_to_type: Type of the entity for which we are routing this incident - User, Escalation Policy or Squad
        :param pulumi.Input[Sequence[pulumi.Input['RulesRuleBasicExpressionArgs']]] basic_expressions: The basic expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[str] expression: The expression which needs to be evaluated to be true for this rule to apply.
        """
        pulumi.set(__self__, "is_basic", is_basic)
        pulumi.set(__self__, "route_to_id", route_to_id)
        pulumi.set(__self__, "route_to_type", route_to_type)
        if basic_expressions is not None:
            pulumi.set(__self__, "basic_expressions", basic_expressions)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)

    @property
    @pulumi.getter(name="isBasic")
    def is_basic(self) -> pulumi.Input[bool]:
        """
        is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        """
        return pulumi.get(self, "is_basic")

    @is_basic.setter
    def is_basic(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_basic", value)

    @property
    @pulumi.getter(name="routeToId")
    def route_to_id(self) -> pulumi.Input[str]:
        """
        The id of the entity (user, escalation policy, squad) for which we are routing this incident.
        """
        return pulumi.get(self, "route_to_id")

    @route_to_id.setter
    def route_to_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_to_id", value)

    @property
    @pulumi.getter(name="routeToType")
    def route_to_type(self) -> pulumi.Input[str]:
        """
        Type of the entity for which we are routing this incident - User, Escalation Policy or Squad
        """
        return pulumi.get(self, "route_to_type")

    @route_to_type.setter
    def route_to_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "route_to_type", value)

    @property
    @pulumi.getter(name="basicExpressions")
    def basic_expressions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulesRuleBasicExpressionArgs']]]]:
        """
        The basic expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "basic_expressions")

    @basic_expressions.setter
    def basic_expressions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulesRuleBasicExpressionArgs']]]]):
        pulumi.set(self, "basic_expressions", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        """
        The expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)


@pulumi.input_type
class RulesRuleBasicExpressionArgs:
    def __init__(__self__, *,
                 lhs: pulumi.Input[str],
                 rhs: pulumi.Input[str]):
        """
        :param pulumi.Input[str] lhs: left hand side dropdown value
        :param pulumi.Input[str] rhs: right hand side value
        """
        pulumi.set(__self__, "lhs", lhs)
        pulumi.set(__self__, "rhs", rhs)

    @property
    @pulumi.getter
    def lhs(self) -> pulumi.Input[str]:
        """
        left hand side dropdown value
        """
        return pulumi.get(self, "lhs")

    @lhs.setter
    def lhs(self, value: pulumi.Input[str]):
        pulumi.set(self, "lhs", value)

    @property
    @pulumi.getter
    def rhs(self) -> pulumi.Input[str]:
        """
        right hand side value
        """
        return pulumi.get(self, "rhs")

    @rhs.setter
    def rhs(self, value: pulumi.Input[str]):
        pulumi.set(self, "rhs", value)


