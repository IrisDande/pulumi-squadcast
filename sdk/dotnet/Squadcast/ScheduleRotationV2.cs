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
    /// [Schedule rotations](https://support.squadcast.com/schedules/schedules-new/adding-a-schedule#2.-choose-a-rotation-pattern) are used to manage on-call scheduling &amp; determine who will be notified when an incident is triggered. The name of the Rotation must be unique within a Schedule.
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
    ///         Name = "example team name",
    ///     });
    /// 
    ///     var exampleUser = Squadcast.GetUser.Invoke(new()
    ///     {
    ///         Email = "test@example.com",
    ///     });
    /// 
    ///     var exampleUser2 = Squadcast.GetUser.Invoke(new()
    ///     {
    ///         Email = "test2@example.com",
    ///     });
    /// 
    ///     var getSchedule = Squadcast.GetScheduleV2.Invoke(new()
    ///     {
    ///         Name = "Test Schedule",
    ///         TeamId = exampleTeam.Apply(getTeamResult =&gt; getTeamResult.Id),
    ///     });
    /// 
    ///     // Create a rotation with weekly period
    ///     var rotationsWithWeeklyPeriod = new Squadcast.ScheduleRotationV2("rotationsWithWeeklyPeriod", new()
    ///     {
    ///         ScheduleId = getSchedule.Apply(getScheduleV2Result =&gt; getScheduleV2Result.Id),
    ///         StartDate = "2023-07-01T00:00:00Z",
    ///         Period = "weekly",
    ///         ShiftTimeslots = new[]
    ///         {
    ///             new Squadcast.Inputs.ScheduleRotationV2ShiftTimeslotArgs
    ///             {
    ///                 StartHour = 10,
    ///                 StartMinute = 30,
    ///                 Duration = 720,
    ///             },
    ///         },
    ///         ChangeParticipantsFrequency = 1,
    ///         ChangeParticipantsUnit = "rotation",
    ///         ParticipantGroups = new[]
    ///         {
    ///             new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupArgs
    ///             {
    ///                 Participants = new[]
    ///                 {
    ///                     new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupParticipantArgs
    ///                     {
    ///                         Id = exampleUser.Apply(getUserResult =&gt; getUserResult.Id),
    ///                         Type = "user",
    ///                     },
    ///                     new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupParticipantArgs
    ///                     {
    ///                         Id = exampleUser2.Apply(getUserResult =&gt; getUserResult.Id),
    ///                         Type = "user",
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///         EndsAfterIterations = 2,
    ///     });
    /// 
    ///     // Create a rotation with custom period
    ///     var rotationsWithCustomPeriod = new Squadcast.ScheduleRotationV2("rotationsWithCustomPeriod", new()
    ///     {
    ///         ScheduleId = getSchedule.Apply(getScheduleV2Result =&gt; getScheduleV2Result.Id),
    ///         StartDate = "2023-06-13T00:00:00Z",
    ///         Period = "custom",
    ///         ShiftTimeslots = new[]
    ///         {
    ///             new Squadcast.Inputs.ScheduleRotationV2ShiftTimeslotArgs
    ///             {
    ///                 StartHour = 10,
    ///                 StartMinute = 0,
    ///                 Duration = 1440,
    ///                 DayOfWeek = "saturday",
    ///             },
    ///             new Squadcast.Inputs.ScheduleRotationV2ShiftTimeslotArgs
    ///             {
    ///                 StartHour = 12,
    ///                 StartMinute = 30,
    ///                 Duration = 720,
    ///                 DayOfWeek = "sunday",
    ///             },
    ///         },
    ///         ChangeParticipantsFrequency = 1,
    ///         ChangeParticipantsUnit = "rotation",
    ///         CustomPeriodFrequency = 1,
    ///         CustomPeriodUnit = "week",
    ///         ParticipantGroups = new[]
    ///         {
    ///             new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupArgs
    ///             {
    ///                 Participants = new[]
    ///                 {
    ///                     new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupParticipantArgs
    ///                     {
    ///                         Id = exampleUser.Apply(getUserResult =&gt; getUserResult.Id),
    ///                         Type = "user",
    ///                     },
    ///                 },
    ///             },
    ///             new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupArgs
    ///             {
    ///                 Participants = new[]
    ///                 {
    ///                     new Squadcast.Inputs.ScheduleRotationV2ParticipantGroupParticipantArgs
    ///                     {
    ///                         Id = exampleUser2.Apply(getUserResult =&gt; getUserResult.Id),
    ///                         Type = "user",
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///         EndDate = "2023-08-31T00:00:00Z",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// teamID:scheduleName:rotationName
    /// 
    /// ```sh
    /// $ pulumi import squadcast:index/scheduleRotationV2:ScheduleRotationV2 rotation "62d2fe23a57381088224d726:Example Schedule:Example Rotation"
    /// ```
    /// </summary>
    [SquadcastResourceType("squadcast:index/scheduleRotationV2:ScheduleRotationV2")]
    public partial class ScheduleRotationV2 : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Frequency with which participants change in the rotation.
        /// </summary>
        [Output("changeParticipantsFrequency")]
        public Output<int> ChangeParticipantsFrequency { get; private set; } = null!;

        /// <summary>
        /// Unit of the frequency with which participants change in the rotation (rotation, day, week, month).
        /// </summary>
        [Output("changeParticipantsUnit")]
        public Output<string> ChangeParticipantsUnit { get; private set; } = null!;

        /// <summary>
        /// Frequency of the custom rotation repeat pattern. Only applicable if period is set to custom.
        /// </summary>
        [Output("customPeriodFrequency")]
        public Output<int?> CustomPeriodFrequency { get; private set; } = null!;

        /// <summary>
        /// Unit of the custom rotation repeat pattern (day, week). Only applicable if period is set to custom.
        /// </summary>
        [Output("customPeriodUnit")]
        public Output<string?> CustomPeriodUnit { get; private set; } = null!;

        /// <summary>
        /// Defines the end date of the schedule rotation.
        /// </summary>
        [Output("endDate")]
        public Output<string?> EndDate { get; private set; } = null!;

        /// <summary>
        /// Defines the number of iterations of the schedule rotation.
        /// </summary>
        [Output("endsAfterIterations")]
        public Output<int?> EndsAfterIterations { get; private set; } = null!;

        /// <summary>
        /// Rotation name.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Ordered list of participant groups for the rotation. For each rotation the participant*groups are cycled through in order.
        /// </summary>
        [Output("participantGroups")]
        public Output<ImmutableArray<Outputs.ScheduleRotationV2ParticipantGroup>> ParticipantGroups { get; private set; } = null!;

        /// <summary>
        /// Rotation period (none, daily, weekly, monthly, custom). Defines how often the rotation repeats.
        /// </summary>
        [Output("period")]
        public Output<string> Period { get; private set; } = null!;

        /// <summary>
        /// id of the schedule that the rotation belongs to.
        /// </summary>
        [Output("scheduleId")]
        public Output<int> ScheduleId { get; private set; } = null!;

        /// <summary>
        /// Timeslots where the rotation is active.
        /// </summary>
        [Output("shiftTimeslots")]
        public Output<ImmutableArray<Outputs.ScheduleRotationV2ShiftTimeslot>> ShiftTimeslots { get; private set; } = null!;

        /// <summary>
        /// Defines the start date of the rotation.
        /// </summary>
        [Output("startDate")]
        public Output<string> StartDate { get; private set; } = null!;


        /// <summary>
        /// Create a ScheduleRotationV2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ScheduleRotationV2(string name, ScheduleRotationV2Args args, CustomResourceOptions? options = null)
            : base("squadcast:index/scheduleRotationV2:ScheduleRotationV2", name, args ?? new ScheduleRotationV2Args(), MakeResourceOptions(options, ""))
        {
        }

        private ScheduleRotationV2(string name, Input<string> id, ScheduleRotationV2State? state = null, CustomResourceOptions? options = null)
            : base("squadcast:index/scheduleRotationV2:ScheduleRotationV2", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ScheduleRotationV2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ScheduleRotationV2 Get(string name, Input<string> id, ScheduleRotationV2State? state = null, CustomResourceOptions? options = null)
        {
            return new ScheduleRotationV2(name, id, state, options);
        }
    }

    public sealed class ScheduleRotationV2Args : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Frequency with which participants change in the rotation.
        /// </summary>
        [Input("changeParticipantsFrequency", required: true)]
        public Input<int> ChangeParticipantsFrequency { get; set; } = null!;

        /// <summary>
        /// Unit of the frequency with which participants change in the rotation (rotation, day, week, month).
        /// </summary>
        [Input("changeParticipantsUnit", required: true)]
        public Input<string> ChangeParticipantsUnit { get; set; } = null!;

        /// <summary>
        /// Frequency of the custom rotation repeat pattern. Only applicable if period is set to custom.
        /// </summary>
        [Input("customPeriodFrequency")]
        public Input<int>? CustomPeriodFrequency { get; set; }

        /// <summary>
        /// Unit of the custom rotation repeat pattern (day, week). Only applicable if period is set to custom.
        /// </summary>
        [Input("customPeriodUnit")]
        public Input<string>? CustomPeriodUnit { get; set; }

        /// <summary>
        /// Defines the end date of the schedule rotation.
        /// </summary>
        [Input("endDate")]
        public Input<string>? EndDate { get; set; }

        /// <summary>
        /// Defines the number of iterations of the schedule rotation.
        /// </summary>
        [Input("endsAfterIterations")]
        public Input<int>? EndsAfterIterations { get; set; }

        /// <summary>
        /// Rotation name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("participantGroups")]
        private InputList<Inputs.ScheduleRotationV2ParticipantGroupArgs>? _participantGroups;

        /// <summary>
        /// Ordered list of participant groups for the rotation. For each rotation the participant*groups are cycled through in order.
        /// </summary>
        public InputList<Inputs.ScheduleRotationV2ParticipantGroupArgs> ParticipantGroups
        {
            get => _participantGroups ?? (_participantGroups = new InputList<Inputs.ScheduleRotationV2ParticipantGroupArgs>());
            set => _participantGroups = value;
        }

        /// <summary>
        /// Rotation period (none, daily, weekly, monthly, custom). Defines how often the rotation repeats.
        /// </summary>
        [Input("period", required: true)]
        public Input<string> Period { get; set; } = null!;

        /// <summary>
        /// id of the schedule that the rotation belongs to.
        /// </summary>
        [Input("scheduleId", required: true)]
        public Input<int> ScheduleId { get; set; } = null!;

        [Input("shiftTimeslots", required: true)]
        private InputList<Inputs.ScheduleRotationV2ShiftTimeslotArgs>? _shiftTimeslots;

        /// <summary>
        /// Timeslots where the rotation is active.
        /// </summary>
        public InputList<Inputs.ScheduleRotationV2ShiftTimeslotArgs> ShiftTimeslots
        {
            get => _shiftTimeslots ?? (_shiftTimeslots = new InputList<Inputs.ScheduleRotationV2ShiftTimeslotArgs>());
            set => _shiftTimeslots = value;
        }

        /// <summary>
        /// Defines the start date of the rotation.
        /// </summary>
        [Input("startDate", required: true)]
        public Input<string> StartDate { get; set; } = null!;

        public ScheduleRotationV2Args()
        {
        }
        public static new ScheduleRotationV2Args Empty => new ScheduleRotationV2Args();
    }

    public sealed class ScheduleRotationV2State : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Frequency with which participants change in the rotation.
        /// </summary>
        [Input("changeParticipantsFrequency")]
        public Input<int>? ChangeParticipantsFrequency { get; set; }

        /// <summary>
        /// Unit of the frequency with which participants change in the rotation (rotation, day, week, month).
        /// </summary>
        [Input("changeParticipantsUnit")]
        public Input<string>? ChangeParticipantsUnit { get; set; }

        /// <summary>
        /// Frequency of the custom rotation repeat pattern. Only applicable if period is set to custom.
        /// </summary>
        [Input("customPeriodFrequency")]
        public Input<int>? CustomPeriodFrequency { get; set; }

        /// <summary>
        /// Unit of the custom rotation repeat pattern (day, week). Only applicable if period is set to custom.
        /// </summary>
        [Input("customPeriodUnit")]
        public Input<string>? CustomPeriodUnit { get; set; }

        /// <summary>
        /// Defines the end date of the schedule rotation.
        /// </summary>
        [Input("endDate")]
        public Input<string>? EndDate { get; set; }

        /// <summary>
        /// Defines the number of iterations of the schedule rotation.
        /// </summary>
        [Input("endsAfterIterations")]
        public Input<int>? EndsAfterIterations { get; set; }

        /// <summary>
        /// Rotation name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("participantGroups")]
        private InputList<Inputs.ScheduleRotationV2ParticipantGroupGetArgs>? _participantGroups;

        /// <summary>
        /// Ordered list of participant groups for the rotation. For each rotation the participant*groups are cycled through in order.
        /// </summary>
        public InputList<Inputs.ScheduleRotationV2ParticipantGroupGetArgs> ParticipantGroups
        {
            get => _participantGroups ?? (_participantGroups = new InputList<Inputs.ScheduleRotationV2ParticipantGroupGetArgs>());
            set => _participantGroups = value;
        }

        /// <summary>
        /// Rotation period (none, daily, weekly, monthly, custom). Defines how often the rotation repeats.
        /// </summary>
        [Input("period")]
        public Input<string>? Period { get; set; }

        /// <summary>
        /// id of the schedule that the rotation belongs to.
        /// </summary>
        [Input("scheduleId")]
        public Input<int>? ScheduleId { get; set; }

        [Input("shiftTimeslots")]
        private InputList<Inputs.ScheduleRotationV2ShiftTimeslotGetArgs>? _shiftTimeslots;

        /// <summary>
        /// Timeslots where the rotation is active.
        /// </summary>
        public InputList<Inputs.ScheduleRotationV2ShiftTimeslotGetArgs> ShiftTimeslots
        {
            get => _shiftTimeslots ?? (_shiftTimeslots = new InputList<Inputs.ScheduleRotationV2ShiftTimeslotGetArgs>());
            set => _shiftTimeslots = value;
        }

        /// <summary>
        /// Defines the start date of the rotation.
        /// </summary>
        [Input("startDate")]
        public Input<string>? StartDate { get; set; }

        public ScheduleRotationV2State()
        {
        }
        public static new ScheduleRotationV2State Empty => new ScheduleRotationV2State();
    }
}
