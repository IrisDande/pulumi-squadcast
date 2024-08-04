// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Escalation.Outputs
{

    [OutputType]
    public sealed class PolicyRule
    {
        public readonly int DelayMinutes;
        /// <summary>
        /// Notification channels to notify the targets. (SMS, Phone, Email, Push)
        /// </summary>
        public readonly ImmutableArray<string> NotificationChannels;
        /// <summary>
        /// repeat this rule
        /// </summary>
        public readonly Outputs.PolicyRuleRepeat? Repeat;
        public readonly Outputs.PolicyRuleRoundRobin? RoundRobin;
        public readonly ImmutableArray<Outputs.PolicyRuleTarget> Targets;

        [OutputConstructor]
        private PolicyRule(
            int delayMinutes,

            ImmutableArray<string> notificationChannels,

            Outputs.PolicyRuleRepeat? repeat,

            Outputs.PolicyRuleRoundRobin? roundRobin,

            ImmutableArray<Outputs.PolicyRuleTarget> targets)
        {
            DelayMinutes = delayMinutes;
            NotificationChannels = notificationChannels;
            Repeat = repeat;
            RoundRobin = roundRobin;
            Targets = targets;
        }
    }
}
