// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Suppression.Outputs
{

    [OutputType]
    public sealed class RulesRuleTimeslot
    {
        /// <summary>
        /// Use this field to specify the custom time slots for which this rule should be applied. This field is only applicable when the repetition field is set to custom.
        /// </summary>
        public readonly ImmutableArray<Outputs.RulesRuleTimeslotCustom> Customs;
        /// <summary>
        /// Defines the end date of the time slot
        /// </summary>
        public readonly string EndTime;
        /// <summary>
        /// Defines whether the time slot ends or not
        /// </summary>
        public readonly bool? EndsNever;
        /// <summary>
        /// Defines the end date of the repetition
        /// </summary>
        public readonly string EndsOn;
        /// <summary>
        /// Defines if the time slot is an all day slot
        /// </summary>
        public readonly bool? IsAllday;
        /// <summary>
        /// Defines whether repetition is custom or not
        /// </summary>
        public readonly bool? IsCustom;
        /// <summary>
        /// Defines the repetition of the time slot
        /// </summary>
        public readonly string Repetition;
        /// <summary>
        /// Defines the start date of the time slot
        /// </summary>
        public readonly string StartTime;
        /// <summary>
        /// Time zone for the time slot
        /// </summary>
        public readonly string TimeZone;

        [OutputConstructor]
        private RulesRuleTimeslot(
            ImmutableArray<Outputs.RulesRuleTimeslotCustom> customs,

            string endTime,

            bool? endsNever,

            string endsOn,

            bool? isAllday,

            bool? isCustom,

            string repetition,

            string startTime,

            string timeZone)
        {
            Customs = customs;
            EndTime = endTime;
            EndsNever = endsNever;
            EndsOn = endsOn;
            IsAllday = isAllday;
            IsCustom = isCustom;
            Repetition = repetition;
            StartTime = startTime;
            TimeZone = timeZone;
        }
    }
}
