// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ger

import (
	"context"
	"reflect"

	"errors"
	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// GER Ruleset is a set of rules and configurations in Squadcast. It allows users to define how alerts are routed to services without the need to set up individual webhooks for each alert source.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast"
//	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/ger"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			exampleTeam, err := squadcast.LookupTeam(ctx, &squadcast.LookupTeamArgs{
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
//			exampleService, err := squadcast.LookupService(ctx, &squadcast.LookupServiceArgs{
//				Name:   "Example Service",
//				TeamId: exampleTeam.Id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			exampleGer, err := squadcast.NewGer(ctx, "exampleGer", &squadcast.GerArgs{
//				Description: pulumi.String("Example GER Description"),
//				TeamId:      pulumi.String(exampleTeam.Id),
//				EntityOwner: &squadcast.GerEntityOwnerArgs{
//					Id:   pulumi.String(user.Id),
//					Type: pulumi.String("user"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ger.NewRuleset(ctx, "exampleGerRuleset", &ger.RulesetArgs{
//				GerId:       exampleGer.ID(),
//				AlertSource: pulumi.String("Prometheus"),
//				CatchAllAction: pulumi.StringMap{
//					"route_to": pulumi.String(exampleService.Id),
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
// gerID:alertSourceName
//
// ```sh
// $ pulumi import squadcast:ger/ruleset:Ruleset example_ger_ruleset_import "53:Grafana"
// ```
type Ruleset struct {
	pulumi.CustomResourceState

	// An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
	AlertSource pulumi.StringOutput `pulumi:"alertSource"`
	// Shortname of the linked alert source.
	AlertSourceShortname pulumi.StringOutput `pulumi:"alertSourceShortname"`
	// Version of the linked alert source.
	AlertSourceVersion pulumi.StringOutput `pulumi:"alertSourceVersion"`
	// The "Catch-All Action", when configured, specifies a fall back service. If none of the defined rules for an incoming event evaluate to true, the incoming event is routed to the Catch-All service, ensuring no events are missed.
	CatchAllAction pulumi.StringMapOutput `pulumi:"catchAllAction"`
	// GER id.
	GerId pulumi.StringOutput `pulumi:"gerId"`
}

// NewRuleset registers a new resource with the given unique name, arguments, and options.
func NewRuleset(ctx *pulumi.Context,
	name string, args *RulesetArgs, opts ...pulumi.ResourceOption) (*Ruleset, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AlertSource == nil {
		return nil, errors.New("invalid value for required argument 'AlertSource'")
	}
	if args.GerId == nil {
		return nil, errors.New("invalid value for required argument 'GerId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Ruleset
	err := ctx.RegisterResource("squadcast:ger/ruleset:Ruleset", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRuleset gets an existing Ruleset resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRuleset(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RulesetState, opts ...pulumi.ResourceOption) (*Ruleset, error) {
	var resource Ruleset
	err := ctx.ReadResource("squadcast:ger/ruleset:Ruleset", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Ruleset resources.
type rulesetState struct {
	// An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
	AlertSource *string `pulumi:"alertSource"`
	// Shortname of the linked alert source.
	AlertSourceShortname *string `pulumi:"alertSourceShortname"`
	// Version of the linked alert source.
	AlertSourceVersion *string `pulumi:"alertSourceVersion"`
	// The "Catch-All Action", when configured, specifies a fall back service. If none of the defined rules for an incoming event evaluate to true, the incoming event is routed to the Catch-All service, ensuring no events are missed.
	CatchAllAction map[string]string `pulumi:"catchAllAction"`
	// GER id.
	GerId *string `pulumi:"gerId"`
}

type RulesetState struct {
	// An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
	AlertSource pulumi.StringPtrInput
	// Shortname of the linked alert source.
	AlertSourceShortname pulumi.StringPtrInput
	// Version of the linked alert source.
	AlertSourceVersion pulumi.StringPtrInput
	// The "Catch-All Action", when configured, specifies a fall back service. If none of the defined rules for an incoming event evaluate to true, the incoming event is routed to the Catch-All service, ensuring no events are missed.
	CatchAllAction pulumi.StringMapInput
	// GER id.
	GerId pulumi.StringPtrInput
}

func (RulesetState) ElementType() reflect.Type {
	return reflect.TypeOf((*rulesetState)(nil)).Elem()
}

type rulesetArgs struct {
	// An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
	AlertSource string `pulumi:"alertSource"`
	// The "Catch-All Action", when configured, specifies a fall back service. If none of the defined rules for an incoming event evaluate to true, the incoming event is routed to the Catch-All service, ensuring no events are missed.
	CatchAllAction map[string]string `pulumi:"catchAllAction"`
	// GER id.
	GerId string `pulumi:"gerId"`
}

// The set of arguments for constructing a Ruleset resource.
type RulesetArgs struct {
	// An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
	AlertSource pulumi.StringInput
	// The "Catch-All Action", when configured, specifies a fall back service. If none of the defined rules for an incoming event evaluate to true, the incoming event is routed to the Catch-All service, ensuring no events are missed.
	CatchAllAction pulumi.StringMapInput
	// GER id.
	GerId pulumi.StringInput
}

func (RulesetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rulesetArgs)(nil)).Elem()
}

type RulesetInput interface {
	pulumi.Input

	ToRulesetOutput() RulesetOutput
	ToRulesetOutputWithContext(ctx context.Context) RulesetOutput
}

func (*Ruleset) ElementType() reflect.Type {
	return reflect.TypeOf((**Ruleset)(nil)).Elem()
}

func (i *Ruleset) ToRulesetOutput() RulesetOutput {
	return i.ToRulesetOutputWithContext(context.Background())
}

func (i *Ruleset) ToRulesetOutputWithContext(ctx context.Context) RulesetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RulesetOutput)
}

// RulesetArrayInput is an input type that accepts RulesetArray and RulesetArrayOutput values.
// You can construct a concrete instance of `RulesetArrayInput` via:
//
//	RulesetArray{ RulesetArgs{...} }
type RulesetArrayInput interface {
	pulumi.Input

	ToRulesetArrayOutput() RulesetArrayOutput
	ToRulesetArrayOutputWithContext(context.Context) RulesetArrayOutput
}

type RulesetArray []RulesetInput

func (RulesetArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ruleset)(nil)).Elem()
}

func (i RulesetArray) ToRulesetArrayOutput() RulesetArrayOutput {
	return i.ToRulesetArrayOutputWithContext(context.Background())
}

func (i RulesetArray) ToRulesetArrayOutputWithContext(ctx context.Context) RulesetArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RulesetArrayOutput)
}

// RulesetMapInput is an input type that accepts RulesetMap and RulesetMapOutput values.
// You can construct a concrete instance of `RulesetMapInput` via:
//
//	RulesetMap{ "key": RulesetArgs{...} }
type RulesetMapInput interface {
	pulumi.Input

	ToRulesetMapOutput() RulesetMapOutput
	ToRulesetMapOutputWithContext(context.Context) RulesetMapOutput
}

type RulesetMap map[string]RulesetInput

func (RulesetMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ruleset)(nil)).Elem()
}

func (i RulesetMap) ToRulesetMapOutput() RulesetMapOutput {
	return i.ToRulesetMapOutputWithContext(context.Background())
}

func (i RulesetMap) ToRulesetMapOutputWithContext(ctx context.Context) RulesetMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RulesetMapOutput)
}

type RulesetOutput struct{ *pulumi.OutputState }

func (RulesetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Ruleset)(nil)).Elem()
}

func (o RulesetOutput) ToRulesetOutput() RulesetOutput {
	return o
}

func (o RulesetOutput) ToRulesetOutputWithContext(ctx context.Context) RulesetOutput {
	return o
}

// An alert source refers to the origin of an event (alert), such as a monitoring tool. These alert sources are associated with specific rules in GER, determining where events from each source should be routed. Find all alert sources supported on Squadcast [here](https://www.squadcast.com/integrations).
func (o RulesetOutput) AlertSource() pulumi.StringOutput {
	return o.ApplyT(func(v *Ruleset) pulumi.StringOutput { return v.AlertSource }).(pulumi.StringOutput)
}

// Shortname of the linked alert source.
func (o RulesetOutput) AlertSourceShortname() pulumi.StringOutput {
	return o.ApplyT(func(v *Ruleset) pulumi.StringOutput { return v.AlertSourceShortname }).(pulumi.StringOutput)
}

// Version of the linked alert source.
func (o RulesetOutput) AlertSourceVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *Ruleset) pulumi.StringOutput { return v.AlertSourceVersion }).(pulumi.StringOutput)
}

// The "Catch-All Action", when configured, specifies a fall back service. If none of the defined rules for an incoming event evaluate to true, the incoming event is routed to the Catch-All service, ensuring no events are missed.
func (o RulesetOutput) CatchAllAction() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Ruleset) pulumi.StringMapOutput { return v.CatchAllAction }).(pulumi.StringMapOutput)
}

// GER id.
func (o RulesetOutput) GerId() pulumi.StringOutput {
	return o.ApplyT(func(v *Ruleset) pulumi.StringOutput { return v.GerId }).(pulumi.StringOutput)
}

type RulesetArrayOutput struct{ *pulumi.OutputState }

func (RulesetArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ruleset)(nil)).Elem()
}

func (o RulesetArrayOutput) ToRulesetArrayOutput() RulesetArrayOutput {
	return o
}

func (o RulesetArrayOutput) ToRulesetArrayOutputWithContext(ctx context.Context) RulesetArrayOutput {
	return o
}

func (o RulesetArrayOutput) Index(i pulumi.IntInput) RulesetOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Ruleset {
		return vs[0].([]*Ruleset)[vs[1].(int)]
	}).(RulesetOutput)
}

type RulesetMapOutput struct{ *pulumi.OutputState }

func (RulesetMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ruleset)(nil)).Elem()
}

func (o RulesetMapOutput) ToRulesetMapOutput() RulesetMapOutput {
	return o
}

func (o RulesetMapOutput) ToRulesetMapOutputWithContext(ctx context.Context) RulesetMapOutput {
	return o
}

func (o RulesetMapOutput) MapIndex(k pulumi.StringInput) RulesetOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Ruleset {
		return vs[0].(map[string]*Ruleset)[vs[1].(string)]
	}).(RulesetOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RulesetInput)(nil)).Elem(), &Ruleset{})
	pulumi.RegisterInputType(reflect.TypeOf((*RulesetArrayInput)(nil)).Elem(), RulesetArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RulesetMapInput)(nil)).Elem(), RulesetMap{})
	pulumi.RegisterOutputType(RulesetOutput{})
	pulumi.RegisterOutputType(RulesetArrayOutput{})
	pulumi.RegisterOutputType(RulesetMapOutput{})
}
