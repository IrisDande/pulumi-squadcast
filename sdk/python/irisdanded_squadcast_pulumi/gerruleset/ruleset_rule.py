# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RulesetRuleArgs', 'RulesetRule']

@pulumi.input_type
class RulesetRuleArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[Mapping[str, pulumi.Input[str]]],
                 alert_source: pulumi.Input[str],
                 description: pulumi.Input[str],
                 expression: pulumi.Input[str],
                 ger_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a RulesetRule resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] action: Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        :param pulumi.Input[str] alert_source: An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        :param pulumi.Input[str] description: GER Ruleset Rule description.
        :param pulumi.Input[str] expression: An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        :param pulumi.Input[str] ger_id: GER id.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "alert_source", alert_source)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "ger_id", ger_id)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[Mapping[str, pulumi.Input[str]]]:
        """
        Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[Mapping[str, pulumi.Input[str]]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="alertSource")
    def alert_source(self) -> pulumi.Input[str]:
        """
        An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        """
        return pulumi.get(self, "alert_source")

    @alert_source.setter
    def alert_source(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_source", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        GER Ruleset Rule description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        """
        An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter(name="gerId")
    def ger_id(self) -> pulumi.Input[str]:
        """
        GER id.
        """
        return pulumi.get(self, "ger_id")

    @ger_id.setter
    def ger_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ger_id", value)


@pulumi.input_type
class _RulesetRuleState:
    def __init__(__self__, *,
                 action: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 alert_source: Optional[pulumi.Input[str]] = None,
                 alert_source_shortname: Optional[pulumi.Input[str]] = None,
                 alert_source_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 ger_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RulesetRule resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] action: Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        :param pulumi.Input[str] alert_source: An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        :param pulumi.Input[str] alert_source_shortname: Shortname of the linked alert source.
        :param pulumi.Input[str] alert_source_version: Version of the linked alert source.
        :param pulumi.Input[str] description: GER Ruleset Rule description.
        :param pulumi.Input[str] expression: An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        :param pulumi.Input[str] ger_id: GER id.
        """
        if action is not None:
            pulumi.set(__self__, "action", action)
        if alert_source is not None:
            pulumi.set(__self__, "alert_source", alert_source)
        if alert_source_shortname is not None:
            pulumi.set(__self__, "alert_source_shortname", alert_source_shortname)
        if alert_source_version is not None:
            pulumi.set(__self__, "alert_source_version", alert_source_version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expression is not None:
            pulumi.set(__self__, "expression", expression)
        if ger_id is not None:
            pulumi.set(__self__, "ger_id", ger_id)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="alertSource")
    def alert_source(self) -> Optional[pulumi.Input[str]]:
        """
        An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        """
        return pulumi.get(self, "alert_source")

    @alert_source.setter
    def alert_source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_source", value)

    @property
    @pulumi.getter(name="alertSourceShortname")
    def alert_source_shortname(self) -> Optional[pulumi.Input[str]]:
        """
        Shortname of the linked alert source.
        """
        return pulumi.get(self, "alert_source_shortname")

    @alert_source_shortname.setter
    def alert_source_shortname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_source_shortname", value)

    @property
    @pulumi.getter(name="alertSourceVersion")
    def alert_source_version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the linked alert source.
        """
        return pulumi.get(self, "alert_source_version")

    @alert_source_version.setter
    def alert_source_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_source_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        GER Ruleset Rule description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def expression(self) -> Optional[pulumi.Input[str]]:
        """
        An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        """
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter(name="gerId")
    def ger_id(self) -> Optional[pulumi.Input[str]]:
        """
        GER id.
        """
        return pulumi.get(self, "ger_id")

    @ger_id.setter
    def ger_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ger_id", value)


class RulesetRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 alert_source: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 ger_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        GER Ruleset Rules are a set of conditions defined within a Global Event Ruleset. These rules have expressions, whose evaluation will determine the destination service for the incoming events.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="Example Team")
        example_user = squadcast.get_user(email="john@example.com")
        example_service = squadcast.get_service(name="Example Service",
            team_id=example_team.id)
        example_ger = squadcast.Ger("exampleGer",
            description="Example GER Description",
            team_id=example_team.id,
            entity_owner=squadcast.GerEntityOwnerArgs(
                id=example_user.id,
                type="user",
            ))
        example_ger_ruleset = squadcast.ger.Ruleset("exampleGerRuleset",
            ger_id=example_ger.id,
            alert_source="Prometheus",
            catch_all_action={
                "route_to": example_service.id,
            })
        example_ger_ruleset_rule = squadcast.ger_ruleset.RulesetRule("exampleGerRulesetRule",
            ger_id=example_ger.id,
            alert_source=example_ger_ruleset.alert_source,
            expression="alertname == \\"DeploymentReplicasNotUpdated\\"",
            description="Example GER Ruleset Rule",
            action={
                "route_to": example_service.id,
            })
        ```

        ## Import

        gerID:alertSourceName:ruleID

        ```sh
        $ pulumi import squadcast:GerRuleset/rulesetRule:RulesetRule ger_ruleset_rule_import "50:Grafana:100"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] action: Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        :param pulumi.Input[str] alert_source: An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        :param pulumi.Input[str] description: GER Ruleset Rule description.
        :param pulumi.Input[str] expression: An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        :param pulumi.Input[str] ger_id: GER id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RulesetRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        GER Ruleset Rules are a set of conditions defined within a Global Event Ruleset. These rules have expressions, whose evaluation will determine the destination service for the incoming events.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="Example Team")
        example_user = squadcast.get_user(email="john@example.com")
        example_service = squadcast.get_service(name="Example Service",
            team_id=example_team.id)
        example_ger = squadcast.Ger("exampleGer",
            description="Example GER Description",
            team_id=example_team.id,
            entity_owner=squadcast.GerEntityOwnerArgs(
                id=example_user.id,
                type="user",
            ))
        example_ger_ruleset = squadcast.ger.Ruleset("exampleGerRuleset",
            ger_id=example_ger.id,
            alert_source="Prometheus",
            catch_all_action={
                "route_to": example_service.id,
            })
        example_ger_ruleset_rule = squadcast.ger_ruleset.RulesetRule("exampleGerRulesetRule",
            ger_id=example_ger.id,
            alert_source=example_ger_ruleset.alert_source,
            expression="alertname == \\"DeploymentReplicasNotUpdated\\"",
            description="Example GER Ruleset Rule",
            action={
                "route_to": example_service.id,
            })
        ```

        ## Import

        gerID:alertSourceName:ruleID

        ```sh
        $ pulumi import squadcast:GerRuleset/rulesetRule:RulesetRule ger_ruleset_rule_import "50:Grafana:100"
        ```

        :param str resource_name: The name of the resource.
        :param RulesetRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulesetRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 alert_source: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expression: Optional[pulumi.Input[str]] = None,
                 ger_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RulesetRuleArgs.__new__(RulesetRuleArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if alert_source is None and not opts.urn:
                raise TypeError("Missing required property 'alert_source'")
            __props__.__dict__["alert_source"] = alert_source
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if expression is None and not opts.urn:
                raise TypeError("Missing required property 'expression'")
            __props__.__dict__["expression"] = expression
            if ger_id is None and not opts.urn:
                raise TypeError("Missing required property 'ger_id'")
            __props__.__dict__["ger_id"] = ger_id
            __props__.__dict__["alert_source_shortname"] = None
            __props__.__dict__["alert_source_version"] = None
        super(RulesetRule, __self__).__init__(
            'squadcast:GerRuleset/rulesetRule:RulesetRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            alert_source: Optional[pulumi.Input[str]] = None,
            alert_source_shortname: Optional[pulumi.Input[str]] = None,
            alert_source_version: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expression: Optional[pulumi.Input[str]] = None,
            ger_id: Optional[pulumi.Input[str]] = None) -> 'RulesetRule':
        """
        Get an existing RulesetRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] action: Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        :param pulumi.Input[str] alert_source: An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        :param pulumi.Input[str] alert_source_shortname: Shortname of the linked alert source.
        :param pulumi.Input[str] alert_source_version: Version of the linked alert source.
        :param pulumi.Input[str] description: GER Ruleset Rule description.
        :param pulumi.Input[str] expression: An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        :param pulumi.Input[str] ger_id: GER id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RulesetRuleState.__new__(_RulesetRuleState)

        __props__.__dict__["action"] = action
        __props__.__dict__["alert_source"] = alert_source
        __props__.__dict__["alert_source_shortname"] = alert_source_shortname
        __props__.__dict__["alert_source_version"] = alert_source_version
        __props__.__dict__["description"] = description
        __props__.__dict__["expression"] = expression
        __props__.__dict__["ger_id"] = ger_id
        return RulesetRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="alertSource")
    def alert_source(self) -> pulumi.Output[str]:
        """
        An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        """
        return pulumi.get(self, "alert_source")

    @property
    @pulumi.getter(name="alertSourceShortname")
    def alert_source_shortname(self) -> pulumi.Output[str]:
        """
        Shortname of the linked alert source.
        """
        return pulumi.get(self, "alert_source_shortname")

    @property
    @pulumi.getter(name="alertSourceVersion")
    def alert_source_version(self) -> pulumi.Output[str]:
        """
        Version of the linked alert source.
        """
        return pulumi.get(self, "alert_source_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        GER Ruleset Rule description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Output[str]:
        """
        An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter(name="gerId")
    def ger_id(self) -> pulumi.Output[str]:
        """
        GER id.
        """
        return pulumi.get(self, "ger_id")

