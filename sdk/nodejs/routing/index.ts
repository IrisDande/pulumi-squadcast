// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { RulesArgs, RulesState } from "./rules";
export type Rules = import("./rules").Rules;
export const Rules: typeof import("./rules").Rules = null as any;
utilities.lazyLoad(exports, ["Rules"], () => require("./rules"));


// Export sub-modules:
import * as rule from "./rule";

export {
    rule,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "squadcast:routing/rules:Rules":
                return new Rules(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("squadcast", "routing/rules", _module)
