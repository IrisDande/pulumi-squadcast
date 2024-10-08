# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 color: pulumi.Input[str],
                 team_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[str] color: Calendar color scheme for this schedule, hex values.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] description: Detailed description about the Schedule.
        :param pulumi.Input[str] name: Name of the Schedule.
        """
        pulumi.set(__self__, "color", color)
        pulumi.set(__self__, "team_id", team_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def color(self) -> pulumi.Input[str]:
        """
        Calendar color scheme for this schedule, hex values.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: pulumi.Input[str]):
        pulumi.set(self, "color", value)

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
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Detailed description about the Schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ScheduleState:
    def __init__(__self__, *,
                 color: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Schedule resources.
        :param pulumi.Input[str] color: Calendar color scheme for this schedule, hex values.
        :param pulumi.Input[str] description: Detailed description about the Schedule.
        :param pulumi.Input[str] name: Name of the Schedule.
        :param pulumi.Input[str] team_id: Team id.
        """
        if color is not None:
            pulumi.set(__self__, "color", color)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def color(self) -> Optional[pulumi.Input[str]]:
        """
        Calendar color scheme for this schedule, hex values.
        """
        return pulumi.get(self, "color")

    @color.setter
    def color(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "color", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Detailed description about the Schedule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Schedule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [Squadcast schedules](https://support.squadcast.com/docs/schedules) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. The name of the Schedule must be unique within and across Teams.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_schedule = squadcast.Schedule("exampleSchedule",
            team_id=example_team.id,
            color="#9900ef")
        ```

        ## Import

        teamID:scheduleName

        Use 'Get All Teams' API to get the id of the team

        ```sh
        $ pulumi import squadcast:index/schedule:Schedule test "62d2fe23a57381088224d726:Example Schedule"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] color: Calendar color scheme for this schedule, hex values.
        :param pulumi.Input[str] description: Detailed description about the Schedule.
        :param pulumi.Input[str] name: Name of the Schedule.
        :param pulumi.Input[str] team_id: Team id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Squadcast schedules](https://support.squadcast.com/docs/schedules) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. The name of the Schedule must be unique within and across Teams.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_schedule = squadcast.Schedule("exampleSchedule",
            team_id=example_team.id,
            color="#9900ef")
        ```

        ## Import

        teamID:scheduleName

        Use 'Get All Teams' API to get the id of the team

        ```sh
        $ pulumi import squadcast:index/schedule:Schedule test "62d2fe23a57381088224d726:Example Schedule"
        ```

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 color: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            if color is None and not opts.urn:
                raise TypeError("Missing required property 'color'")
            __props__.__dict__["color"] = color
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
        super(Schedule, __self__).__init__(
            'squadcast:index/schedule:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            color: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] color: Calendar color scheme for this schedule, hex values.
        :param pulumi.Input[str] description: Detailed description about the Schedule.
        :param pulumi.Input[str] name: Name of the Schedule.
        :param pulumi.Input[str] team_id: Team id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ScheduleState.__new__(_ScheduleState)

        __props__.__dict__["color"] = color
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["team_id"] = team_id
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def color(self) -> pulumi.Output[str]:
        """
        Calendar color scheme for this schedule, hex values.
        """
        return pulumi.get(self, "color")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Detailed description about the Schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

