// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Inputs
{

    public sealed class WebformSeverityArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Severity description.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Severity type.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public WebformSeverityArgs()
        {
        }
        public static new WebformSeverityArgs Empty => new WebformSeverityArgs();
    }
}
