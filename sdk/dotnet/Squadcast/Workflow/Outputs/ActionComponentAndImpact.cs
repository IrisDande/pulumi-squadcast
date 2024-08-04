// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Workflow.Outputs
{

    [OutputType]
    public sealed class ActionComponentAndImpact
    {
        /// <summary>
        /// The ID of the component
        /// </summary>
        public readonly int ComponentId;
        /// <summary>
        /// The ID of the impact status
        /// </summary>
        public readonly int ImpactStatusId;

        [OutputConstructor]
        private ActionComponentAndImpact(
            int componentId,

            int impactStatusId)
        {
            ComponentId = componentId;
            ImpactStatusId = impactStatusId;
        }
    }
}
