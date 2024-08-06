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

__all__ = ['V2Args', 'V2']

@pulumi.input_type
class V2Args:
    def __init__(__self__, *,
                 entity_owner: pulumi.Input['V2EntityOwnerArgs'],
                 team_id: pulumi.Input[str],
                 timezone: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]]] = None):
        """
        The set of arguments for constructing a V2 resource.
        :param pulumi.Input['V2EntityOwnerArgs'] entity_owner: Schedule owner.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] timezone: Timezone for the schedule.
        :param pulumi.Input[str] description: Detailed description about the schedule.
        :param pulumi.Input[str] name: Name of the schedule.
        :param pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]] tags: Schedule tags.
        """
        pulumi.set(__self__, "entity_owner", entity_owner)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "timezone", timezone)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="entityOwner")
    def entity_owner(self) -> pulumi.Input['V2EntityOwnerArgs']:
        """
        Schedule owner.
        """
        return pulumi.get(self, "entity_owner")

    @entity_owner.setter
    def entity_owner(self, value: pulumi.Input['V2EntityOwnerArgs']):
        pulumi.set(self, "entity_owner", value)

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

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Input[str]:
        """
        Timezone for the schedule.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: pulumi.Input[str]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Detailed description about the schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]]]:
        """
        Schedule tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _V2State:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 entity_owner: Optional[pulumi.Input['V2EntityOwnerArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering V2 resources.
        :param pulumi.Input[str] description: Detailed description about the schedule.
        :param pulumi.Input['V2EntityOwnerArgs'] entity_owner: Schedule owner.
        :param pulumi.Input[str] name: Name of the schedule.
        :param pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]] tags: Schedule tags.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] timezone: Timezone for the schedule.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if entity_owner is not None:
            pulumi.set(__self__, "entity_owner", entity_owner)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Detailed description about the schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="entityOwner")
    def entity_owner(self) -> Optional[pulumi.Input['V2EntityOwnerArgs']]:
        """
        Schedule owner.
        """
        return pulumi.get(self, "entity_owner")

    @entity_owner.setter
    def entity_owner(self, value: Optional[pulumi.Input['V2EntityOwnerArgs']]):
        pulumi.set(self, "entity_owner", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]]]:
        """
        Schedule tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['V2TagArgs']]]]):
        pulumi.set(self, "tags", value)

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

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        Timezone for the schedule.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


class V2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entity_owner: Optional[pulumi.Input[pulumi.InputType['V2EntityOwnerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['V2TagArgs']]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. The name of the Schedule must be unique within a Team.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_user = squadcast.get_user(email="test@example.com")
        schedule_test = squadcast.schedule.V2("scheduleTest",
            description="test schedule",
            timezone="Asia/Kolkata",
            team_id=example_team.id,
            entity_owner=squadcast.schedule.V2EntityOwnerArgs(
                id=example_user.id,
                type="user",
            ),
            tags=[
                squadcast.schedule.V2TagArgs(
                    key="testkey",
                    value="testval",
                ),
                squadcast.schedule.V2TagArgs(
                    key="testkey2",
                    value="testval2",
                ),
            ])
        ```

        ## Import

        teamID:scheduleName

        Use 'Get All Teams' API to get the id of the team

        ```sh
        $ pulumi import squadcast:Schedule/v2:V2 schedule_test "62d2fe23a57381088224d726:Example Schedule"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Detailed description about the schedule.
        :param pulumi.Input[pulumi.InputType['V2EntityOwnerArgs']] entity_owner: Schedule owner.
        :param pulumi.Input[str] name: Name of the schedule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['V2TagArgs']]]] tags: Schedule tags.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] timezone: Timezone for the schedule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: V2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. The name of the Schedule must be unique within a Team.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_user = squadcast.get_user(email="test@example.com")
        schedule_test = squadcast.schedule.V2("scheduleTest",
            description="test schedule",
            timezone="Asia/Kolkata",
            team_id=example_team.id,
            entity_owner=squadcast.schedule.V2EntityOwnerArgs(
                id=example_user.id,
                type="user",
            ),
            tags=[
                squadcast.schedule.V2TagArgs(
                    key="testkey",
                    value="testval",
                ),
                squadcast.schedule.V2TagArgs(
                    key="testkey2",
                    value="testval2",
                ),
            ])
        ```

        ## Import

        teamID:scheduleName

        Use 'Get All Teams' API to get the id of the team

        ```sh
        $ pulumi import squadcast:Schedule/v2:V2 schedule_test "62d2fe23a57381088224d726:Example Schedule"
        ```

        :param str resource_name: The name of the resource.
        :param V2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(V2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entity_owner: Optional[pulumi.Input[pulumi.InputType['V2EntityOwnerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['V2TagArgs']]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = V2Args.__new__(V2Args)

            __props__.__dict__["description"] = description
            if entity_owner is None and not opts.urn:
                raise TypeError("Missing required property 'entity_owner'")
            __props__.__dict__["entity_owner"] = entity_owner
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            if timezone is None and not opts.urn:
                raise TypeError("Missing required property 'timezone'")
            __props__.__dict__["timezone"] = timezone
        super(V2, __self__).__init__(
            'squadcast:Schedule/v2:V2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            entity_owner: Optional[pulumi.Input[pulumi.InputType['V2EntityOwnerArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['V2TagArgs']]]]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            timezone: Optional[pulumi.Input[str]] = None) -> 'V2':
        """
        Get an existing V2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Detailed description about the schedule.
        :param pulumi.Input[pulumi.InputType['V2EntityOwnerArgs']] entity_owner: Schedule owner.
        :param pulumi.Input[str] name: Name of the schedule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['V2TagArgs']]]] tags: Schedule tags.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] timezone: Timezone for the schedule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _V2State.__new__(_V2State)

        __props__.__dict__["description"] = description
        __props__.__dict__["entity_owner"] = entity_owner
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["timezone"] = timezone
        return V2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Detailed description about the schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="entityOwner")
    def entity_owner(self) -> pulumi.Output['outputs.V2EntityOwner']:
        """
        Schedule owner.
        """
        return pulumi.get(self, "entity_owner")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.V2Tag']]]:
        """
        Schedule tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[str]:
        """
        Timezone for the schedule.
        """
        return pulumi.get(self, "timezone")

