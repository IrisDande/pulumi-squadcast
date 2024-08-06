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

// [Deduplication rules](https://support.squadcast.com/docs/de-duplication-rules) can help you reduce alert noise by organising and grouping alerts. This also provides easy access to similar alerts when needed. When these rules evaluate to true for an incoming incident, alerts will get deduplicated.
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
//			exampleService, err := squadcast.LookupService(ctx, &squadcast.LookupServiceArgs{
//				Name:   "example service name",
//				TeamId: exampleTeam.Id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewDeduplicationRuleV2(ctx, "exampleDeduplicationRule", &squadcast.DeduplicationRuleV2Args{
//				ServiceId:   pulumi.String(exampleService.Id),
//				IsBasic:     pulumi.Bool(false),
//				Description: pulumi.String("not basic"),
//				Expression:  pulumi.String("payload[\"event_id\"] == 40"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewDeduplicationRuleV2(ctx, "exampleBasicDeduplicationRule", &squadcast.DeduplicationRuleV2Args{
//				ServiceId:               pulumi.String(exampleService.Id),
//				IsBasic:                 pulumi.Bool(true),
//				Description:             pulumi.String("basic"),
//				DependencyDeduplication: pulumi.Bool(true),
//				TimeWindow:              pulumi.Int(2),
//				TimeUnit:                pulumi.String("hour"),
//				BasicExpressions: squadcast.DeduplicationRuleV2BasicExpressionArray{
//					&squadcast.DeduplicationRuleV2BasicExpressionArgs{
//						Lhs: pulumi.String("payload[\"foo\"]"),
//						Op:  pulumi.String("is"),
//						Rhs: pulumi.String("bar"),
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
// serviceID:ruleID
//
// ```sh
// $ pulumi import squadcast:index/deduplicationRuleV2:DeduplicationRuleV2 test_resource_name 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
// ```
type DeduplicationRuleV2 struct {
	pulumi.CustomResourceState

	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions DeduplicationRuleV2BasicExpressionArrayOutput `pulumi:"basicExpressions"`
	// Denotes if dependent services should also be deduplicated
	DependencyDeduplication pulumi.BoolPtrOutput `pulumi:"dependencyDeduplication"`
	// description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression pulumi.StringPtrOutput `pulumi:"expression"`
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic pulumi.BoolOutput `pulumi:"isBasic"`
	// Service id.
	ServiceId pulumi.StringOutput `pulumi:"serviceId"`
	// time unit (mins or hours)
	TimeUnit pulumi.StringPtrOutput `pulumi:"timeUnit"`
	// integer for time_unit
	TimeWindow pulumi.IntPtrOutput `pulumi:"timeWindow"`
}

// NewDeduplicationRuleV2 registers a new resource with the given unique name, arguments, and options.
func NewDeduplicationRuleV2(ctx *pulumi.Context,
	name string, args *DeduplicationRuleV2Args, opts ...pulumi.ResourceOption) (*DeduplicationRuleV2, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IsBasic == nil {
		return nil, errors.New("invalid value for required argument 'IsBasic'")
	}
	if args.ServiceId == nil {
		return nil, errors.New("invalid value for required argument 'ServiceId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeduplicationRuleV2
	err := ctx.RegisterResource("squadcast:index/deduplicationRuleV2:DeduplicationRuleV2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeduplicationRuleV2 gets an existing DeduplicationRuleV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeduplicationRuleV2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeduplicationRuleV2State, opts ...pulumi.ResourceOption) (*DeduplicationRuleV2, error) {
	var resource DeduplicationRuleV2
	err := ctx.ReadResource("squadcast:index/deduplicationRuleV2:DeduplicationRuleV2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeduplicationRuleV2 resources.
type deduplicationRuleV2State struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions []DeduplicationRuleV2BasicExpression `pulumi:"basicExpressions"`
	// Denotes if dependent services should also be deduplicated
	DependencyDeduplication *bool `pulumi:"dependencyDeduplication"`
	// description.
	Description *string `pulumi:"description"`
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression *string `pulumi:"expression"`
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic *bool `pulumi:"isBasic"`
	// Service id.
	ServiceId *string `pulumi:"serviceId"`
	// time unit (mins or hours)
	TimeUnit *string `pulumi:"timeUnit"`
	// integer for time_unit
	TimeWindow *int `pulumi:"timeWindow"`
}

type DeduplicationRuleV2State struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions DeduplicationRuleV2BasicExpressionArrayInput
	// Denotes if dependent services should also be deduplicated
	DependencyDeduplication pulumi.BoolPtrInput
	// description.
	Description pulumi.StringPtrInput
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression pulumi.StringPtrInput
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic pulumi.BoolPtrInput
	// Service id.
	ServiceId pulumi.StringPtrInput
	// time unit (mins or hours)
	TimeUnit pulumi.StringPtrInput
	// integer for time_unit
	TimeWindow pulumi.IntPtrInput
}

func (DeduplicationRuleV2State) ElementType() reflect.Type {
	return reflect.TypeOf((*deduplicationRuleV2State)(nil)).Elem()
}

type deduplicationRuleV2Args struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions []DeduplicationRuleV2BasicExpression `pulumi:"basicExpressions"`
	// Denotes if dependent services should also be deduplicated
	DependencyDeduplication *bool `pulumi:"dependencyDeduplication"`
	// description.
	Description *string `pulumi:"description"`
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression *string `pulumi:"expression"`
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic bool `pulumi:"isBasic"`
	// Service id.
	ServiceId string `pulumi:"serviceId"`
	// time unit (mins or hours)
	TimeUnit *string `pulumi:"timeUnit"`
	// integer for time_unit
	TimeWindow *int `pulumi:"timeWindow"`
}

// The set of arguments for constructing a DeduplicationRuleV2 resource.
type DeduplicationRuleV2Args struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions DeduplicationRuleV2BasicExpressionArrayInput
	// Denotes if dependent services should also be deduplicated
	DependencyDeduplication pulumi.BoolPtrInput
	// description.
	Description pulumi.StringPtrInput
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression pulumi.StringPtrInput
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic pulumi.BoolInput
	// Service id.
	ServiceId pulumi.StringInput
	// time unit (mins or hours)
	TimeUnit pulumi.StringPtrInput
	// integer for time_unit
	TimeWindow pulumi.IntPtrInput
}

func (DeduplicationRuleV2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*deduplicationRuleV2Args)(nil)).Elem()
}

type DeduplicationRuleV2Input interface {
	pulumi.Input

	ToDeduplicationRuleV2Output() DeduplicationRuleV2Output
	ToDeduplicationRuleV2OutputWithContext(ctx context.Context) DeduplicationRuleV2Output
}

func (*DeduplicationRuleV2) ElementType() reflect.Type {
	return reflect.TypeOf((**DeduplicationRuleV2)(nil)).Elem()
}

func (i *DeduplicationRuleV2) ToDeduplicationRuleV2Output() DeduplicationRuleV2Output {
	return i.ToDeduplicationRuleV2OutputWithContext(context.Background())
}

func (i *DeduplicationRuleV2) ToDeduplicationRuleV2OutputWithContext(ctx context.Context) DeduplicationRuleV2Output {
	return pulumi.ToOutputWithContext(ctx, i).(DeduplicationRuleV2Output)
}

// DeduplicationRuleV2ArrayInput is an input type that accepts DeduplicationRuleV2Array and DeduplicationRuleV2ArrayOutput values.
// You can construct a concrete instance of `DeduplicationRuleV2ArrayInput` via:
//
//	DeduplicationRuleV2Array{ DeduplicationRuleV2Args{...} }
type DeduplicationRuleV2ArrayInput interface {
	pulumi.Input

	ToDeduplicationRuleV2ArrayOutput() DeduplicationRuleV2ArrayOutput
	ToDeduplicationRuleV2ArrayOutputWithContext(context.Context) DeduplicationRuleV2ArrayOutput
}

type DeduplicationRuleV2Array []DeduplicationRuleV2Input

func (DeduplicationRuleV2Array) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DeduplicationRuleV2)(nil)).Elem()
}

func (i DeduplicationRuleV2Array) ToDeduplicationRuleV2ArrayOutput() DeduplicationRuleV2ArrayOutput {
	return i.ToDeduplicationRuleV2ArrayOutputWithContext(context.Background())
}

func (i DeduplicationRuleV2Array) ToDeduplicationRuleV2ArrayOutputWithContext(ctx context.Context) DeduplicationRuleV2ArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeduplicationRuleV2ArrayOutput)
}

// DeduplicationRuleV2MapInput is an input type that accepts DeduplicationRuleV2Map and DeduplicationRuleV2MapOutput values.
// You can construct a concrete instance of `DeduplicationRuleV2MapInput` via:
//
//	DeduplicationRuleV2Map{ "key": DeduplicationRuleV2Args{...} }
type DeduplicationRuleV2MapInput interface {
	pulumi.Input

	ToDeduplicationRuleV2MapOutput() DeduplicationRuleV2MapOutput
	ToDeduplicationRuleV2MapOutputWithContext(context.Context) DeduplicationRuleV2MapOutput
}

type DeduplicationRuleV2Map map[string]DeduplicationRuleV2Input

func (DeduplicationRuleV2Map) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DeduplicationRuleV2)(nil)).Elem()
}

func (i DeduplicationRuleV2Map) ToDeduplicationRuleV2MapOutput() DeduplicationRuleV2MapOutput {
	return i.ToDeduplicationRuleV2MapOutputWithContext(context.Background())
}

func (i DeduplicationRuleV2Map) ToDeduplicationRuleV2MapOutputWithContext(ctx context.Context) DeduplicationRuleV2MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeduplicationRuleV2MapOutput)
}

type DeduplicationRuleV2Output struct{ *pulumi.OutputState }

func (DeduplicationRuleV2Output) ElementType() reflect.Type {
	return reflect.TypeOf((**DeduplicationRuleV2)(nil)).Elem()
}

func (o DeduplicationRuleV2Output) ToDeduplicationRuleV2Output() DeduplicationRuleV2Output {
	return o
}

func (o DeduplicationRuleV2Output) ToDeduplicationRuleV2OutputWithContext(ctx context.Context) DeduplicationRuleV2Output {
	return o
}

// The basic expression which needs to be evaluated to be true for this rule to apply.
func (o DeduplicationRuleV2Output) BasicExpressions() DeduplicationRuleV2BasicExpressionArrayOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) DeduplicationRuleV2BasicExpressionArrayOutput { return v.BasicExpressions }).(DeduplicationRuleV2BasicExpressionArrayOutput)
}

// Denotes if dependent services should also be deduplicated
func (o DeduplicationRuleV2Output) DependencyDeduplication() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.BoolPtrOutput { return v.DependencyDeduplication }).(pulumi.BoolPtrOutput)
}

// description.
func (o DeduplicationRuleV2Output) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The expression which needs to be evaluated to be true for this rule to apply.
func (o DeduplicationRuleV2Output) Expression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.StringPtrOutput { return v.Expression }).(pulumi.StringPtrOutput)
}

// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
func (o DeduplicationRuleV2Output) IsBasic() pulumi.BoolOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.BoolOutput { return v.IsBasic }).(pulumi.BoolOutput)
}

// Service id.
func (o DeduplicationRuleV2Output) ServiceId() pulumi.StringOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.StringOutput { return v.ServiceId }).(pulumi.StringOutput)
}

// time unit (mins or hours)
func (o DeduplicationRuleV2Output) TimeUnit() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.StringPtrOutput { return v.TimeUnit }).(pulumi.StringPtrOutput)
}

// integer for time_unit
func (o DeduplicationRuleV2Output) TimeWindow() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *DeduplicationRuleV2) pulumi.IntPtrOutput { return v.TimeWindow }).(pulumi.IntPtrOutput)
}

type DeduplicationRuleV2ArrayOutput struct{ *pulumi.OutputState }

func (DeduplicationRuleV2ArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DeduplicationRuleV2)(nil)).Elem()
}

func (o DeduplicationRuleV2ArrayOutput) ToDeduplicationRuleV2ArrayOutput() DeduplicationRuleV2ArrayOutput {
	return o
}

func (o DeduplicationRuleV2ArrayOutput) ToDeduplicationRuleV2ArrayOutputWithContext(ctx context.Context) DeduplicationRuleV2ArrayOutput {
	return o
}

func (o DeduplicationRuleV2ArrayOutput) Index(i pulumi.IntInput) DeduplicationRuleV2Output {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DeduplicationRuleV2 {
		return vs[0].([]*DeduplicationRuleV2)[vs[1].(int)]
	}).(DeduplicationRuleV2Output)
}

type DeduplicationRuleV2MapOutput struct{ *pulumi.OutputState }

func (DeduplicationRuleV2MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DeduplicationRuleV2)(nil)).Elem()
}

func (o DeduplicationRuleV2MapOutput) ToDeduplicationRuleV2MapOutput() DeduplicationRuleV2MapOutput {
	return o
}

func (o DeduplicationRuleV2MapOutput) ToDeduplicationRuleV2MapOutputWithContext(ctx context.Context) DeduplicationRuleV2MapOutput {
	return o
}

func (o DeduplicationRuleV2MapOutput) MapIndex(k pulumi.StringInput) DeduplicationRuleV2Output {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DeduplicationRuleV2 {
		return vs[0].(map[string]*DeduplicationRuleV2)[vs[1].(string)]
	}).(DeduplicationRuleV2Output)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeduplicationRuleV2Input)(nil)).Elem(), &DeduplicationRuleV2{})
	pulumi.RegisterInputType(reflect.TypeOf((*DeduplicationRuleV2ArrayInput)(nil)).Elem(), DeduplicationRuleV2Array{})
	pulumi.RegisterInputType(reflect.TypeOf((*DeduplicationRuleV2MapInput)(nil)).Elem(), DeduplicationRuleV2Map{})
	pulumi.RegisterOutputType(DeduplicationRuleV2Output{})
	pulumi.RegisterOutputType(DeduplicationRuleV2ArrayOutput{})
	pulumi.RegisterOutputType(DeduplicationRuleV2MapOutput{})
}
