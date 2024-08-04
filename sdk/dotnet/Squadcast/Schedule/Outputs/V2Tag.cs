// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Schedule.Outputs
{

    [OutputType]
    public sealed class V2Tag
    {
        /// <summary>
        /// Schedule tag color.
        /// </summary>
        public readonly string? Color;
        /// <summary>
        /// Schedule tag key.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// Schedule tag value.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private V2Tag(
            string? color,

            string key,

            string value)
        {
            Color = color;
            Key = key;
            Value = value;
        }
    }
}
