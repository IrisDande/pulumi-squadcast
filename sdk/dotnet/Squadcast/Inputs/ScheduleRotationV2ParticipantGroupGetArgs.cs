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

    public sealed class ScheduleRotationV2ParticipantGroupGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("participants")]
        private InputList<Inputs.ScheduleRotationV2ParticipantGroupParticipantGetArgs>? _participants;

        /// <summary>
        /// Group participants.
        /// </summary>
        public InputList<Inputs.ScheduleRotationV2ParticipantGroupParticipantGetArgs> Participants
        {
            get => _participants ?? (_participants = new InputList<Inputs.ScheduleRotationV2ParticipantGroupParticipantGetArgs>());
            set => _participants = value;
        }

        public ScheduleRotationV2ParticipantGroupGetArgs()
        {
        }
        public static new ScheduleRotationV2ParticipantGroupGetArgs Empty => new ScheduleRotationV2ParticipantGroupGetArgs();
    }
}
