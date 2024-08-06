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
from ._inputs import *

__all__ = ['RuleV2Args', 'RuleV2']

@pulumi.input_type
class RuleV2Args:
    def __init__(__self__, *,
                 is_basic: pulumi.Input[bool],
                 service_id: pulumi.Input[str],
                 basic_expressions: Optional[pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]]] = None,
                 dependency_deduplication: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 time_unit: Optional[pulumi.Input[str]] = None,
                 time_window: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a RuleV2 resource.
        :param pulumi.Input[bool] is_basic: is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]] basic_expressions: The basic expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] dependency_deduplication: Denotes if dependent services should also be deduplicated
        :param pulumi.Input[str] description: description.
        :param pulumi.Input[str] expression: The expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[str] time_unit: time unit (mins or hours)
        :param pulumi.Input[int] time_window: integer for time_unit
        """
        pulumi.set(__self__, "is_basic", is_basic)
        pulumi.set(__self__, "service_id", service_id)
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
    def is_basic(self) -> pulumi.Input[bool]:
        """
        is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        """
        return pulumi.get(self, "is_basic")

    @is_basic.setter
    def is_basic(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_basic", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[str]:
        """
        Service id.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter(name="basicExpressions")
    def basic_expressions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]]]:
        """
        The basic expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "basic_expressions")

    @basic_expressions.setter
    def basic_expressions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]]]):
        pulumi.set(self, "basic_expressions", value)

    @property
    @pulumi.getter(name="dependencyDeduplication")
    def dependency_deduplication(self) -> Optional[pulumi.Input[bool]]:
        """
        Denotes if dependent services should also be deduplicated
        """
        return pulumi.get(self, "dependency_deduplication")

    @dependency_deduplication.setter
    def dependency_deduplication(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dependency_deduplication", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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

    @property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[str]]:
        """
        time unit (mins or hours)
        """
        return pulumi.get(self, "time_unit")

    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_unit", value)

    @property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[pulumi.Input[int]]:
        """
        integer for time_unit
        """
        return pulumi.get(self, "time_window")

    @time_window.setter
    def time_window(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "time_window", value)


@pulumi.input_type
class _RuleV2State:
    def __init__(__self__, *,
                 basic_expressions: Optional[pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]]] = None,
                 dependency_deduplication: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 is_basic: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 time_unit: Optional[pulumi.Input[str]] = None,
                 time_window: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering RuleV2 resources.
        :param pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]] basic_expressions: The basic expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] dependency_deduplication: Denotes if dependent services should also be deduplicated
        :param pulumi.Input[str] description: description.
        :param pulumi.Input[str] expression: The expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] is_basic: is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] time_unit: time unit (mins or hours)
        :param pulumi.Input[int] time_window: integer for time_unit
        """
        if basic_expressions is not None:
            pulumi.set(__self__, "basic_expressions", basic_expressions)
        if dependency_deduplication is not None:
            pulumi.set(__self__, "dependency_deduplication", dependency_deduplication)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if is_basic is not None:
            pulumi.set(__self__, "is_basic", is_basic)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if time_unit is not None:
            pulumi.set(__self__, "time_unit", time_unit)
        if time_window is not None:
            pulumi.set(__self__, "time_window", time_window)

    @property
    @pulumi.getter(name="basicExpressions")
    def basic_expressions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]]]:
        """
        The basic expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "basic_expressions")

    @basic_expressions.setter
    def basic_expressions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RuleV2BasicExpressionArgs']]]]):
        pulumi.set(self, "basic_expressions", value)

    @property
    @pulumi.getter(name="dependencyDeduplication")
    def dependency_deduplication(self) -> Optional[pulumi.Input[bool]]:
        """
        Denotes if dependent services should also be deduplicated
        """
        return pulumi.get(self, "dependency_deduplication")

    @dependency_deduplication.setter
    def dependency_deduplication(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dependency_deduplication", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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

    @property
    @pulumi.getter(name="isBasic")
    def is_basic(self) -> Optional[pulumi.Input[bool]]:
        """
        is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        """
        return pulumi.get(self, "is_basic")

    @is_basic.setter
    def is_basic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_basic", value)

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[str]]:
        """
        Service id.
        """
        return pulumi.get(self, "service_id")

    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_id", value)

    @property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[str]]:
        """
        time unit (mins or hours)
        """
        return pulumi.get(self, "time_unit")

    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_unit", value)

    @property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> Optional[pulumi.Input[int]]:
        """
        integer for time_unit
        """
        return pulumi.get(self, "time_window")

    @time_window.setter
    def time_window(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "time_window", value)


class RuleV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_expressions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RuleV2BasicExpressionArgs']]]]] = None,
                 dependency_deduplication: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 is_basic: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 time_unit: Optional[pulumi.Input[str]] = None,
                 time_window: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        [Deduplication rules](https://support.squadcast.com/docs/de-duplication-rules) can help you reduce alert noise by organising and grouping alerts. This also provides easy access to similar alerts when needed. When these rules evaluate to true for an incoming incident, alerts will get deduplicated.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_service = squadcast.get_service(name="example service name",
            team_id=example_team.id)
        example_deduplication_rule = squadcast.deduplication_rule.RuleV2("exampleDeduplicationRule",
            service_id=example_service.id,
            is_basic=False,
            description="not basic",
            expression="payload[\\"event_id\\"] == 40")
        example_basic_deduplication_rule = squadcast.deduplication_rule.RuleV2("exampleBasicDeduplicationRule",
            service_id=example_service.id,
            is_basic=True,
            description="basic",
            dependency_deduplication=True,
            time_window=2,
            time_unit="hour",
            basic_expressions=[squadcast.deduplication_rule.RuleV2BasicExpressionArgs(
                lhs="payload[\\"foo\\"]",
                op="is",
                rhs="bar",
            )])
        ```

        ## Import

        serviceID:ruleID

        ```sh
        $ pulumi import squadcast:DeduplicationRule/ruleV2:RuleV2 test_resource_name 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RuleV2BasicExpressionArgs']]]] basic_expressions: The basic expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] dependency_deduplication: Denotes if dependent services should also be deduplicated
        :param pulumi.Input[str] description: description.
        :param pulumi.Input[str] expression: The expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] is_basic: is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] time_unit: time unit (mins or hours)
        :param pulumi.Input[int] time_window: integer for time_unit
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RuleV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Deduplication rules](https://support.squadcast.com/docs/de-duplication-rules) can help you reduce alert noise by organising and grouping alerts. This also provides easy access to similar alerts when needed. When these rules evaluate to true for an incoming incident, alerts will get deduplicated.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_service = squadcast.get_service(name="example service name",
            team_id=example_team.id)
        example_deduplication_rule = squadcast.deduplication_rule.RuleV2("exampleDeduplicationRule",
            service_id=example_service.id,
            is_basic=False,
            description="not basic",
            expression="payload[\\"event_id\\"] == 40")
        example_basic_deduplication_rule = squadcast.deduplication_rule.RuleV2("exampleBasicDeduplicationRule",
            service_id=example_service.id,
            is_basic=True,
            description="basic",
            dependency_deduplication=True,
            time_window=2,
            time_unit="hour",
            basic_expressions=[squadcast.deduplication_rule.RuleV2BasicExpressionArgs(
                lhs="payload[\\"foo\\"]",
                op="is",
                rhs="bar",
            )])
        ```

        ## Import

        serviceID:ruleID

        ```sh
        $ pulumi import squadcast:DeduplicationRule/ruleV2:RuleV2 test_resource_name 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
        ```

        :param str resource_name: The name of the resource.
        :param RuleV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RuleV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 basic_expressions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RuleV2BasicExpressionArgs']]]]] = None,
                 dependency_deduplication: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 is_basic: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 time_unit: Optional[pulumi.Input[str]] = None,
                 time_window: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RuleV2Args.__new__(RuleV2Args)

            __props__.__dict__["basic_expressions"] = basic_expressions
            __props__.__dict__["dependency_deduplication"] = dependency_deduplication
            __props__.__dict__["description"] = description
            __props__.__dict__["expression"] = expression
            if is_basic is None and not opts.urn:
                raise TypeError("Missing required property 'is_basic'")
            __props__.__dict__["is_basic"] = is_basic
            if service_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_id'")
            __props__.__dict__["service_id"] = service_id
            __props__.__dict__["time_unit"] = time_unit
            __props__.__dict__["time_window"] = time_window
        super(RuleV2, __self__).__init__(
            'squadcast:DeduplicationRule/ruleV2:RuleV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            basic_expressions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RuleV2BasicExpressionArgs']]]]] = None,
            dependency_deduplication: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expression: Optional[pulumi.Input[str]] = None,
            is_basic: Optional[pulumi.Input[bool]] = None,
            service_id: Optional[pulumi.Input[str]] = None,
            time_unit: Optional[pulumi.Input[str]] = None,
            time_window: Optional[pulumi.Input[int]] = None) -> 'RuleV2':
        """
        Get an existing RuleV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RuleV2BasicExpressionArgs']]]] basic_expressions: The basic expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] dependency_deduplication: Denotes if dependent services should also be deduplicated
        :param pulumi.Input[str] description: description.
        :param pulumi.Input[str] expression: The expression which needs to be evaluated to be true for this rule to apply.
        :param pulumi.Input[bool] is_basic: is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] time_unit: time unit (mins or hours)
        :param pulumi.Input[int] time_window: integer for time_unit
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RuleV2State.__new__(_RuleV2State)

        __props__.__dict__["basic_expressions"] = basic_expressions
        __props__.__dict__["dependency_deduplication"] = dependency_deduplication
        __props__.__dict__["description"] = description
        __props__.__dict__["expression"] = expression
        __props__.__dict__["is_basic"] = is_basic
        __props__.__dict__["service_id"] = service_id
        __props__.__dict__["time_unit"] = time_unit
        __props__.__dict__["time_window"] = time_window
        return RuleV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="basicExpressions")
    def basic_expressions(self) -> pulumi.Output[Optional[Sequence['outputs.RuleV2BasicExpression']]]:
        """
        The basic expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "basic_expressions")

    @property
    @pulumi.getter(name="dependencyDeduplication")
    def dependency_deduplication(self) -> pulumi.Output[Optional[bool]]:
        """
        Denotes if dependent services should also be deduplicated
        """
        return pulumi.get(self, "dependency_deduplication")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Output[Optional[str]]:
        """
        The expression which needs to be evaluated to be true for this rule to apply.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter(name="isBasic")
    def is_basic(self) -> pulumi.Output[bool]:
        """
        is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
        """
        return pulumi.get(self, "is_basic")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[str]:
        """
        Service id.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> pulumi.Output[Optional[str]]:
        """
        time unit (mins or hours)
        """
        return pulumi.get(self, "time_unit")

    @property
    @pulumi.getter(name="timeWindow")
    def time_window(self) -> pulumi.Output[Optional[int]]:
        """
        integer for time_unit
        """
        return pulumi.get(self, "time_window")

