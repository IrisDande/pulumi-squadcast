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
    public sealed class ScheduleRotationV2ParticipantGroup
    {
        /// <summary>
        /// Group participants.
        /// </summary>
        public readonly ImmutableArray<Outputs.ScheduleRotationV2ParticipantGroupParticipant> Participants;

        [OutputConstructor]
        private ScheduleRotationV2ParticipantGroup(ImmutableArray<Outputs.ScheduleRotationV2ParticipantGroupParticipant> participants)
        {
            Participants = participants;
        }
    }
}
