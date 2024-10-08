// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * [Tagging](https://support.squadcast.com/docs/event-tagging) is a rule-based, auto-tagging system with which you can define customised tags based on incident payloads, that get automatically assigned to incidents when they are triggered.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squadcast from "@irisdanded/pulumi-squadcast";
 * import * as squadcast from "@pulumi/squadcast";
 *
 * const exampleTeam = squadcast.getTeam({
 *     name: "example test name",
 * });
 * const exampleService = exampleTeam.then(exampleTeam => squadcast.getService({
 *     name: "example service name",
 *     teamId: exampleTeam.id,
 * }));
 * const exampleTaggingRules = new squadcast.tagging.Rules("exampleTaggingRules", {
 *     teamId: exampleTeam.then(exampleTeam => exampleTeam.id),
 *     serviceId: exampleService.then(exampleService => exampleService.id),
 *     rules: [
 *         {
 *             isBasic: false,
 *             expression: "payload[\"event_id\"] == 40",
 *             tags: [{
 *                 key: "MyTag",
 *                 value: "foo",
 *                 color: "#ababab",
 *             }],
 *         },
 *         {
 *             isBasic: true,
 *             basicExpressions: [{
 *                 lhs: "payload[\"foo\"]",
 *                 op: "is",
 *                 rhs: "bar",
 *             }],
 *             tags: [
 *                 {
 *                     key: "MyTag",
 *                     value: "foo",
 *                     color: "#ababab",
 *                 },
 *                 {
 *                     key: "MyTag2",
 *                     value: "bar",
 *                     color: "#f0f0f0",
 *                 },
 *             ],
 *         },
 *     ],
 * });
 * // addTags must be set in expression when tags are not passed
 * const exampleTaggingRulesResourceWithouttags = new squadcast.tagging.Rules("exampleTaggingRulesResourceWithouttags", {
 *     teamId: exampleTeam.then(exampleTeam => exampleTeam.id),
 *     serviceId: exampleService.then(exampleService => exampleService.id),
 *     rules: [{
 *         isBasic: false,
 *         expression: "addTag(\"EventType\", payload.details.event_type_key, \"#037916\")",
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * teamID:serviceID
 *
 * Use 'Get All Teams' and 'Get All Services' APIs to get the id of the team and service respectively
 *
 * ```sh
 * $ pulumi import squadcast:tagging/rules:Rules test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
 * ```
 */
export class Rules extends pulumi.CustomResource {
    /**
     * Get an existing Rules resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RulesState, opts?: pulumi.CustomResourceOptions): Rules {
        return new Rules(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'squadcast:tagging/rules:Rules';

    /**
     * Returns true if the given object is an instance of Rules.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rules {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rules.__pulumiType;
    }

    public readonly rules!: pulumi.Output<outputs.tagging.RulesRule[]>;
    /**
     * Service id.
     */
    public readonly serviceId!: pulumi.Output<string>;
    /**
     * Team id.
     */
    public readonly teamId!: pulumi.Output<string>;

    /**
     * Create a Rules resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RulesArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RulesArgs | RulesState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RulesState | undefined;
            resourceInputs["rules"] = state ? state.rules : undefined;
            resourceInputs["serviceId"] = state ? state.serviceId : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
        } else {
            const args = argsOrState as RulesArgs | undefined;
            if ((!args || args.rules === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rules'");
            }
            if ((!args || args.serviceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceId'");
            }
            if ((!args || args.teamId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'teamId'");
            }
            resourceInputs["rules"] = args ? args.rules : undefined;
            resourceInputs["serviceId"] = args ? args.serviceId : undefined;
            resourceInputs["teamId"] = args ? args.teamId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Rules.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Rules resources.
 */
export interface RulesState {
    rules?: pulumi.Input<pulumi.Input<inputs.tagging.RulesRule>[]>;
    /**
     * Service id.
     */
    serviceId?: pulumi.Input<string>;
    /**
     * Team id.
     */
    teamId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Rules resource.
 */
export interface RulesArgs {
    rules: pulumi.Input<pulumi.Input<inputs.tagging.RulesRule>[]>;
    /**
     * Service id.
     */
    serviceId: pulumi.Input<string>;
    /**
     * Team id.
     */
    teamId: pulumi.Input<string>;
}
