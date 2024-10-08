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

    public sealed class WorkflowActionStatusAndMessageArgs : global::Pulumi.ResourceArgs
    {
        [Input("messages")]
        private InputList<string>? _messages;

        /// <summary>
        /// The messages to be set for the issue
        /// </summary>
        public InputList<string> Messages
        {
            get => _messages ?? (_messages = new InputList<string>());
            set => _messages = value;
        }

        /// <summary>
        /// The ID of the status
        /// </summary>
        [Input("statusId", required: true)]
        public Input<int> StatusId { get; set; } = null!;

        public WorkflowActionStatusAndMessageArgs()
        {
        }
        public static new WorkflowActionStatusAndMessageArgs Empty => new WorkflowActionStatusAndMessageArgs();
    }
}
