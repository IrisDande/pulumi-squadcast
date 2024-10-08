# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SquadArgs', 'Squad']

@pulumi.input_type
class SquadArgs:
    def __init__(__self__, *,
                 member_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 team_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Squad resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] member_ids: User ObjectId.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] name: Name of the Squad.
        """
        pulumi.set(__self__, "member_ids", member_ids)
        pulumi.set(__self__, "team_id", team_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="memberIds")
    def member_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        User ObjectId.
        """
        return pulumi.get(self, "member_ids")

    @member_ids.setter
    def member_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "member_ids", value)

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
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Squad.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SquadState:
    def __init__(__self__, *,
                 member_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Squad resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] member_ids: User ObjectId.
        :param pulumi.Input[str] name: Name of the Squad.
        :param pulumi.Input[str] team_id: Team id.
        """
        if member_ids is not None:
            pulumi.set(__self__, "member_ids", member_ids)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter(name="memberIds")
    def member_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        User ObjectId.
        """
        return pulumi.get(self, "member_ids")

    @member_ids.setter
    def member_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "member_ids", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Squad.
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


class Squad(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 member_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [Squads](https://support.squadcast.com/docs/squads) are smaller groups of members within Teams. Squads could correspond to groups of people that are responsible for specific projects within a Team. The name of the Squad must be unique within a Team.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example test name")
        example_user = squadcast.get_user(email="test@example.com")
        example_squad = squadcast.Squad("exampleSquad",
            team_id=example_team.id,
            member_ids=[example_user.id])
        ```

        ## Import

        teamID:squadID

        Use 'Get All Teams' and 'Get All Squads' APIs to get the id of the squad and slo respectively

        ```sh
        $ pulumi import squadcast:index/squad:Squad test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] member_ids: User ObjectId.
        :param pulumi.Input[str] name: Name of the Squad.
        :param pulumi.Input[str] team_id: Team id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SquadArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Squads](https://support.squadcast.com/docs/squads) are smaller groups of members within Teams. Squads could correspond to groups of people that are responsible for specific projects within a Team. The name of the Squad must be unique within a Team.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example test name")
        example_user = squadcast.get_user(email="test@example.com")
        example_squad = squadcast.Squad("exampleSquad",
            team_id=example_team.id,
            member_ids=[example_user.id])
        ```

        ## Import

        teamID:squadID

        Use 'Get All Teams' and 'Get All Squads' APIs to get the id of the squad and slo respectively

        ```sh
        $ pulumi import squadcast:index/squad:Squad test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
        ```

        :param str resource_name: The name of the resource.
        :param SquadArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SquadArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 member_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SquadArgs.__new__(SquadArgs)

            if member_ids is None and not opts.urn:
                raise TypeError("Missing required property 'member_ids'")
            __props__.__dict__["member_ids"] = member_ids
            __props__.__dict__["name"] = name
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
        super(Squad, __self__).__init__(
            'squadcast:index/squad:Squad',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            member_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'Squad':
        """
        Get an existing Squad resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] member_ids: User ObjectId.
        :param pulumi.Input[str] name: Name of the Squad.
        :param pulumi.Input[str] team_id: Team id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SquadState.__new__(_SquadState)

        __props__.__dict__["member_ids"] = member_ids
        __props__.__dict__["name"] = name
        __props__.__dict__["team_id"] = team_id
        return Squad(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="memberIds")
    def member_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        User ObjectId.
        """
        return pulumi.get(self, "member_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Squad.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

