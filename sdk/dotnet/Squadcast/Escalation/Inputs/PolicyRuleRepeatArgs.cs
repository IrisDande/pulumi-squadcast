// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Escalation.Inputs
{

    public sealed class PolicyRuleRepeatArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// repeat after minutes
        /// </summary>
        [Input("delayMinutes", required: true)]
        public Input<int> DelayMinutes { get; set; } = null!;

        /// <summary>
        /// repeat times
        /// </summary>
        [Input("times", required: true)]
        public Input<int> Times { get; set; } = null!;

        public PolicyRuleRepeatArgs()
        {
        }
        public static new PolicyRuleRepeatArgs Empty => new PolicyRuleRepeatArgs();
    }
}
