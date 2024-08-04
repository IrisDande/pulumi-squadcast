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

// Global Event Ruleset (GER) is a centralized set of rules that defines service routes for incoming events.
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
//			team, err := squadcast.LookupTeam(ctx, &squadcast.LookupTeamArgs{
//				Name: "Example Team",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			user, err := squadcast.LookupUser(ctx, &squadcast.LookupUserArgs{
//				Email: "john@example.com",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.LookupService(ctx, &squadcast.LookupServiceArgs{
//				Name:   "Example Service",
//				TeamId: team.Id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewGer(ctx, "ger", &squadcast.GerArgs{
//				Description: pulumi.String("Example GER Description"),
//				TeamId:      pulumi.String(team.Id),
//				EntityOwner: &squadcast.GerEntityOwnerArgs{
//					Id:   pulumi.String(user.Id),
//					Type: pulumi.String("user"),
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
// gerID
//
// ```sh
// $ pulumi import squadcast:index/ger:Ger example_ger_import "53"
// ```
type Ger struct {
	pulumi.CustomResourceState

	// GER description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// GER owner.
	EntityOwner GerEntityOwnerOutput `pulumi:"entityOwner"`
	// GER name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Routing Key is an identifier used to determine the ruleset that an incoming event belongs to. It is a common key that associates multiple alert sources with their configured rules, ensuring events are routed to the appropriate services when the defined criteria are met.
	RoutingKey pulumi.StringOutput `pulumi:"routingKey"`
	// Team id.
	TeamId pulumi.StringOutput `pulumi:"teamId"`
}

// NewGer registers a new resource with the given unique name, arguments, and options.
func NewGer(ctx *pulumi.Context,
	name string, args *GerArgs, opts ...pulumi.ResourceOption) (*Ger, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EntityOwner == nil {
		return nil, errors.New("invalid value for required argument 'EntityOwner'")
	}
	if args.TeamId == nil {
		return nil, errors.New("invalid value for required argument 'TeamId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Ger
	err := ctx.RegisterResource("squadcast:index/ger:Ger", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGer gets an existing Ger resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GerState, opts ...pulumi.ResourceOption) (*Ger, error) {
	var resource Ger
	err := ctx.ReadResource("squadcast:index/ger:Ger", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Ger resources.
type gerState struct {
	// GER description.
	Description *string `pulumi:"description"`
	// GER owner.
	EntityOwner *GerEntityOwner `pulumi:"entityOwner"`
	// GER name.
	Name *string `pulumi:"name"`
	// Routing Key is an identifier used to determine the ruleset that an incoming event belongs to. It is a common key that associates multiple alert sources with their configured rules, ensuring events are routed to the appropriate services when the defined criteria are met.
	RoutingKey *string `pulumi:"routingKey"`
	// Team id.
	TeamId *string `pulumi:"teamId"`
}

type GerState struct {
	// GER description.
	Description pulumi.StringPtrInput
	// GER owner.
	EntityOwner GerEntityOwnerPtrInput
	// GER name.
	Name pulumi.StringPtrInput
	// Routing Key is an identifier used to determine the ruleset that an incoming event belongs to. It is a common key that associates multiple alert sources with their configured rules, ensuring events are routed to the appropriate services when the defined criteria are met.
	RoutingKey pulumi.StringPtrInput
	// Team id.
	TeamId pulumi.StringPtrInput
}

func (GerState) ElementType() reflect.Type {
	return reflect.TypeOf((*gerState)(nil)).Elem()
}

type gerArgs struct {
	// GER description.
	Description *string `pulumi:"description"`
	// GER owner.
	EntityOwner GerEntityOwner `pulumi:"entityOwner"`
	// GER name.
	Name *string `pulumi:"name"`
	// Team id.
	TeamId string `pulumi:"teamId"`
}

// The set of arguments for constructing a Ger resource.
type GerArgs struct {
	// GER description.
	Description pulumi.StringPtrInput
	// GER owner.
	EntityOwner GerEntityOwnerInput
	// GER name.
	Name pulumi.StringPtrInput
	// Team id.
	TeamId pulumi.StringInput
}

func (GerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gerArgs)(nil)).Elem()
}

type GerInput interface {
	pulumi.Input

	ToGerOutput() GerOutput
	ToGerOutputWithContext(ctx context.Context) GerOutput
}

func (*Ger) ElementType() reflect.Type {
	return reflect.TypeOf((**Ger)(nil)).Elem()
}

func (i *Ger) ToGerOutput() GerOutput {
	return i.ToGerOutputWithContext(context.Background())
}

func (i *Ger) ToGerOutputWithContext(ctx context.Context) GerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GerOutput)
}

// GerArrayInput is an input type that accepts GerArray and GerArrayOutput values.
// You can construct a concrete instance of `GerArrayInput` via:
//
//	GerArray{ GerArgs{...} }
type GerArrayInput interface {
	pulumi.Input

	ToGerArrayOutput() GerArrayOutput
	ToGerArrayOutputWithContext(context.Context) GerArrayOutput
}

type GerArray []GerInput

func (GerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ger)(nil)).Elem()
}

func (i GerArray) ToGerArrayOutput() GerArrayOutput {
	return i.ToGerArrayOutputWithContext(context.Background())
}

func (i GerArray) ToGerArrayOutputWithContext(ctx context.Context) GerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GerArrayOutput)
}

// GerMapInput is an input type that accepts GerMap and GerMapOutput values.
// You can construct a concrete instance of `GerMapInput` via:
//
//	GerMap{ "key": GerArgs{...} }
type GerMapInput interface {
	pulumi.Input

	ToGerMapOutput() GerMapOutput
	ToGerMapOutputWithContext(context.Context) GerMapOutput
}

type GerMap map[string]GerInput

func (GerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ger)(nil)).Elem()
}

func (i GerMap) ToGerMapOutput() GerMapOutput {
	return i.ToGerMapOutputWithContext(context.Background())
}

func (i GerMap) ToGerMapOutputWithContext(ctx context.Context) GerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GerMapOutput)
}

type GerOutput struct{ *pulumi.OutputState }

func (GerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Ger)(nil)).Elem()
}

func (o GerOutput) ToGerOutput() GerOutput {
	return o
}

func (o GerOutput) ToGerOutputWithContext(ctx context.Context) GerOutput {
	return o
}

// GER description.
func (o GerOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Ger) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// GER owner.
func (o GerOutput) EntityOwner() GerEntityOwnerOutput {
	return o.ApplyT(func(v *Ger) GerEntityOwnerOutput { return v.EntityOwner }).(GerEntityOwnerOutput)
}

// GER name.
func (o GerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Ger) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Routing Key is an identifier used to determine the ruleset that an incoming event belongs to. It is a common key that associates multiple alert sources with their configured rules, ensuring events are routed to the appropriate services when the defined criteria are met.
func (o GerOutput) RoutingKey() pulumi.StringOutput {
	return o.ApplyT(func(v *Ger) pulumi.StringOutput { return v.RoutingKey }).(pulumi.StringOutput)
}

// Team id.
func (o GerOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v *Ger) pulumi.StringOutput { return v.TeamId }).(pulumi.StringOutput)
}

type GerArrayOutput struct{ *pulumi.OutputState }

func (GerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ger)(nil)).Elem()
}

func (o GerArrayOutput) ToGerArrayOutput() GerArrayOutput {
	return o
}

func (o GerArrayOutput) ToGerArrayOutputWithContext(ctx context.Context) GerArrayOutput {
	return o
}

func (o GerArrayOutput) Index(i pulumi.IntInput) GerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Ger {
		return vs[0].([]*Ger)[vs[1].(int)]
	}).(GerOutput)
}

type GerMapOutput struct{ *pulumi.OutputState }

func (GerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ger)(nil)).Elem()
}

func (o GerMapOutput) ToGerMapOutput() GerMapOutput {
	return o
}

func (o GerMapOutput) ToGerMapOutputWithContext(ctx context.Context) GerMapOutput {
	return o
}

func (o GerMapOutput) MapIndex(k pulumi.StringInput) GerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Ger {
		return vs[0].(map[string]*Ger)[vs[1].(string)]
	}).(GerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GerInput)(nil)).Elem(), &Ger{})
	pulumi.RegisterInputType(reflect.TypeOf((*GerArrayInput)(nil)).Elem(), GerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GerMapInput)(nil)).Elem(), GerMap{})
	pulumi.RegisterOutputType(GerOutput{})
	pulumi.RegisterOutputType(GerArrayOutput{})
	pulumi.RegisterOutputType(GerMapOutput{})
}
