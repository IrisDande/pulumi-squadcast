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
    public sealed class SloNotify
    {
        /// <summary>
        /// The ID of the notification rule
        /// </summary>
        public readonly int? Id;
        /// <summary>
        /// The ID of the service in which the user want to create an incident
        /// </summary>
        public readonly string? ServiceId;
        /// <summary>
        /// The ID of the SLO.
        /// </summary>
        public readonly int? SloId;
        /// <summary>
        /// List of Squad ID's who should be alerted via email.
        /// </summary>
        public readonly ImmutableArray<string> SquadIds;
        /// <summary>
        /// List of user ID's who should be alerted via email.
        /// </summary>
        public readonly ImmutableArray<string> UserIds;

        [OutputConstructor]
        private SloNotify(
            int? id,

            string? serviceId,

            int? sloId,

            ImmutableArray<string> squadIds,

            ImmutableArray<string> userIds)
        {
            Id = id;
            ServiceId = serviceId;
            SloId = sloId;
            SquadIds = squadIds;
            UserIds = userIds;
        }
    }
}
