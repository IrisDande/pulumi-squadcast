# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['StatusPageComponentArgs', 'StatusPageComponent']

@pulumi.input_type
class StatusPageComponentArgs:
    def __init__(__self__, *,
                 status_page_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StatusPageComponent resource.
        :param pulumi.Input[str] status_page_id: Id of the status page to which this component belongs to.
        :param pulumi.Input[str] description: Description of the status page component.
        :param pulumi.Input[str] group_id: Id of the group to which this component belongs to.
        :param pulumi.Input[str] name: Name of the status page component.
        """
        pulumi.set(__self__, "status_page_id", status_page_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="statusPageId")
    def status_page_id(self) -> pulumi.Input[str]:
        """
        Id of the status page to which this component belongs to.
        """
        return pulumi.get(self, "status_page_id")

    @status_page_id.setter
    def status_page_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "status_page_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the status page component.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the group to which this component belongs to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the status page component.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _StatusPageComponentState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status_page_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering StatusPageComponent resources.
        :param pulumi.Input[str] description: Description of the status page component.
        :param pulumi.Input[str] group_id: Id of the group to which this component belongs to.
        :param pulumi.Input[str] name: Name of the status page component.
        :param pulumi.Input[str] status_page_id: Id of the status page to which this component belongs to.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status_page_id is not None:
            pulumi.set(__self__, "status_page_id", status_page_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the status page component.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the group to which this component belongs to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the status page component.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="statusPageId")
    def status_page_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of the status page to which this component belongs to.
        """
        return pulumi.get(self, "status_page_id")

    @status_page_id.setter
    def status_page_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status_page_id", value)


class StatusPageComponent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status_page_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Status page component defines a component that represents a specific element within a status page. This resource enables you to configure various attributes of the component, and optionally associate it with a group on the status page.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        team = squadcast.get_team(name="Default Team")
        user = squadcast.get_user(email="john@example.com")
        test_status_page = squadcast.StatusPage("testStatusPage",
            team_id=team.id,
            description="Status Page description",
            is_public=True,
            domain_name="test-statuspage",
            timezone="Asia/Kolkata",
            contact_email="example@test.com",
            theme_color=squadcast.StatusPageThemeColorArgs(
                primary="#000000",
                secondary="#dddddd",
            ),
            owner=squadcast.StatusPageOwnerArgs(
                type="user",
                id=user.id,
            ))
        example_group = squadcast.StatusPageGroup("exampleGroup", status_page_id=test_status_page.id)
        example_component = squadcast.StatusPageComponent("exampleComponent",
            status_page_id=test_status_page.id,
            description="Component 1 description",
            group_id=example_group.id)
        ```

        ## Import

        statusPageID:componentID

        ```sh
        $ pulumi import squadcast:index/statusPageComponent:StatusPageComponent test_component 300:573
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the status page component.
        :param pulumi.Input[str] group_id: Id of the group to which this component belongs to.
        :param pulumi.Input[str] name: Name of the status page component.
        :param pulumi.Input[str] status_page_id: Id of the status page to which this component belongs to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StatusPageComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Status page component defines a component that represents a specific element within a status page. This resource enables you to configure various attributes of the component, and optionally associate it with a group on the status page.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        team = squadcast.get_team(name="Default Team")
        user = squadcast.get_user(email="john@example.com")
        test_status_page = squadcast.StatusPage("testStatusPage",
            team_id=team.id,
            description="Status Page description",
            is_public=True,
            domain_name="test-statuspage",
            timezone="Asia/Kolkata",
            contact_email="example@test.com",
            theme_color=squadcast.StatusPageThemeColorArgs(
                primary="#000000",
                secondary="#dddddd",
            ),
            owner=squadcast.StatusPageOwnerArgs(
                type="user",
                id=user.id,
            ))
        example_group = squadcast.StatusPageGroup("exampleGroup", status_page_id=test_status_page.id)
        example_component = squadcast.StatusPageComponent("exampleComponent",
            status_page_id=test_status_page.id,
            description="Component 1 description",
            group_id=example_group.id)
        ```

        ## Import

        statusPageID:componentID

        ```sh
        $ pulumi import squadcast:index/statusPageComponent:StatusPageComponent test_component 300:573
        ```

        :param str resource_name: The name of the resource.
        :param StatusPageComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StatusPageComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status_page_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StatusPageComponentArgs.__new__(StatusPageComponentArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["name"] = name
            if status_page_id is None and not opts.urn:
                raise TypeError("Missing required property 'status_page_id'")
            __props__.__dict__["status_page_id"] = status_page_id
        super(StatusPageComponent, __self__).__init__(
            'squadcast:index/statusPageComponent:StatusPageComponent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            status_page_id: Optional[pulumi.Input[str]] = None) -> 'StatusPageComponent':
        """
        Get an existing StatusPageComponent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the status page component.
        :param pulumi.Input[str] group_id: Id of the group to which this component belongs to.
        :param pulumi.Input[str] name: Name of the status page component.
        :param pulumi.Input[str] status_page_id: Id of the status page to which this component belongs to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _StatusPageComponentState.__new__(_StatusPageComponentState)

        __props__.__dict__["description"] = description
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["name"] = name
        __props__.__dict__["status_page_id"] = status_page_id
        return StatusPageComponent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the status page component.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[Optional[str]]:
        """
        Id of the group to which this component belongs to.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the status page component.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="statusPageId")
    def status_page_id(self) -> pulumi.Output[str]:
        """
        Id of the status page to which this component belongs to.
        """
        return pulumi.get(self, "status_page_id")

