// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * User resource.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squadcast from "@irisdanded/pulumi-squadcast";
 *
 * const exampleUser = new squadcast.User("exampleUser", {
 *     abilities: ["manage-billing"],
 *     email: "test@example.com",
 *     firstName: "test",
 *     lastName: "lastname",
 *     role: "stakeholder",
 * });
 * ```
 *
 * ## Import
 *
 * emailID
 *
 * ```sh
 * $ pulumi import squadcast:index/user:User example_resource_name test@example.com
 * ```
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'squadcast:index/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
     */
    public readonly abilities!: pulumi.Output<string[] | undefined>;
    /**
     * User email.
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * User first name.
     */
    public readonly firstName!: pulumi.Output<string>;
    /**
     * User last name.
     */
    public readonly lastName!: pulumi.Output<string>;
    /**
     * User role.
     */
    public readonly role!: pulumi.Output<string>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserState | undefined;
            resourceInputs["abilities"] = state ? state.abilities : undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["firstName"] = state ? state.firstName : undefined;
            resourceInputs["lastName"] = state ? state.lastName : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.firstName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'firstName'");
            }
            if ((!args || args.lastName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'lastName'");
            }
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            resourceInputs["abilities"] = args ? args.abilities : undefined;
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["firstName"] = args ? args.firstName : undefined;
            resourceInputs["lastName"] = args ? args.lastName : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(User.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
     */
    abilities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * User email.
     */
    email?: pulumi.Input<string>;
    /**
     * User first name.
     */
    firstName?: pulumi.Input<string>;
    /**
     * User last name.
     */
    lastName?: pulumi.Input<string>;
    /**
     * User role.
     */
    role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
     */
    abilities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * User email.
     */
    email: pulumi.Input<string>;
    /**
     * User first name.
     */
    firstName: pulumi.Input<string>;
    /**
     * User last name.
     */
    lastName: pulumi.Input<string>;
    /**
     * User role.
     */
    role: pulumi.Input<string>;
}
