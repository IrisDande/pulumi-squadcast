// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Outputs
{

    [OutputType]
    public sealed class WorkflowTag
    {
        public readonly string Color;
        public readonly string Key;
        public readonly string Value;

        [OutputConstructor]
        private WorkflowTag(
            string color,

            string key,

            string value)
        {
            Color = color;
            Key = key;
            Value = value;
        }
    }
}
