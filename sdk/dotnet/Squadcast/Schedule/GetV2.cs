// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace IrisDanded.Pulumi.Squadcast.Schedule
{
    public static class GetV2
    {
        /// <summary>
        /// [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling &amp; determine who will be notified when an incident is triggered. Use this data source to get information about a specific schedule that you can use for other Squadcast resources.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Squadcast = Pulumi.Squadcast;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = Squadcast.Schedule.GetV2.Invoke(new()
        ///     {
        ///         Name = squadcast_schedule_v2.Test.Name,
        ///         TeamId = "team_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetV2Result> InvokeAsync(GetV2Args args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetV2Result>("squadcast:Schedule/getV2:getV2", args ?? new GetV2Args(), options.WithDefaults());

        /// <summary>
        /// [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling &amp; determine who will be notified when an incident is triggered. Use this data source to get information about a specific schedule that you can use for other Squadcast resources.
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Squadcast = Pulumi.Squadcast;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = Squadcast.Schedule.GetV2.Invoke(new()
        ///     {
        ///         Name = squadcast_schedule_v2.Test.Name,
        ///         TeamId = "team_id",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetV2Result> Invoke(GetV2InvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetV2Result>("squadcast:Schedule/getV2:getV2", args ?? new GetV2InvokeArgs(), options.WithDefaults());
    }


    public sealed class GetV2Args : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the Schedule.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// Team id.
        /// </summary>
        [Input("teamId", required: true)]
        public string TeamId { get; set; } = null!;

        public GetV2Args()
        {
        }
        public static new GetV2Args Empty => new GetV2Args();
    }

    public sealed class GetV2InvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the Schedule.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Team id.
        /// </summary>
        [Input("teamId", required: true)]
        public Input<string> TeamId { get; set; } = null!;

        public GetV2InvokeArgs()
        {
        }
        public static new GetV2InvokeArgs Empty => new GetV2InvokeArgs();
    }


    [OutputType]
    public sealed class GetV2Result
    {
        /// <summary>
        /// Detailed description about the schedule.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// Schedule owner.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetV2EntityOwnerResult> EntityOwners;
        /// <summary>
        /// Schedule id.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Name of the Schedule.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Schedule tags.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetV2TagResult> Tags;
        /// <summary>
        /// Team id.
        /// </summary>
        public readonly string TeamId;
        /// <summary>
        /// Timezone for the schedule.
        /// </summary>
        public readonly string Timezone;

        [OutputConstructor]
        private GetV2Result(
            string description,

            ImmutableArray<Outputs.GetV2EntityOwnerResult> entityOwners,

            string id,

            string name,

            ImmutableArray<Outputs.GetV2TagResult> tags,

            string teamId,

            string timezone)
        {
            Description = description;
            EntityOwners = entityOwners;
            Id = id;
            Name = name;
            Tags = tags;
            TeamId = teamId;
            Timezone = timezone;
        }
    }
}
