# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSquadResult',
    'AwaitableGetSquadResult',
    'get_squad',
    'get_squad_output',
]

@pulumi.output_type
class GetSquadResult:
    """
    A collection of values returned by getSquad.
    """
    def __init__(__self__, id=None, member_ids=None, name=None, team_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_ids and not isinstance(member_ids, list):
            raise TypeError("Expected argument 'member_ids' to be a list")
        pulumi.set(__self__, "member_ids", member_ids)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Squad id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberIds")
    def member_ids(self) -> Sequence[str]:
        return pulumi.get(self, "member_ids")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Squad.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")


class AwaitableGetSquadResult(GetSquadResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSquadResult(
            id=self.id,
            member_ids=self.member_ids,
            name=self.name,
            team_id=self.team_id)


def get_squad(name: Optional[str] = None,
              team_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSquadResult:
    """
    [Squads](https://support.squadcast.com/docs/squads) are smaller groups of members within Teams. Squads could correspond to groups of people that are responsible for specific projects within a Team.Use this data source to get information about a specific Squad.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_squadcast as squadcast

    test = squadcast.get_squad(name="test",
        team_id="team id")
    ```


    :param str name: Name of the Squad.
    :param str team_id: Team id.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['teamId'] = team_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('squadcast:index/getSquad:getSquad', __args__, opts=opts, typ=GetSquadResult).value

    return AwaitableGetSquadResult(
        id=pulumi.get(__ret__, 'id'),
        member_ids=pulumi.get(__ret__, 'member_ids'),
        name=pulumi.get(__ret__, 'name'),
        team_id=pulumi.get(__ret__, 'team_id'))


@_utilities.lift_output_func(get_squad)
def get_squad_output(name: Optional[pulumi.Input[str]] = None,
                     team_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSquadResult]:
    """
    [Squads](https://support.squadcast.com/docs/squads) are smaller groups of members within Teams. Squads could correspond to groups of people that are responsible for specific projects within a Team.Use this data source to get information about a specific Squad.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_squadcast as squadcast

    test = squadcast.get_squad(name="test",
        team_id="team id")
    ```


    :param str name: Name of the Squad.
    :param str team_id: Team id.
    """
    ...
