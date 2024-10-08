// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package squadcast

import (
	"context"
	"reflect"

	"errors"
	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// [Squadcast schedules v2](https://support.squadcast.com/schedules/schedules-new) are used to manage on-call scheduling & determine who will be notified when an incident is triggered. The name of the Schedule must be unique within a Team.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleTeam, err := squadcast.LookupTeam(ctx, &squadcast.LookupTeamArgs{
//				Name: "example team name",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			exampleUser, err := squadcast.LookupUser(ctx, &squadcast.LookupUserArgs{
//				Email: "test@example.com",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewScheduleV2(ctx, "scheduleTest", &squadcast.ScheduleV2Args{
//				Description: pulumi.String("test schedule"),
//				Timezone:    pulumi.String("Asia/Kolkata"),
//				TeamId:      pulumi.String(exampleTeam.Id),
//				EntityOwner: &squadcast.ScheduleV2EntityOwnerArgs{
//					Id:   pulumi.String(exampleUser.Id),
//					Type: pulumi.String("user"),
//				},
//				Tags: squadcast.ScheduleV2TagArray{
//					&squadcast.ScheduleV2TagArgs{
//						Key:   pulumi.String("testkey"),
//						Value: pulumi.String("testval"),
//					},
//					&squadcast.ScheduleV2TagArgs{
//						Key:   pulumi.String("testkey2"),
//						Value: pulumi.String("testval2"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// teamID:scheduleName
//
// Use 'Get All Teams' API to get the id of the team
//
// ```sh
// $ pulumi import squadcast:index/scheduleV2:ScheduleV2 schedule_test "62d2fe23a57381088224d726:Example Schedule"
// ```
type ScheduleV2 struct {
	pulumi.CustomResourceState

	// Detailed description about the schedule.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Schedule owner.
	EntityOwner ScheduleV2EntityOwnerOutput `pulumi:"entityOwner"`
	// Name of the schedule.
	Name pulumi.StringOutput `pulumi:"name"`
	// Schedule tags.
	Tags ScheduleV2TagArrayOutput `pulumi:"tags"`
	// Team id.
	TeamId pulumi.StringOutput `pulumi:"teamId"`
	// Timezone for the schedule.
	Timezone pulumi.StringOutput `pulumi:"timezone"`
}

// NewScheduleV2 registers a new resource with the given unique name, arguments, and options.
func NewScheduleV2(ctx *pulumi.Context,
	name string, args *ScheduleV2Args, opts ...pulumi.ResourceOption) (*ScheduleV2, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EntityOwner == nil {
		return nil, errors.New("invalid value for required argument 'EntityOwner'")
	}
	if args.TeamId == nil {
		return nil, errors.New("invalid value for required argument 'TeamId'")
	}
	if args.Timezone == nil {
		return nil, errors.New("invalid value for required argument 'Timezone'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ScheduleV2
	err := ctx.RegisterResource("squadcast:index/scheduleV2:ScheduleV2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetScheduleV2 gets an existing ScheduleV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetScheduleV2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ScheduleV2State, opts ...pulumi.ResourceOption) (*ScheduleV2, error) {
	var resource ScheduleV2
	err := ctx.ReadResource("squadcast:index/scheduleV2:ScheduleV2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ScheduleV2 resources.
type scheduleV2State struct {
	// Detailed description about the schedule.
	Description *string `pulumi:"description"`
	// Schedule owner.
	EntityOwner *ScheduleV2EntityOwner `pulumi:"entityOwner"`
	// Name of the schedule.
	Name *string `pulumi:"name"`
	// Schedule tags.
	Tags []ScheduleV2Tag `pulumi:"tags"`
	// Team id.
	TeamId *string `pulumi:"teamId"`
	// Timezone for the schedule.
	Timezone *string `pulumi:"timezone"`
}

type ScheduleV2State struct {
	// Detailed description about the schedule.
	Description pulumi.StringPtrInput
	// Schedule owner.
	EntityOwner ScheduleV2EntityOwnerPtrInput
	// Name of the schedule.
	Name pulumi.StringPtrInput
	// Schedule tags.
	Tags ScheduleV2TagArrayInput
	// Team id.
	TeamId pulumi.StringPtrInput
	// Timezone for the schedule.
	Timezone pulumi.StringPtrInput
}

func (ScheduleV2State) ElementType() reflect.Type {
	return reflect.TypeOf((*scheduleV2State)(nil)).Elem()
}

type scheduleV2Args struct {
	// Detailed description about the schedule.
	Description *string `pulumi:"description"`
	// Schedule owner.
	EntityOwner ScheduleV2EntityOwner `pulumi:"entityOwner"`
	// Name of the schedule.
	Name *string `pulumi:"name"`
	// Schedule tags.
	Tags []ScheduleV2Tag `pulumi:"tags"`
	// Team id.
	TeamId string `pulumi:"teamId"`
	// Timezone for the schedule.
	Timezone string `pulumi:"timezone"`
}

// The set of arguments for constructing a ScheduleV2 resource.
type ScheduleV2Args struct {
	// Detailed description about the schedule.
	Description pulumi.StringPtrInput
	// Schedule owner.
	EntityOwner ScheduleV2EntityOwnerInput
	// Name of the schedule.
	Name pulumi.StringPtrInput
	// Schedule tags.
	Tags ScheduleV2TagArrayInput
	// Team id.
	TeamId pulumi.StringInput
	// Timezone for the schedule.
	Timezone pulumi.StringInput
}

func (ScheduleV2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*scheduleV2Args)(nil)).Elem()
}

type ScheduleV2Input interface {
	pulumi.Input

	ToScheduleV2Output() ScheduleV2Output
	ToScheduleV2OutputWithContext(ctx context.Context) ScheduleV2Output
}

func (*ScheduleV2) ElementType() reflect.Type {
	return reflect.TypeOf((**ScheduleV2)(nil)).Elem()
}

func (i *ScheduleV2) ToScheduleV2Output() ScheduleV2Output {
	return i.ToScheduleV2OutputWithContext(context.Background())
}

func (i *ScheduleV2) ToScheduleV2OutputWithContext(ctx context.Context) ScheduleV2Output {
	return pulumi.ToOutputWithContext(ctx, i).(ScheduleV2Output)
}

// ScheduleV2ArrayInput is an input type that accepts ScheduleV2Array and ScheduleV2ArrayOutput values.
// You can construct a concrete instance of `ScheduleV2ArrayInput` via:
//
//	ScheduleV2Array{ ScheduleV2Args{...} }
type ScheduleV2ArrayInput interface {
	pulumi.Input

	ToScheduleV2ArrayOutput() ScheduleV2ArrayOutput
	ToScheduleV2ArrayOutputWithContext(context.Context) ScheduleV2ArrayOutput
}

type ScheduleV2Array []ScheduleV2Input

func (ScheduleV2Array) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ScheduleV2)(nil)).Elem()
}

func (i ScheduleV2Array) ToScheduleV2ArrayOutput() ScheduleV2ArrayOutput {
	return i.ToScheduleV2ArrayOutputWithContext(context.Background())
}

func (i ScheduleV2Array) ToScheduleV2ArrayOutputWithContext(ctx context.Context) ScheduleV2ArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScheduleV2ArrayOutput)
}

// ScheduleV2MapInput is an input type that accepts ScheduleV2Map and ScheduleV2MapOutput values.
// You can construct a concrete instance of `ScheduleV2MapInput` via:
//
//	ScheduleV2Map{ "key": ScheduleV2Args{...} }
type ScheduleV2MapInput interface {
	pulumi.Input

	ToScheduleV2MapOutput() ScheduleV2MapOutput
	ToScheduleV2MapOutputWithContext(context.Context) ScheduleV2MapOutput
}

type ScheduleV2Map map[string]ScheduleV2Input

func (ScheduleV2Map) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ScheduleV2)(nil)).Elem()
}

func (i ScheduleV2Map) ToScheduleV2MapOutput() ScheduleV2MapOutput {
	return i.ToScheduleV2MapOutputWithContext(context.Background())
}

func (i ScheduleV2Map) ToScheduleV2MapOutputWithContext(ctx context.Context) ScheduleV2MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScheduleV2MapOutput)
}

type ScheduleV2Output struct{ *pulumi.OutputState }

func (ScheduleV2Output) ElementType() reflect.Type {
	return reflect.TypeOf((**ScheduleV2)(nil)).Elem()
}

func (o ScheduleV2Output) ToScheduleV2Output() ScheduleV2Output {
	return o
}

func (o ScheduleV2Output) ToScheduleV2OutputWithContext(ctx context.Context) ScheduleV2Output {
	return o
}

// Detailed description about the schedule.
func (o ScheduleV2Output) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ScheduleV2) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Schedule owner.
func (o ScheduleV2Output) EntityOwner() ScheduleV2EntityOwnerOutput {
	return o.ApplyT(func(v *ScheduleV2) ScheduleV2EntityOwnerOutput { return v.EntityOwner }).(ScheduleV2EntityOwnerOutput)
}

// Name of the schedule.
func (o ScheduleV2Output) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ScheduleV2) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Schedule tags.
func (o ScheduleV2Output) Tags() ScheduleV2TagArrayOutput {
	return o.ApplyT(func(v *ScheduleV2) ScheduleV2TagArrayOutput { return v.Tags }).(ScheduleV2TagArrayOutput)
}

// Team id.
func (o ScheduleV2Output) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v *ScheduleV2) pulumi.StringOutput { return v.TeamId }).(pulumi.StringOutput)
}

// Timezone for the schedule.
func (o ScheduleV2Output) Timezone() pulumi.StringOutput {
	return o.ApplyT(func(v *ScheduleV2) pulumi.StringOutput { return v.Timezone }).(pulumi.StringOutput)
}

type ScheduleV2ArrayOutput struct{ *pulumi.OutputState }

func (ScheduleV2ArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ScheduleV2)(nil)).Elem()
}

func (o ScheduleV2ArrayOutput) ToScheduleV2ArrayOutput() ScheduleV2ArrayOutput {
	return o
}

func (o ScheduleV2ArrayOutput) ToScheduleV2ArrayOutputWithContext(ctx context.Context) ScheduleV2ArrayOutput {
	return o
}

func (o ScheduleV2ArrayOutput) Index(i pulumi.IntInput) ScheduleV2Output {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ScheduleV2 {
		return vs[0].([]*ScheduleV2)[vs[1].(int)]
	}).(ScheduleV2Output)
}

type ScheduleV2MapOutput struct{ *pulumi.OutputState }

func (ScheduleV2MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ScheduleV2)(nil)).Elem()
}

func (o ScheduleV2MapOutput) ToScheduleV2MapOutput() ScheduleV2MapOutput {
	return o
}

func (o ScheduleV2MapOutput) ToScheduleV2MapOutputWithContext(ctx context.Context) ScheduleV2MapOutput {
	return o
}

func (o ScheduleV2MapOutput) MapIndex(k pulumi.StringInput) ScheduleV2Output {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ScheduleV2 {
		return vs[0].(map[string]*ScheduleV2)[vs[1].(string)]
	}).(ScheduleV2Output)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ScheduleV2Input)(nil)).Elem(), &ScheduleV2{})
	pulumi.RegisterInputType(reflect.TypeOf((*ScheduleV2ArrayInput)(nil)).Elem(), ScheduleV2Array{})
	pulumi.RegisterInputType(reflect.TypeOf((*ScheduleV2MapInput)(nil)).Elem(), ScheduleV2Map{})
	pulumi.RegisterOutputType(ScheduleV2Output{})
	pulumi.RegisterOutputType(ScheduleV2ArrayOutput{})
	pulumi.RegisterOutputType(ScheduleV2MapOutput{})
}
