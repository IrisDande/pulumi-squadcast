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
    public sealed class GetWebformOwnerResult
    {
        /// <summary>
        /// Form owner id.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Form owner name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Form owner type (user, team, squad).
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetWebformOwnerResult(
            string id,

            string name,

            string type)
        {
            Id = id;
            Name = name;
            Type = type;
        }
    }
}
