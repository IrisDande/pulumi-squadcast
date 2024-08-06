# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MemberArgs', 'Member']

@pulumi.input_type
class MemberArgs:
    def __init__(__self__, *,
                 role_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 team_id: pulumi.Input[str],
                 user_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a Member resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: role ids.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] user_id: user id (ObjectId).
        """
        pulumi.set(__self__, "role_ids", role_ids)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        role ids.
        """
        return pulumi.get(self, "role_ids")

    @role_ids.setter
    def role_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "role_ids", value)

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
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        user id (ObjectId).
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)


@pulumi.input_type
class _MemberState:
    def __init__(__self__, *,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Member resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: role ids.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] user_id: user id (ObjectId).
        """
        if role_ids is not None:
            pulumi.set(__self__, "role_ids", role_ids)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        role ids.
        """
        return pulumi.get(self, "role_ids")

    @role_ids.setter
    def role_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "role_ids", value)

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
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        user id (ObjectId).
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class Member(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        You can manage the members of a Team here.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_user = squadcast.get_user(email="test@example.com")
        example_team_role = squadcast.Team.get_role(name="example role name",
            team_id=example_team.id)
        example_team_member = squadcast.team.Member("exampleTeamMember",
            team_id=example_team.id,
            user_id=example_user.id,
            role_ids=[example_team_role.id])
        ```

        ## Import

        teamID:emailID

        Use 'Get All Teams' API to get the id of the team

        ```sh
        $ pulumi import squadcast:Team/member:Member example_resource_name 62d2fe23a57381088224d726:test@example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: role ids.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] user_id: user id (ObjectId).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        You can manage the members of a Team here.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        example_team = squadcast.get_team(name="example team name")
        example_user = squadcast.get_user(email="test@example.com")
        example_team_role = squadcast.Team.get_role(name="example role name",
            team_id=example_team.id)
        example_team_member = squadcast.team.Member("exampleTeamMember",
            team_id=example_team.id,
            user_id=example_user.id,
            role_ids=[example_team_role.id])
        ```

        ## Import

        teamID:emailID

        Use 'Get All Teams' API to get the id of the team

        ```sh
        $ pulumi import squadcast:Team/member:Member example_resource_name 62d2fe23a57381088224d726:test@example.com
        ```

        :param str resource_name: The name of the resource.
        :param MemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MemberArgs.__new__(MemberArgs)

            if role_ids is None and not opts.urn:
                raise TypeError("Missing required property 'role_ids'")
            __props__.__dict__["role_ids"] = role_ids
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
        super(Member, __self__).__init__(
            'squadcast:Team/member:Member',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            role_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'Member':
        """
        Get an existing Member resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] role_ids: role ids.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[str] user_id: user id (ObjectId).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MemberState.__new__(_MemberState)

        __props__.__dict__["role_ids"] = role_ids
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["user_id"] = user_id
        return Member(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="roleIds")
    def role_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        role ids.
        """
        return pulumi.get(self, "role_ids")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        user id (ObjectId).
        """
        return pulumi.get(self, "user_id")

