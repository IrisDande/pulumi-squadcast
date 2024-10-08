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
    public sealed class GetWebformServiceResult
    {
        /// <summary>
        /// Service alias.
        /// </summary>
        public readonly string Alias;
        /// <summary>
        /// Service name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Service ID.
        /// </summary>
        public readonly string ServiceId;

        [OutputConstructor]
        private GetWebformServiceResult(
            string alias,

            string name,

            string serviceId)
        {
            Alias = alias;
            Name = name;
            ServiceId = serviceId;
        }
    }
}
