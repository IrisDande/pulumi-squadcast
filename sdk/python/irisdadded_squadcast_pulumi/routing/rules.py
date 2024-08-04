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

__all__ = ['RulesArgs', 'Rules']

@pulumi.input_type
class RulesArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['RulesRuleArgs']]],
                 service_id: pulumi.Input[str],
                 team_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Rules resource.
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] team_id: Team id.
        """
        pulumi.set(__self__, "rules", rules)
        pulumi.set(__self__, "service_id", service_id)
        pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['RulesRuleArgs']]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['RulesRuleArgs']]]):
        pulumi.set(self, "rules", value)

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
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)


@pulumi.input_type
class _RulesState:
    def __init__(__self__, *,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['RulesRuleArgs']]]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Rules resources.
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] team_id: Team id.
        """
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if service_id is not None:
            pulumi.set(__self__, "service_id", service_id)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulesRuleArgs']]]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulesRuleArgs']]]]):
        pulumi.set(self, "rules", value)

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
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


class Rules(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesRuleArgs']]]]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [Routing rules](https://support.squadcast.com/docs/alert-routing) allows you to ensure that alerts are routed to the right responder with the help of `event tags` attached to them.

        ## Example Usage

        ```python
        import pulumi
        import irisdadded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_user = squadcast.get_user(email="test@example.com")
        example_service = squadcast.get_service(name="example service name",
            team_id=example_team.id)
        example_escalaion_policy = squadcast.escalation.get_policy(name="example escalation policy name",
            team_id=example_team.id)
        example_squad = squadcast.get_squad(name="example squad name",
            team_id=example_team.id)
        example_routing_rules = squadcast.routing.Rules("exampleRoutingRules",
            team_id=example_team.id,
            service_id=example_service.id,
            rules=[
                squadcast.routing.RulesRuleArgs(
                    is_basic=False,
                    expression="payload[\\"event_id\\"] == 40",
                    route_to_id=example_escalaion_policy.id,
                    route_to_type="escalationpolicy",
                ),
                squadcast.routing.RulesRuleArgs(
                    is_basic=True,
                    basic_expressions=[squadcast.routing.RulesRuleBasicExpressionArgs(
                        lhs="payload[\\"foo\\"]",
                        rhs="bar",
                    )],
                    route_to_id=example_user.id,
                    route_to_type="user",
                ),
            ])
        ```

        ## Import

        teamID:serviceID

        Use 'Get All Teams' and 'Get All Services' APIs to get the id of the team and service respectively

        ```sh
        $ pulumi import squadcast:routing/rules:Rules test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] team_id: Team id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RulesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Routing rules](https://support.squadcast.com/docs/alert-routing) allows you to ensure that alerts are routed to the right responder with the help of `event tags` attached to them.

        ## Example Usage

        ```python
        import pulumi
        import irisdadded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_user = squadcast.get_user(email="test@example.com")
        example_service = squadcast.get_service(name="example service name",
            team_id=example_team.id)
        example_escalaion_policy = squadcast.escalation.get_policy(name="example escalation policy name",
            team_id=example_team.id)
        example_squad = squadcast.get_squad(name="example squad name",
            team_id=example_team.id)
        example_routing_rules = squadcast.routing.Rules("exampleRoutingRules",
            team_id=example_team.id,
            service_id=example_service.id,
            rules=[
                squadcast.routing.RulesRuleArgs(
                    is_basic=False,
                    expression="payload[\\"event_id\\"] == 40",
                    route_to_id=example_escalaion_policy.id,
                    route_to_type="escalationpolicy",
                ),
                squadcast.routing.RulesRuleArgs(
                    is_basic=True,
                    basic_expressions=[squadcast.routing.RulesRuleBasicExpressionArgs(
                        lhs="payload[\\"foo\\"]",
                        rhs="bar",
                    )],
                    route_to_id=example_user.id,
                    route_to_type="user",
                ),
            ])
        ```

        ## Import

        teamID:serviceID

        Use 'Get All Teams' and 'Get All Services' APIs to get the id of the team and service respectively

        ```sh
        $ pulumi import squadcast:routing/rules:Rules test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
        ```

        :param str resource_name: The name of the resource.
        :param RulesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesRuleArgs']]]]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RulesArgs.__new__(RulesArgs)

            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            if service_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_id'")
            __props__.__dict__["service_id"] = service_id
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
        super(Rules, __self__).__init__(
            'squadcast:routing/rules:Rules',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesRuleArgs']]]]] = None,
            service_id: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'Rules':
        """
        Get an existing Rules resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] service_id: Service id.
        :param pulumi.Input[str] team_id: Team id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RulesState.__new__(_RulesState)

        __props__.__dict__["rules"] = rules
        __props__.__dict__["service_id"] = service_id
        __props__.__dict__["team_id"] = team_id
        return Rules(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.RulesRule']]:
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[str]:
        """
        Service id.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

