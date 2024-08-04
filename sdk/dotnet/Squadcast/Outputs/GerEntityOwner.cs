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
    public sealed class GerEntityOwner
    {
        /// <summary>
        /// GER owner id.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// GER owner type. Supported values are 'user' or 'squad'.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GerEntityOwner(
            string id,

            string type)
        {
            Id = id;
            Type = type;
        }
    }
}
