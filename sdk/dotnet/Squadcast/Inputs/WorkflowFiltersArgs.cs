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

    public sealed class WorkflowFiltersArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Condition to be applied on the filters (and / or)
        /// </summary>
        [Input("condition", required: true)]
        public Input<string> Condition { get; set; } = null!;

        [Input("filters")]
        private InputList<Inputs.WorkflowFiltersFilterArgs>? _filters;
        public InputList<Inputs.WorkflowFiltersFilterArgs> Filters
        {
            get => _filters ?? (_filters = new InputList<Inputs.WorkflowFiltersFilterArgs>());
            set => _filters = value;
        }

        public WorkflowFiltersArgs()
        {
        }
        public static new WorkflowFiltersArgs Empty => new WorkflowFiltersArgs();
    }
}
