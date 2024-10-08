# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetScheduleV2Result',
    'AwaitableGetScheduleV2Result',
    'get_schedule_v2',
    'get_schedule_v2_output',
]

@pulumi.output_type
class GetScheduleV2Result:
    """
    A collection of values returned by getScheduleV2.
    """
    def __init__(__self__, description=None, entity_owners=None, id=None, name=None, tags=None, team_id=None, timezone=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if entity_owners and not isinstance(entity_owners, list):
            raise TypeError("Expected argument 'entity_owners' to be a list")
        pulumi.set(__self__, "entity_owners", entity_owners)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)
        if timezone and not isinstance(timezone, str):
            raise TypeError("Expected argument 'timezone' to be a str")
        pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Detailed description about the schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="entityOwners")
    def entity_owners(self) -> Sequence['outputs.GetScheduleV2EntityOwnerResult']:
        """
        Schedule owner.
        """
        return pulumi.get(self, "entity_owners")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Schedule id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetScheduleV2TagResult']:
        """
        Schedule tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def timezone(self) -> str:
        """
        Timezone for the schedule.
        """
        return pulumi.get(self, "timezone")


class AwaitableGetScheduleV2Result(GetScheduleV2Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduleV2Result(
            description=self.description,
            entity_owners=self.entity_owners,
            id=self.id,
            name=self.name,
            tags=self.tags,
            team_id=self.team_id,
            timezone=self.timezone)


def get_schedule_v2(name: Optional[str] = None,
                    team_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduleV2Result:
    """
    [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. Use this data source to get information about a specific schedule that you can use for other Squadcast resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_squadcast as squadcast

    test = squadcast.get_schedule_v2(name=squadcast_schedule_v2["test"]["name"],
        team_id="team_id")
    ```


    :param str name: Name of the Schedule.
    :param str team_id: Team id.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['teamId'] = team_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('squadcast:index/getScheduleV2:getScheduleV2', __args__, opts=opts, typ=GetScheduleV2Result).value

    return AwaitableGetScheduleV2Result(
        description=pulumi.get(__ret__, 'description'),
        entity_owners=pulumi.get(__ret__, 'entity_owners'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'),
        team_id=pulumi.get(__ret__, 'team_id'),
        timezone=pulumi.get(__ret__, 'timezone'))


@_utilities.lift_output_func(get_schedule_v2)
def get_schedule_v2_output(name: Optional[pulumi.Input[str]] = None,
                           team_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduleV2Result]:
    """
    [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. Use this data source to get information about a specific schedule that you can use for other Squadcast resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_squadcast as squadcast

    test = squadcast.get_schedule_v2(name=squadcast_schedule_v2["test"]["name"],
        team_id="team_id")
    ```


    :param str name: Name of the Schedule.
    :param str team_id: Team id.
    """
    ...
