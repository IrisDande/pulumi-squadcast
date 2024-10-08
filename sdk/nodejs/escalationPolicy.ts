// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * [Escalation Policies](https://support.squadcast.com/docs/escalation-policies) defines rules indicating when and how alerts will escalate to various Users, Squads and (or) Schedules within your Organization. The name of the Escalation Policy must be unique within and across Teams.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squadcast from "@irisdanded/pulumi-squadcast";
 * import * as squadcast from "@pulumi/squadcast";
 *
 * const exampleTeam = squadcast.getTeam({
 *     name: "example team name",
 * });
 * const exampleUser = squadcast.getUser({
 *     email: "test@example.com",
 * });
 * const exampleSquad = exampleTeam.then(exampleTeam => squadcast.getSquad({
 *     name: "example squad name",
 *     teamId: exampleTeam.id,
 * }));
 * const exampleScheduleV2 = exampleTeam.then(exampleTeam => squadcast.getScheduleV2({
 *     name: "example schedule name",
 *     teamId: exampleTeam.id,
 * }));
 * const exampleEscalaionPolicy = new squadcast.EscalationPolicy("exampleEscalaionPolicy", {
 *     description: "It's an amazing policy",
 *     teamId: exampleTeam.then(exampleTeam => exampleTeam.id),
 *     rules: [
 *         {
 *             delayMinutes: 0,
 *             targets: [
 *                 {
 *                     id: exampleUser.then(exampleUser => exampleUser.id),
 *                     type: "user",
 *                 },
 *                 {
 *                     id: exampleScheduleV2.then(exampleScheduleV2 => exampleScheduleV2.id),
 *                     type: "schedulev2",
 *                 },
 *             ],
 *         },
 *         {
 *             delayMinutes: 5,
 *             targets: [
 *                 {
 *                     id: exampleUser.then(exampleUser => exampleUser.id),
 *                     type: "user",
 *                 },
 *                 {
 *                     id: exampleSquad.then(exampleSquad => exampleSquad.id),
 *                     type: "squad",
 *                 },
 *             ],
 *             notificationChannels: ["Phone"],
 *             repeat: {
 *                 times: 1,
 *                 delayMinutes: 5,
 *             },
 *         },
 *         {
 *             delayMinutes: 10,
 *             targets: [
 *                 {
 *                     id: exampleSquad.then(exampleSquad => exampleSquad.id),
 *                     type: "squad",
 *                 },
 *                 {
 *                     id: exampleScheduleV2.then(exampleScheduleV2 => exampleScheduleV2.id),
 *                     type: "schedulev2",
 *                 },
 *             ],
 *             roundRobin: {
 *                 enabled: true,
 *                 rotation: {
 *                     enabled: true,
 *                     delayMinutes: 1,
 *                 },
 *             },
 *         },
 *     ],
 *     repeat: {
 *         times: 2,
 *         delayMinutes: 10,
 *     },
 *     entityOwner: {
 *         id: exampleUser.then(exampleUser => exampleUser.id),
 *         type: "user",
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * teamID:escalationPolicyID
 *
 * Use 'Get All Teams' and 'Get All Escalation Policies' APIs to get the id of the team and escalation policy name respectively
 *
 * ```sh
 * $ pulumi import squadcast:index/escalationPolicy:EscalationPolicy test "62d2fe23a57381088224d726:Example Escalation Policy"
 * ```
 */
export class EscalationPolicy extends pulumi.CustomResource {
    /**
     * Get an existing EscalationPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EscalationPolicyState, opts?: pulumi.CustomResourceOptions): EscalationPolicy {
        return new EscalationPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'squadcast:index/escalationPolicy:EscalationPolicy';

    /**
     * Returns true if the given object is an instance of EscalationPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EscalationPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EscalationPolicy.__pulumiType;
    }

    /**
     * Detailed description about the Escalation Policy.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Escalation policy owner.
     */
    public readonly entityOwner!: pulumi.Output<outputs.EscalationPolicyEntityOwner>;
    /**
     * Name of the Escalation Policy.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * You can choose to repeate the entire policy, if no one acknowledges the incident even after the Escalation Policy has been executed fully once
     */
    public readonly repeat!: pulumi.Output<outputs.EscalationPolicyRepeat | undefined>;
    /**
     * Rules will have the details of who to notify and when to notify and how to notify them.
     */
    public readonly rules!: pulumi.Output<outputs.EscalationPolicyRule[]>;
    /**
     * Team id.
     */
    public readonly teamId!: pulumi.Output<string>;

    /**
     * Create a EscalationPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EscalationPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: EscalationPolicyArgs | EscalationPolicyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as EscalationPolicyState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["entityOwner"] = state ? state.entityOwner : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["repeat"] = state ? state.repeat : undefined;
            resourceInputs["rules"] = state ? state.rules : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
        } else {
            const args = argsOrState as EscalationPolicyArgs | undefined;
            if ((!args || args.entityOwner === undefined) && !opts.urn) {
                throw new Error("Missing required property 'entityOwner'");
            }
            if ((!args || args.rules === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rules'");
            }
            if ((!args || args.teamId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'teamId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["entityOwner"] = args ? args.entityOwner : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["repeat"] = args ? args.repeat : undefined;
            resourceInputs["rules"] = args ? args.rules : undefined;
            resourceInputs["teamId"] = args ? args.teamId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(EscalationPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering EscalationPolicy resources.
 */
export interface EscalationPolicyState {
    /**
     * Detailed description about the Escalation Policy.
     */
    description?: pulumi.Input<string>;
    /**
     * Escalation policy owner.
     */
    entityOwner?: pulumi.Input<inputs.EscalationPolicyEntityOwner>;
    /**
     * Name of the Escalation Policy.
     */
    name?: pulumi.Input<string>;
    /**
     * You can choose to repeate the entire policy, if no one acknowledges the incident even after the Escalation Policy has been executed fully once
     */
    repeat?: pulumi.Input<inputs.EscalationPolicyRepeat>;
    /**
     * Rules will have the details of who to notify and when to notify and how to notify them.
     */
    rules?: pulumi.Input<pulumi.Input<inputs.EscalationPolicyRule>[]>;
    /**
     * Team id.
     */
    teamId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a EscalationPolicy resource.
 */
export interface EscalationPolicyArgs {
    /**
     * Detailed description about the Escalation Policy.
     */
    description?: pulumi.Input<string>;
    /**
     * Escalation policy owner.
     */
    entityOwner: pulumi.Input<inputs.EscalationPolicyEntityOwner>;
    /**
     * Name of the Escalation Policy.
     */
    name?: pulumi.Input<string>;
    /**
     * You can choose to repeate the entire policy, if no one acknowledges the incident even after the Escalation Policy has been executed fully once
     */
    repeat?: pulumi.Input<inputs.EscalationPolicyRepeat>;
    /**
     * Rules will have the details of who to notify and when to notify and how to notify them.
     */
    rules: pulumi.Input<pulumi.Input<inputs.EscalationPolicyRule>[]>;
    /**
     * Team id.
     */
    teamId: pulumi.Input<string>;
}
