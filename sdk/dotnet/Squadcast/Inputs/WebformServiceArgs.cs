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

    public sealed class WebformServiceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Service alias.
        /// </summary>
        [Input("alias")]
        public Input<string>? Alias { get; set; }

        /// <summary>
        /// Service name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Service ID.
        /// </summary>
        [Input("serviceId", required: true)]
        public Input<string> ServiceId { get; set; } = null!;

        public WebformServiceArgs()
        {
        }
        public static new WebformServiceArgs Empty => new WebformServiceArgs();
    }
}
