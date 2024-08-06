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

__all__ = ['PageArgs', 'Page']

@pulumi.input_type
class PageArgs:
    def __init__(__self__, *,
                 contact_email: pulumi.Input[str],
                 domain_name: pulumi.Input[str],
                 is_public: pulumi.Input[bool],
                 owner: pulumi.Input['PageOwnerArgs'],
                 team_id: pulumi.Input[str],
                 theme_color: pulumi.Input['PageThemeColorArgs'],
                 timezone: pulumi.Input[str],
                 allow_components_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_maintenance_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_webhook_subscription: Optional[pulumi.Input[bool]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 hide_from_search_engines: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Page resource.
        :param pulumi.Input[str] contact_email: Contact email.
        :param pulumi.Input[str] domain_name: Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        :param pulumi.Input[bool] is_public: Determines if the status page is public or not.
        :param pulumi.Input['PageOwnerArgs'] owner: Status page owner.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input['PageThemeColorArgs'] theme_color: Theme color for the status page.
        :param pulumi.Input[str] timezone: Timezone for the status page.
        :param pulumi.Input[bool] allow_components_subscription: Determines if components subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_maintenance_subscription: Determines if maintenance subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_webhook_subscription: Determines if webhook subscription is allowed to the status page.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the status page.
        :param pulumi.Input[str] description: Status page description.
        :param pulumi.Input[bool] hide_from_search_engines: Determines if the status page is hidden from search engines. Applicable on public status pages only.
        :param pulumi.Input[str] name: Status page name.
        """
        pulumi.set(__self__, "contact_email", contact_email)
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "is_public", is_public)
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "theme_color", theme_color)
        pulumi.set(__self__, "timezone", timezone)
        if allow_components_subscription is not None:
            pulumi.set(__self__, "allow_components_subscription", allow_components_subscription)
        if allow_maintenance_subscription is not None:
            pulumi.set(__self__, "allow_maintenance_subscription", allow_maintenance_subscription)
        if allow_webhook_subscription is not None:
            pulumi.set(__self__, "allow_webhook_subscription", allow_webhook_subscription)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if hide_from_search_engines is not None:
            pulumi.set(__self__, "hide_from_search_engines", hide_from_search_engines)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> pulumi.Input[str]:
        """
        Contact email.
        """
        return pulumi.get(self, "contact_email")

    @contact_email.setter
    def contact_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "contact_email", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> pulumi.Input[bool]:
        """
        Determines if the status page is public or not.
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input['PageOwnerArgs']:
        """
        Status page owner.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input['PageOwnerArgs']):
        pulumi.set(self, "owner", value)

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
    @pulumi.getter(name="themeColor")
    def theme_color(self) -> pulumi.Input['PageThemeColorArgs']:
        """
        Theme color for the status page.
        """
        return pulumi.get(self, "theme_color")

    @theme_color.setter
    def theme_color(self, value: pulumi.Input['PageThemeColorArgs']):
        pulumi.set(self, "theme_color", value)

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Input[str]:
        """
        Timezone for the status page.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: pulumi.Input[str]):
        pulumi.set(self, "timezone", value)

    @property
    @pulumi.getter(name="allowComponentsSubscription")
    def allow_components_subscription(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if components subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_components_subscription")

    @allow_components_subscription.setter
    def allow_components_subscription(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_components_subscription", value)

    @property
    @pulumi.getter(name="allowMaintenanceSubscription")
    def allow_maintenance_subscription(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if maintenance subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_maintenance_subscription")

    @allow_maintenance_subscription.setter
    def allow_maintenance_subscription(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_maintenance_subscription", value)

    @property
    @pulumi.getter(name="allowWebhookSubscription")
    def allow_webhook_subscription(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if webhook subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_webhook_subscription")

    @allow_webhook_subscription.setter
    def allow_webhook_subscription(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_webhook_subscription", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom domain name of the status page.
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Status page description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="hideFromSearchEngines")
    def hide_from_search_engines(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if the status page is hidden from search engines. Applicable on public status pages only.
        """
        return pulumi.get(self, "hide_from_search_engines")

    @hide_from_search_engines.setter
    def hide_from_search_engines(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hide_from_search_engines", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Status page name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _PageState:
    def __init__(__self__, *,
                 allow_components_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_maintenance_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_webhook_subscription: Optional[pulumi.Input[bool]] = None,
                 contact_email: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 hide_from_search_engines: Optional[pulumi.Input[bool]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input['PageOwnerArgs']] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 theme_color: Optional[pulumi.Input['PageThemeColorArgs']] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Page resources.
        :param pulumi.Input[bool] allow_components_subscription: Determines if components subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_maintenance_subscription: Determines if maintenance subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_webhook_subscription: Determines if webhook subscription is allowed to the status page.
        :param pulumi.Input[str] contact_email: Contact email.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the status page.
        :param pulumi.Input[str] description: Status page description.
        :param pulumi.Input[str] domain_name: Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        :param pulumi.Input[bool] hide_from_search_engines: Determines if the status page is hidden from search engines. Applicable on public status pages only.
        :param pulumi.Input[bool] is_public: Determines if the status page is public or not.
        :param pulumi.Input[str] name: Status page name.
        :param pulumi.Input['PageOwnerArgs'] owner: Status page owner.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input['PageThemeColorArgs'] theme_color: Theme color for the status page.
        :param pulumi.Input[str] timezone: Timezone for the status page.
        """
        if allow_components_subscription is not None:
            pulumi.set(__self__, "allow_components_subscription", allow_components_subscription)
        if allow_maintenance_subscription is not None:
            pulumi.set(__self__, "allow_maintenance_subscription", allow_maintenance_subscription)
        if allow_webhook_subscription is not None:
            pulumi.set(__self__, "allow_webhook_subscription", allow_webhook_subscription)
        if contact_email is not None:
            pulumi.set(__self__, "contact_email", contact_email)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if hide_from_search_engines is not None:
            pulumi.set(__self__, "hide_from_search_engines", hide_from_search_engines)
        if is_public is not None:
            pulumi.set(__self__, "is_public", is_public)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if theme_color is not None:
            pulumi.set(__self__, "theme_color", theme_color)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter(name="allowComponentsSubscription")
    def allow_components_subscription(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if components subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_components_subscription")

    @allow_components_subscription.setter
    def allow_components_subscription(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_components_subscription", value)

    @property
    @pulumi.getter(name="allowMaintenanceSubscription")
    def allow_maintenance_subscription(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if maintenance subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_maintenance_subscription")

    @allow_maintenance_subscription.setter
    def allow_maintenance_subscription(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_maintenance_subscription", value)

    @property
    @pulumi.getter(name="allowWebhookSubscription")
    def allow_webhook_subscription(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if webhook subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_webhook_subscription")

    @allow_webhook_subscription.setter
    def allow_webhook_subscription(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_webhook_subscription", value)

    @property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> Optional[pulumi.Input[str]]:
        """
        Contact email.
        """
        return pulumi.get(self, "contact_email")

    @contact_email.setter
    def contact_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_email", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom domain name of the status page.
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Status page description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="hideFromSearchEngines")
    def hide_from_search_engines(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if the status page is hidden from search engines. Applicable on public status pages only.
        """
        return pulumi.get(self, "hide_from_search_engines")

    @hide_from_search_engines.setter
    def hide_from_search_engines(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hide_from_search_engines", value)

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines if the status page is public or not.
        """
        return pulumi.get(self, "is_public")

    @is_public.setter
    def is_public(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_public", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Status page name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input['PageOwnerArgs']]:
        """
        Status page owner.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input['PageOwnerArgs']]):
        pulumi.set(self, "owner", value)

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
    @pulumi.getter(name="themeColor")
    def theme_color(self) -> Optional[pulumi.Input['PageThemeColorArgs']]:
        """
        Theme color for the status page.
        """
        return pulumi.get(self, "theme_color")

    @theme_color.setter
    def theme_color(self, value: Optional[pulumi.Input['PageThemeColorArgs']]):
        pulumi.set(self, "theme_color", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        Timezone for the status page.
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


class Page(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_components_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_maintenance_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_webhook_subscription: Optional[pulumi.Input[bool]] = None,
                 contact_email: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 hide_from_search_engines: Optional[pulumi.Input[bool]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[pulumi.InputType['PageOwnerArgs']]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 theme_color: Optional[pulumi.Input[pulumi.InputType['PageThemeColorArgs']]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        [Status Pages](https://www.squadcast.com/blog/status-pages-101-everything-you-need-to-know-about-status-pages) serves as a communication instrument enabling you to notify your customers regarding service interruptions and scheduled maintenance. You can create a status page for each of your services and customize it to your liking. You can also add components & groups to your status page to show the status of your services.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        team = squadcast.get_team(name="Default Team")
        user = squadcast.get_user(email="john@example.com")
        test_status_page = squadcast.status.Page("testStatusPage",
            team_id=team.id,
            description="Status Page description",
            is_public=True,
            domain_name="test-statuspage",
            timezone="Asia/Kolkata",
            contact_email="example@test.com",
            theme_color=squadcast.status.PageThemeColorArgs(
                primary="#000000",
                secondary="#dddddd",
            ),
            owner=squadcast.status.PageOwnerArgs(
                type="user",
                id=user.id,
            ),
            allow_webhook_subscription=True,
            allow_components_subscription=True,
            allow_maintenance_subscription=True)
        ```

        ## Import

        statusPageID

        ```sh
        $ pulumi import squadcast:Status/page:Page test_status_page 285
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_components_subscription: Determines if components subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_maintenance_subscription: Determines if maintenance subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_webhook_subscription: Determines if webhook subscription is allowed to the status page.
        :param pulumi.Input[str] contact_email: Contact email.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the status page.
        :param pulumi.Input[str] description: Status page description.
        :param pulumi.Input[str] domain_name: Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        :param pulumi.Input[bool] hide_from_search_engines: Determines if the status page is hidden from search engines. Applicable on public status pages only.
        :param pulumi.Input[bool] is_public: Determines if the status page is public or not.
        :param pulumi.Input[str] name: Status page name.
        :param pulumi.Input[pulumi.InputType['PageOwnerArgs']] owner: Status page owner.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[pulumi.InputType['PageThemeColorArgs']] theme_color: Theme color for the status page.
        :param pulumi.Input[str] timezone: Timezone for the status page.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Status Pages](https://www.squadcast.com/blog/status-pages-101-everything-you-need-to-know-about-status-pages) serves as a communication instrument enabling you to notify your customers regarding service interruptions and scheduled maintenance. You can create a status page for each of your services and customize it to your liking. You can also add components & groups to your status page to show the status of your services.

        ## Example Usage

        ```python
        import pulumi
        import irisdanded_squadcast_pulumi as squadcast
        import pulumi_squadcast as squadcast

        team = squadcast.get_team(name="Default Team")
        user = squadcast.get_user(email="john@example.com")
        test_status_page = squadcast.status.Page("testStatusPage",
            team_id=team.id,
            description="Status Page description",
            is_public=True,
            domain_name="test-statuspage",
            timezone="Asia/Kolkata",
            contact_email="example@test.com",
            theme_color=squadcast.status.PageThemeColorArgs(
                primary="#000000",
                secondary="#dddddd",
            ),
            owner=squadcast.status.PageOwnerArgs(
                type="user",
                id=user.id,
            ),
            allow_webhook_subscription=True,
            allow_components_subscription=True,
            allow_maintenance_subscription=True)
        ```

        ## Import

        statusPageID

        ```sh
        $ pulumi import squadcast:Status/page:Page test_status_page 285
        ```

        :param str resource_name: The name of the resource.
        :param PageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_components_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_maintenance_subscription: Optional[pulumi.Input[bool]] = None,
                 allow_webhook_subscription: Optional[pulumi.Input[bool]] = None,
                 contact_email: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 hide_from_search_engines: Optional[pulumi.Input[bool]] = None,
                 is_public: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[pulumi.InputType['PageOwnerArgs']]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 theme_color: Optional[pulumi.Input[pulumi.InputType['PageThemeColorArgs']]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PageArgs.__new__(PageArgs)

            __props__.__dict__["allow_components_subscription"] = allow_components_subscription
            __props__.__dict__["allow_maintenance_subscription"] = allow_maintenance_subscription
            __props__.__dict__["allow_webhook_subscription"] = allow_webhook_subscription
            if contact_email is None and not opts.urn:
                raise TypeError("Missing required property 'contact_email'")
            __props__.__dict__["contact_email"] = contact_email
            __props__.__dict__["custom_domain_name"] = custom_domain_name
            __props__.__dict__["description"] = description
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["hide_from_search_engines"] = hide_from_search_engines
            if is_public is None and not opts.urn:
                raise TypeError("Missing required property 'is_public'")
            __props__.__dict__["is_public"] = is_public
            __props__.__dict__["name"] = name
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            if theme_color is None and not opts.urn:
                raise TypeError("Missing required property 'theme_color'")
            __props__.__dict__["theme_color"] = theme_color
            if timezone is None and not opts.urn:
                raise TypeError("Missing required property 'timezone'")
            __props__.__dict__["timezone"] = timezone
        super(Page, __self__).__init__(
            'squadcast:Status/page:Page',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_components_subscription: Optional[pulumi.Input[bool]] = None,
            allow_maintenance_subscription: Optional[pulumi.Input[bool]] = None,
            allow_webhook_subscription: Optional[pulumi.Input[bool]] = None,
            contact_email: Optional[pulumi.Input[str]] = None,
            custom_domain_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            hide_from_search_engines: Optional[pulumi.Input[bool]] = None,
            is_public: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[pulumi.InputType['PageOwnerArgs']]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            theme_color: Optional[pulumi.Input[pulumi.InputType['PageThemeColorArgs']]] = None,
            timezone: Optional[pulumi.Input[str]] = None) -> 'Page':
        """
        Get an existing Page resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_components_subscription: Determines if components subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_maintenance_subscription: Determines if maintenance subscription is allowed to the status page.
        :param pulumi.Input[bool] allow_webhook_subscription: Determines if webhook subscription is allowed to the status page.
        :param pulumi.Input[str] contact_email: Contact email.
        :param pulumi.Input[str] custom_domain_name: Custom domain name of the status page.
        :param pulumi.Input[str] description: Status page description.
        :param pulumi.Input[str] domain_name: Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        :param pulumi.Input[bool] hide_from_search_engines: Determines if the status page is hidden from search engines. Applicable on public status pages only.
        :param pulumi.Input[bool] is_public: Determines if the status page is public or not.
        :param pulumi.Input[str] name: Status page name.
        :param pulumi.Input[pulumi.InputType['PageOwnerArgs']] owner: Status page owner.
        :param pulumi.Input[str] team_id: Team id.
        :param pulumi.Input[pulumi.InputType['PageThemeColorArgs']] theme_color: Theme color for the status page.
        :param pulumi.Input[str] timezone: Timezone for the status page.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PageState.__new__(_PageState)

        __props__.__dict__["allow_components_subscription"] = allow_components_subscription
        __props__.__dict__["allow_maintenance_subscription"] = allow_maintenance_subscription
        __props__.__dict__["allow_webhook_subscription"] = allow_webhook_subscription
        __props__.__dict__["contact_email"] = contact_email
        __props__.__dict__["custom_domain_name"] = custom_domain_name
        __props__.__dict__["description"] = description
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["hide_from_search_engines"] = hide_from_search_engines
        __props__.__dict__["is_public"] = is_public
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["theme_color"] = theme_color
        __props__.__dict__["timezone"] = timezone
        return Page(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowComponentsSubscription")
    def allow_components_subscription(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if components subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_components_subscription")

    @property
    @pulumi.getter(name="allowMaintenanceSubscription")
    def allow_maintenance_subscription(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if maintenance subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_maintenance_subscription")

    @property
    @pulumi.getter(name="allowWebhookSubscription")
    def allow_webhook_subscription(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if webhook subscription is allowed to the status page.
        """
        return pulumi.get(self, "allow_webhook_subscription")

    @property
    @pulumi.getter(name="contactEmail")
    def contact_email(self) -> pulumi.Output[str]:
        """
        Contact email.
        """
        return pulumi.get(self, "contact_email")

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        Custom domain name of the status page.
        """
        return pulumi.get(self, "custom_domain_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Status page description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Domain name of the status page. This will be appended to https://statuspage.squadcast.com/\\n\\n/ to form the URL of the status page (can only be set during creation)
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="hideFromSearchEngines")
    def hide_from_search_engines(self) -> pulumi.Output[Optional[bool]]:
        """
        Determines if the status page is hidden from search engines. Applicable on public status pages only.
        """
        return pulumi.get(self, "hide_from_search_engines")

    @property
    @pulumi.getter(name="isPublic")
    def is_public(self) -> pulumi.Output[bool]:
        """
        Determines if the status page is public or not.
        """
        return pulumi.get(self, "is_public")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Status page name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output['outputs.PageOwner']:
        """
        Status page owner.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        Team id.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="themeColor")
    def theme_color(self) -> pulumi.Output['outputs.PageThemeColor']:
        """
        Theme color for the status page.
        """
        return pulumi.get(self, "theme_color")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[str]:
        """
        Timezone for the status page.
        """
        return pulumi.get(self, "timezone")

