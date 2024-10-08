// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * GER Ruleset Rules are a set of conditions defined within a Global Event Ruleset. These rules have expressions, whose evaluation will determine the destination service for the incoming events.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squadcast from "@irisdanded/pulumi-squadcast";
 * import * as squadcast from "@pulumi/squadcast";
 *
 * const exampleTeam = squadcast.getTeam({
 *     name: "Example Team",
 * });
 * const exampleUser = squadcast.getUser({
 *     email: "john@example.com",
 * });
 * const exampleService = exampleTeam.then(exampleTeam => squadcast.getService({
 *     name: "Example Service",
 *     teamId: exampleTeam.id,
 * }));
 * const exampleGer = new squadcast.Ger("exampleGer", {
 *     description: "Example GER Description",
 *     teamId: exampleTeam.then(exampleTeam => exampleTeam.id),
 *     entityOwner: {
 *         id: exampleUser.then(exampleUser => exampleUser.id),
 *         type: "user",
 *     },
 * });
 * const exampleGerRuleset = new squadcast.GerRuleset("exampleGerRuleset", {
 *     gerId: exampleGer.id,
 *     alertSource: "Prometheus",
 *     catchAllAction: {
 *         route_to: exampleService.then(exampleService => exampleService.id),
 *     },
 * });
 * const exampleGerRulesetRule = new squadcast.GerRulesetRule("exampleGerRulesetRule", {
 *     gerId: exampleGer.id,
 *     alertSource: exampleGerRuleset.alertSource,
 *     expression: "alertname == \"DeploymentReplicasNotUpdated\"",
 *     description: "Example GER Ruleset Rule",
 *     action: {
 *         route_to: exampleService.then(exampleService => exampleService.id),
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * gerID:alertSourceName:ruleID
 *
 * ```sh
 * $ pulumi import squadcast:index/gerRulesetRule:GerRulesetRule ger_ruleset_rule_import "50:Grafana:100"
 * ```
 */
export class GerRulesetRule extends pulumi.CustomResource {
    /**
     * Get an existing GerRulesetRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GerRulesetRuleState, opts?: pulumi.CustomResourceOptions): GerRulesetRule {
        return new GerRulesetRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'squadcast:index/gerRulesetRule:GerRulesetRule';

    /**
     * Returns true if the given object is an instance of GerRulesetRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GerRulesetRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GerRulesetRule.__pulumiType;
    }

    /**
     * Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
     */
    public readonly action!: pulumi.Output<{[key: string]: string}>;
    /**
     * An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
     */
    public readonly alertSource!: pulumi.Output<string>;
    /**
     * Shortname of the linked alert source.
     */
    public /*out*/ readonly alertSourceShortname!: pulumi.Output<string>;
    /**
     * Version of the linked alert source.
     */
    public /*out*/ readonly alertSourceVersion!: pulumi.Output<string>;
    /**
     * GER Ruleset Rule description.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
     */
    public readonly expression!: pulumi.Output<string>;
    /**
     * GER id.
     */
    public readonly gerId!: pulumi.Output<string>;

    /**
     * Create a GerRulesetRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GerRulesetRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GerRulesetRuleArgs | GerRulesetRuleState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GerRulesetRuleState | undefined;
            resourceInputs["action"] = state ? state.action : undefined;
            resourceInputs["alertSource"] = state ? state.alertSource : undefined;
            resourceInputs["alertSourceShortname"] = state ? state.alertSourceShortname : undefined;
            resourceInputs["alertSourceVersion"] = state ? state.alertSourceVersion : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["expression"] = state ? state.expression : undefined;
            resourceInputs["gerId"] = state ? state.gerId : undefined;
        } else {
            const args = argsOrState as GerRulesetRuleArgs | undefined;
            if ((!args || args.action === undefined) && !opts.urn) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.alertSource === undefined) && !opts.urn) {
                throw new Error("Missing required property 'alertSource'");
            }
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.expression === undefined) && !opts.urn) {
                throw new Error("Missing required property 'expression'");
            }
            if ((!args || args.gerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gerId'");
            }
            resourceInputs["action"] = args ? args.action : undefined;
            resourceInputs["alertSource"] = args ? args.alertSource : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["expression"] = args ? args.expression : undefined;
            resourceInputs["gerId"] = args ? args.gerId : undefined;
            resourceInputs["alertSourceShortname"] = undefined /*out*/;
            resourceInputs["alertSourceVersion"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GerRulesetRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GerRulesetRule resources.
 */
export interface GerRulesetRuleState {
    /**
     * Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
     */
    action?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
     */
    alertSource?: pulumi.Input<string>;
    /**
     * Shortname of the linked alert source.
     */
    alertSourceShortname?: pulumi.Input<string>;
    /**
     * Version of the linked alert source.
     */
    alertSourceVersion?: pulumi.Input<string>;
    /**
     * GER Ruleset Rule description.
     */
    description?: pulumi.Input<string>;
    /**
     * An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
     */
    expression?: pulumi.Input<string>;
    /**
     * GER id.
     */
    gerId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GerRulesetRule resource.
 */
export interface GerRulesetRuleArgs {
    /**
     * Rule Action refers to the designated destination service to which an event should be directed towards, whenever a rule expression is true.
     */
    action: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
     */
    alertSource: pulumi.Input<string>;
    /**
     * GER Ruleset Rule description.
     */
    description: pulumi.Input<string>;
    /**
     * An expression is a single condition or a set of conditions that must be met for the rule to take action, such as routing the incoming event to a specific service.
     */
    expression: pulumi.Input<string>;
    /**
     * GER id.
     */
    gerId: pulumi.Input<string>;
}
