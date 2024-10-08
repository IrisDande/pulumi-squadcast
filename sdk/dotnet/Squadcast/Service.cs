// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast
{
    /// <summary>
    /// [Squadcast Services](https://support.squadcast.com/docs/adding-a-service-1) are the core components of your infrastructure/application for which alerts are generated. Services in Squadcast represent specific systems, applications, components, products, or teams for which an incident is created. To check out some of the best practices on creating Services in Squadcast, refer to the guide [here](https://www.squadcast.com/blog/how-to-configure-services-in-squadcast-best-practices-to-reduce-mttr). The name of the Service must be unique within and across Teams.
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
    ///     var exampleUser = Squadcast.GetUser.Invoke(new()
    ///     {
    ///         Email = "test@example.com",
    ///     });
    /// 
    ///     var exampleTeam = Squadcast.GetTeam.Invoke(new()
    ///     {
    ///         Name = "example team name",
    ///     });
    /// 
    ///     var exampleEscalaionPolicy = Squadcast.GetEscalationPolicy.Invoke(new()
    ///     {
    ///         Name = "example escalation policy name",
    ///         TeamId = exampleTeam.Apply(getTeamResult =&gt; getTeamResult.Id),
    ///     });
    /// 
    ///     var exampleService = new Squadcast.Service("exampleService", new()
    ///     {
    ///         TeamId = exampleTeam.Apply(getTeamResult =&gt; getTeamResult.Id),
    ///         EscalationPolicyId = exampleEscalaionPolicy.Apply(getEscalationPolicyResult =&gt; getEscalationPolicyResult.Id),
    ///         EmailPrefix = "example-service-email",
    ///         Maintainer = new Squadcast.Inputs.ServiceMaintainerArgs
    ///         {
    ///             Id = exampleUser.Apply(getUserResult =&gt; getUserResult.Id),
    ///             Type = "user",
    ///         },
    ///         Tags = new[]
    ///         {
    ///             new Squadcast.Inputs.ServiceTagArgs
    ///             {
    ///                 Key = "testkey",
    ///                 Value = "testval",
    ///             },
    ///             new Squadcast.Inputs.ServiceTagArgs
    ///             {
    ///                 Key = "testkey2",
    ///                 Value = "testval2",
    ///             },
    ///         },
    ///         AlertSources = new[]
    ///         {
    ///             "example-alert-source",
    ///         },
    ///         SlackChannelId = "D0KAQDEPSH",
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
    /// $ pulumi import squadcast:index/service:Service test_parent 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
    /// ```
    /// </summary>
    [SquadcastResourceType("squadcast:index/service:Service")]
    public partial class Service : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Active alert source endpoints.
        /// </summary>
        [Output("activeAlertSourceEndpoints")]
        public Output<ImmutableDictionary<string, string>> ActiveAlertSourceEndpoints { get; private set; } = null!;

        /// <summary>
        /// All available alert source endpoints.
        /// </summary>
        [Output("alertSourceEndpoints")]
        public Output<ImmutableDictionary<string, string>> AlertSourceEndpoints { get; private set; } = null!;

        /// <summary>
        /// List of active alert source names. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        /// </summary>
        [Output("alertSources")]
        public Output<ImmutableArray<string>> AlertSources { get; private set; } = null!;

        /// <summary>
        /// Unique API key of this service.
        /// </summary>
        [Output("apiKey")]
        public Output<string> ApiKey { get; private set; } = null!;

        /// <summary>
        /// Dependencies (serviceIds)
        /// </summary>
        [Output("dependencies")]
        public Output<ImmutableArray<string>> Dependencies { get; private set; } = null!;

        /// <summary>
        /// Detailed description about this service.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Email.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Email prefix.
        /// </summary>
        [Output("emailPrefix")]
        public Output<string> EmailPrefix { get; private set; } = null!;

        /// <summary>
        /// Escalation policy id.
        /// </summary>
        [Output("escalationPolicyId")]
        public Output<string> EscalationPolicyId { get; private set; } = null!;

        /// <summary>
        /// Service owner.
        /// </summary>
        [Output("maintainer")]
        public Output<Outputs.ServiceMaintainer> Maintainer { get; private set; } = null!;

        /// <summary>
        /// Name of the Service.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Slack extension for the service. If set, specifies the ID of the Slack channel associated with the service. If this ID is set, it cannot be removed, but it can be changed to a different slack*channel*id.
        /// </summary>
        [Output("slackChannelId")]
        public Output<string> SlackChannelId { get; private set; } = null!;

        /// <summary>
        /// Service tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ServiceTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// Team id.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;


        /// <summary>
        /// Create a Service resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Service(string name, ServiceArgs args, CustomResourceOptions? options = null)
            : base("squadcast:index/service:Service", name, args ?? new ServiceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Service(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
            : base("squadcast:index/service:Service", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Service resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Service Get(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
        {
            return new Service(name, id, state, options);
        }
    }

    public sealed class ServiceArgs : global::Pulumi.ResourceArgs
    {
        [Input("alertSources")]
        private InputList<string>? _alertSources;

        /// <summary>
        /// List of active alert source names. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        /// </summary>
        public InputList<string> AlertSources
        {
            get => _alertSources ?? (_alertSources = new InputList<string>());
            set => _alertSources = value;
        }

        [Input("dependencies")]
        private InputList<string>? _dependencies;

        /// <summary>
        /// Dependencies (serviceIds)
        /// </summary>
        public InputList<string> Dependencies
        {
            get => _dependencies ?? (_dependencies = new InputList<string>());
            set => _dependencies = value;
        }

        /// <summary>
        /// Detailed description about this service.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Email prefix.
        /// </summary>
        [Input("emailPrefix", required: true)]
        public Input<string> EmailPrefix { get; set; } = null!;

        /// <summary>
        /// Escalation policy id.
        /// </summary>
        [Input("escalationPolicyId", required: true)]
        public Input<string> EscalationPolicyId { get; set; } = null!;

        /// <summary>
        /// Service owner.
        /// </summary>
        [Input("maintainer", required: true)]
        public Input<Inputs.ServiceMaintainerArgs> Maintainer { get; set; } = null!;

        /// <summary>
        /// Name of the Service.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Slack extension for the service. If set, specifies the ID of the Slack channel associated with the service. If this ID is set, it cannot be removed, but it can be changed to a different slack*channel*id.
        /// </summary>
        [Input("slackChannelId")]
        public Input<string>? SlackChannelId { get; set; }

        [Input("tags")]
        private InputList<Inputs.ServiceTagArgs>? _tags;

        /// <summary>
        /// Service tags.
        /// </summary>
        public InputList<Inputs.ServiceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ServiceTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// Team id.
        /// </summary>
        [Input("teamId", required: true)]
        public Input<string> TeamId { get; set; } = null!;

        public ServiceArgs()
        {
        }
        public static new ServiceArgs Empty => new ServiceArgs();
    }

    public sealed class ServiceState : global::Pulumi.ResourceArgs
    {
        [Input("activeAlertSourceEndpoints")]
        private InputMap<string>? _activeAlertSourceEndpoints;

        /// <summary>
        /// Active alert source endpoints.
        /// </summary>
        public InputMap<string> ActiveAlertSourceEndpoints
        {
            get => _activeAlertSourceEndpoints ?? (_activeAlertSourceEndpoints = new InputMap<string>());
            set => _activeAlertSourceEndpoints = value;
        }

        [Input("alertSourceEndpoints")]
        private InputMap<string>? _alertSourceEndpoints;

        /// <summary>
        /// All available alert source endpoints.
        /// </summary>
        public InputMap<string> AlertSourceEndpoints
        {
            get => _alertSourceEndpoints ?? (_alertSourceEndpoints = new InputMap<string>());
            set => _alertSourceEndpoints = value;
        }

        [Input("alertSources")]
        private InputList<string>? _alertSources;

        /// <summary>
        /// List of active alert source names. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
        /// </summary>
        public InputList<string> AlertSources
        {
            get => _alertSources ?? (_alertSources = new InputList<string>());
            set => _alertSources = value;
        }

        /// <summary>
        /// Unique API key of this service.
        /// </summary>
        [Input("apiKey")]
        public Input<string>? ApiKey { get; set; }

        [Input("dependencies")]
        private InputList<string>? _dependencies;

        /// <summary>
        /// Dependencies (serviceIds)
        /// </summary>
        public InputList<string> Dependencies
        {
            get => _dependencies ?? (_dependencies = new InputList<string>());
            set => _dependencies = value;
        }

        /// <summary>
        /// Detailed description about this service.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Email.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Email prefix.
        /// </summary>
        [Input("emailPrefix")]
        public Input<string>? EmailPrefix { get; set; }

        /// <summary>
        /// Escalation policy id.
        /// </summary>
        [Input("escalationPolicyId")]
        public Input<string>? EscalationPolicyId { get; set; }

        /// <summary>
        /// Service owner.
        /// </summary>
        [Input("maintainer")]
        public Input<Inputs.ServiceMaintainerGetArgs>? Maintainer { get; set; }

        /// <summary>
        /// Name of the Service.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Slack extension for the service. If set, specifies the ID of the Slack channel associated with the service. If this ID is set, it cannot be removed, but it can be changed to a different slack*channel*id.
        /// </summary>
        [Input("slackChannelId")]
        public Input<string>? SlackChannelId { get; set; }

        [Input("tags")]
        private InputList<Inputs.ServiceTagGetArgs>? _tags;

        /// <summary>
        /// Service tags.
        /// </summary>
        public InputList<Inputs.ServiceTagGetArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ServiceTagGetArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// Team id.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public ServiceState()
        {
        }
        public static new ServiceState Empty => new ServiceState();
    }
}
