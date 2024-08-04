// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Suppression.Inputs
{

    public sealed class RulesRuleTimeslotCustomGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Determines how often the rule repeats. Valid values are day, week, month.
        /// </summary>
        [Input("repeats", required: true)]
        public Input<string> Repeats { get; set; } = null!;

        /// <summary>
        /// Number of times to repeat.
        /// </summary>
        [Input("repeatsCount")]
        public Input<int>? RepeatsCount { get; set; }

        /// <summary>
        /// Repeats on month.
        /// </summary>
        [Input("repeatsOnMonth")]
        public Input<string>? RepeatsOnMonth { get; set; }

        [Input("repeatsOnWeekdays")]
        private InputList<int>? _repeatsOnWeekdays;

        /// <summary>
        /// List of weekdays to repeat on.
        /// </summary>
        public InputList<int> RepeatsOnWeekdays
        {
            get => _repeatsOnWeekdays ?? (_repeatsOnWeekdays = new InputList<int>());
            set => _repeatsOnWeekdays = value;
        }

        public RulesRuleTimeslotCustomGetArgs()
        {
        }
        public static new RulesRuleTimeslotCustomGetArgs Empty => new RulesRuleTimeslotCustomGetArgs();
    }
}
