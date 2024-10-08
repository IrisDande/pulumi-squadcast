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

    public sealed class WebformInputFieldGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Input field Label.
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        [Input("options")]
        private InputList<string>? _options;

        /// <summary>
        /// Input field options.
        /// </summary>
        public InputList<string> Options
        {
            get => _options ?? (_options = new InputList<string>());
            set => _options = value;
        }

        public WebformInputFieldGetArgs()
        {
        }
        public static new WebformInputFieldGetArgs Empty => new WebformInputFieldGetArgs();
    }
}
