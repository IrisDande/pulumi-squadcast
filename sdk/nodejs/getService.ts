// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * [Squadcast Services](https://support.squadcast.com/docs/adding-a-service-1) are the core components of your infrastructure/application for which alerts are generated. Services in Squadcast represent specific systems, applications, components, products, or teams for which an incident is created. To check out some of the best practices on creating Services in Squadcast, refer to the guide [here](https://www.squadcast.com/blog/how-to-configure-services-in-squadcast-best-practices-to-reduce-mttr).Use this data source to get information about a specific service.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squadcast from "@pulumi/squadcast";
 *
 * const test = squadcast.getService({
 *     name: squadcast_service.test.name,
 *     teamId: "team id",
 * });
 * ```
 */
export function getService(args: GetServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("squadcast:index/getService:getService", {
        "name": args.name,
        "teamId": args.teamId,
    }, opts);
}

/**
 * A collection of arguments for invoking getService.
 */
export interface GetServiceArgs {
    /**
     * Name of the Service.
     */
    name: string;
    /**
     * Team id.
     */
    teamId: string;
}

/**
 * A collection of values returned by getService.
 */
export interface GetServiceResult {
    /**
     * Active alert source endpoints.
     */
    readonly activeAlertSourceEndpoints: {[key: string]: string};
    /**
     * All available alert source endpoints.
     */
    readonly alertSourceEndpoints: {[key: string]: string};
    /**
     * Unique API key of the service
     */
    readonly apiKey: string;
    /**
     * dependencies.
     */
    readonly dependencies: string[];
    /**
     * Detailed description about the service.
     */
    readonly description: string;
    /**
     * Email.
     */
    readonly email: string;
    /**
     * Email prefix.
     */
    readonly emailPrefix: string;
    /**
     * Escalation policy id.
     */
    readonly escalationPolicyId: string;
    /**
     * Service id.
     */
    readonly id: string;
    /**
     * Service owner
     */
    readonly maintainers: outputs.GetServiceMaintainer[];
    /**
     * Name of the Service.
     */
    readonly name: string;
    /**
     * Slack extension for the service. If set, specifies the ID of the Slack channel associated with the service. If this ID is set, it cannot be removed, but it can be changed to a different slack*channel*id.
     */
    readonly slackChannelId: string;
    /**
     * Service tags
     */
    readonly tags: outputs.GetServiceTag[];
    /**
     * Team id.
     */
    readonly teamId: string;
}
/**
 * [Squadcast Services](https://support.squadcast.com/docs/adding-a-service-1) are the core components of your infrastructure/application for which alerts are generated. Services in Squadcast represent specific systems, applications, components, products, or teams for which an incident is created. To check out some of the best practices on creating Services in Squadcast, refer to the guide [here](https://www.squadcast.com/blog/how-to-configure-services-in-squadcast-best-practices-to-reduce-mttr).Use this data source to get information about a specific service.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squadcast from "@pulumi/squadcast";
 *
 * const test = squadcast.getService({
 *     name: squadcast_service.test.name,
 *     teamId: "team id",
 * });
 * ```
 */
export function getServiceOutput(args: GetServiceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceResult> {
    return pulumi.output(args).apply((a: any) => getService(a, opts))
}

/**
 * A collection of arguments for invoking getService.
 */
export interface GetServiceOutputArgs {
    /**
     * Name of the Service.
     */
    name: pulumi.Input<string>;
    /**
     * Team id.
     */
    teamId: pulumi.Input<string>;
}
