// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Tagging
{
    /// <summary>
    /// [Tagging](https://support.squadcast.com/docs/event-tagging) is a rule-based, auto-tagging system with which you can define customised tags based on incident payloads, that get automatically assigned to incidents when they are triggered.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Squadcast = IrisDanded.Pulumi.Squadcast;
    /// using Squadcast = Pulumi.Squadcast;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleTeam = Squadcast.GetTeam.Invoke(new()
    ///     {
    ///         Name = "example test name",
    ///     });
    /// 
    ///     var exampleService = Squadcast.GetService.Invoke(new()
    ///     {
    ///         Name = "example service name",
    ///         TeamId = exampleTeam.Apply(getTeamResult =&gt; getTeamResult.Id),
    ///     });
    /// 
    ///     var exampleTaggingRules = new Squadcast.Tagging.Rules("exampleTaggingRules", new()
    ///     {
    ///         TeamId = exampleTeam.Apply(getTeamResult =&gt; getTeamResult.Id),
    ///         ServiceId = exampleService.Apply(getServiceResult =&gt; getServiceResult.Id),
    ///         TaggingRules = new[]
    ///         {
    ///             new Squadcast.Tagging.Inputs.RulesRuleArgs
    ///             {
    ///                 IsBasic = false,
    ///                 Expression = "payload[\"event_id\"] == 40",
    ///                 Tags = new[]
    ///                 {
    ///                     new Squadcast.Tagging.Inputs.RulesRuleTagArgs
    ///                     {
    ///                         Key = "MyTag",
    ///                         Value = "foo",
    ///                         Color = "#ababab",
    ///                     },
    ///                 },
    ///             },
    ///             new Squadcast.Tagging.Inputs.RulesRuleArgs
    ///             {
    ///                 IsBasic = true,
    ///                 BasicExpressions = new[]
    ///                 {
    ///                     new Squadcast.Tagging.Inputs.RulesRuleBasicExpressionArgs
    ///                     {
    ///                         Lhs = "payload[\"foo\"]",
    ///                         Op = "is",
    ///                         Rhs = "bar",
    ///                     },
    ///                 },
    ///                 Tags = new[]
    ///                 {
    ///                     new Squadcast.Tagging.Inputs.RulesRuleTagArgs
    ///                     {
    ///                         Key = "MyTag",
    ///                         Value = "foo",
    ///                         Color = "#ababab",
    ///                     },
    ///                     new Squadcast.Tagging.Inputs.RulesRuleTagArgs
    ///                     {
    ///                         Key = "MyTag2",
    ///                         Value = "bar",
    ///                         Color = "#f0f0f0",
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    ///     // addTags must be set in expression when tags are not passed
    ///     var exampleTaggingRulesResourceWithouttags = new Squadcast.Tagging.Rules("exampleTaggingRulesResourceWithouttags", new()
    ///     {
    ///         TeamId = exampleTeam.Apply(getTeamResult =&gt; getTeamResult.Id),
    ///         ServiceId = exampleService.Apply(getServiceResult =&gt; getServiceResult.Id),
    ///         TaggingRules = new[]
    ///         {
    ///             new Squadcast.Tagging.Inputs.RulesRuleArgs
    ///             {
    ///                 IsBasic = false,
    ///                 Expression = "addTag(\"EventType\", payload.details.event_type_key, \"#037916\")",
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// teamID:serviceID
    /// 
    /// Use 'Get All Teams' and 'Get All Services' APIs to get the id of the team and service respectively
    /// 
    /// ```sh
    /// $ pulumi import squadcast:tagging/rules:Rules test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
    /// ```
    /// </summary>
    [SquadcastResourceType("squadcast:tagging/rules:Rules")]
    public partial class Rules : global::Pulumi.CustomResource
    {
        [Output("rules")]
        public Output<ImmutableArray<Outputs.RulesRule>> TaggingRules { get; private set; } = null!;

        /// <summary>
        /// Service id.
        /// </summary>
        [Output("serviceId")]
        public Output<string> ServiceId { get; private set; } = null!;

        /// <summary>
        /// Team id.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;


        /// <summary>
        /// Create a Rules resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Rules(string name, RulesArgs args, CustomResourceOptions? options = null)
            : base("squadcast:tagging/rules:Rules", name, args ?? new RulesArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Rules(string name, Input<string> id, RulesState? state = null, CustomResourceOptions? options = null)
            : base("squadcast:tagging/rules:Rules", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/IrisDande/pulumi-squadcast",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Rules resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Rules Get(string name, Input<string> id, RulesState? state = null, CustomResourceOptions? options = null)
        {
            return new Rules(name, id, state, options);
        }
    }

    public sealed class RulesArgs : global::Pulumi.ResourceArgs
    {
        [Input("rules", required: true)]
        private InputList<Inputs.RulesRuleArgs>? _rules;
        public InputList<Inputs.RulesRuleArgs> TaggingRules
        {
            get => _rules ?? (_rules = new InputList<Inputs.RulesRuleArgs>());
            set => _rules = value;
        }

        /// <summary>
        /// Service id.
        /// </summary>
        [Input("serviceId", required: true)]
        public Input<string> ServiceId { get; set; } = null!;

        /// <summary>
        /// Team id.
        /// </summary>
        [Input("teamId", required: true)]
        public Input<string> TeamId { get; set; } = null!;

        public RulesArgs()
        {
        }
        public static new RulesArgs Empty => new RulesArgs();
    }

    public sealed class RulesState : global::Pulumi.ResourceArgs
    {
        [Input("rules")]
        private InputList<Inputs.RulesRuleGetArgs>? _rules;
        public InputList<Inputs.RulesRuleGetArgs> TaggingRules
        {
            get => _rules ?? (_rules = new InputList<Inputs.RulesRuleGetArgs>());
            set => _rules = value;
        }

        /// <summary>
        /// Service id.
        /// </summary>
        [Input("serviceId")]
        public Input<string>? ServiceId { get; set; }

        /// <summary>
        /// Team id.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public RulesState()
        {
        }
        public static new RulesState Empty => new RulesState();
    }
}
