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

// [Tagging](https://support.squadcast.com/docs/event-tagging) is a rule-based, auto-tagging system with which you can define customised tags based on incident payloads, that get automatically assigned to incidents when they are triggered.
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
//			exampleService, err := squadcast.LookupService(ctx, &squadcast.LookupServiceArgs{
//				Name:   "example service name",
//				TeamId: data.Squadcast_team.Example_team.Id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewTaggingRuleV2(ctx, "exampleTaggingRule", &squadcast.TaggingRuleV2Args{
//				ServiceId:  pulumi.String(exampleService.Id),
//				IsBasic:    pulumi.Bool(false),
//				Expression: pulumi.String("payload[\"event_id\"] == 40"),
//				Tags: squadcast.TaggingRuleV2TagArray{
//					&squadcast.TaggingRuleV2TagArgs{
//						Key:   pulumi.String("MyTag"),
//						Value: pulumi.String("foo"),
//						Color: pulumi.String("#ababab"),
//					},
//					&squadcast.TaggingRuleV2TagArgs{
//						Key:   pulumi.String("MyTag2"),
//						Value: pulumi.String("bar"),
//						Color: pulumi.String("#f0f0f0"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewTaggingRuleV2(ctx, "exampleBasicTaggingRule", &squadcast.TaggingRuleV2Args{
//				ServiceId: pulumi.String(exampleService.Id),
//				IsBasic:   pulumi.Bool(true),
//				BasicExpressions: squadcast.TaggingRuleV2BasicExpressionArray{
//					&squadcast.TaggingRuleV2BasicExpressionArgs{
//						Lhs: pulumi.String("payload[\"foo\"]"),
//						Op:  pulumi.String("is"),
//						Rhs: pulumi.String("bar"),
//					},
//				},
//				Tags: squadcast.TaggingRuleV2TagArray{
//					&squadcast.TaggingRuleV2TagArgs{
//						Key:   pulumi.String("MyTag"),
//						Value: pulumi.String("foo"),
//						Color: pulumi.String("#ababab"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			// addTags must be set in expression when tags are not passed
//			_, err = squadcast.NewTaggingRuleV2(ctx, "exampleTaggingRulesResourceWithouttags", &squadcast.TaggingRuleV2Args{
//				ServiceId:  pulumi.String(exampleService.Id),
//				IsBasic:    pulumi.Bool(false),
//				Expression: pulumi.String("addTag(\"EventType\", payload.details.event_type_key, \"#037916\")"),
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
// $ pulumi import squadcast:index/taggingRuleV2:TaggingRuleV2 test 62d2fe23a57381088224d726:62da76c088f407f9ca756ca5
// ```
type TaggingRuleV2 struct {
	pulumi.CustomResourceState

	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions TaggingRuleV2BasicExpressionArrayOutput `pulumi:"basicExpressions"`
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression pulumi.StringPtrOutput `pulumi:"expression"`
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic pulumi.BoolOutput `pulumi:"isBasic"`
	// Service id.
	ServiceId pulumi.StringOutput `pulumi:"serviceId"`
	// The tags supposed to be set for a given payload(incident), Expression must be set when tags are empty and must contain addTags parameters.
	Tags TaggingRuleV2TagArrayOutput `pulumi:"tags"`
}

// NewTaggingRuleV2 registers a new resource with the given unique name, arguments, and options.
func NewTaggingRuleV2(ctx *pulumi.Context,
	name string, args *TaggingRuleV2Args, opts ...pulumi.ResourceOption) (*TaggingRuleV2, error) {
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
	var resource TaggingRuleV2
	err := ctx.RegisterResource("squadcast:index/taggingRuleV2:TaggingRuleV2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTaggingRuleV2 gets an existing TaggingRuleV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTaggingRuleV2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TaggingRuleV2State, opts ...pulumi.ResourceOption) (*TaggingRuleV2, error) {
	var resource TaggingRuleV2
	err := ctx.ReadResource("squadcast:index/taggingRuleV2:TaggingRuleV2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TaggingRuleV2 resources.
type taggingRuleV2State struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions []TaggingRuleV2BasicExpression `pulumi:"basicExpressions"`
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression *string `pulumi:"expression"`
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic *bool `pulumi:"isBasic"`
	// Service id.
	ServiceId *string `pulumi:"serviceId"`
	// The tags supposed to be set for a given payload(incident), Expression must be set when tags are empty and must contain addTags parameters.
	Tags []TaggingRuleV2Tag `pulumi:"tags"`
}

type TaggingRuleV2State struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions TaggingRuleV2BasicExpressionArrayInput
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression pulumi.StringPtrInput
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic pulumi.BoolPtrInput
	// Service id.
	ServiceId pulumi.StringPtrInput
	// The tags supposed to be set for a given payload(incident), Expression must be set when tags are empty and must contain addTags parameters.
	Tags TaggingRuleV2TagArrayInput
}

func (TaggingRuleV2State) ElementType() reflect.Type {
	return reflect.TypeOf((*taggingRuleV2State)(nil)).Elem()
}

type taggingRuleV2Args struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions []TaggingRuleV2BasicExpression `pulumi:"basicExpressions"`
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression *string `pulumi:"expression"`
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic bool `pulumi:"isBasic"`
	// Service id.
	ServiceId string `pulumi:"serviceId"`
	// The tags supposed to be set for a given payload(incident), Expression must be set when tags are empty and must contain addTags parameters.
	Tags []TaggingRuleV2Tag `pulumi:"tags"`
}

// The set of arguments for constructing a TaggingRuleV2 resource.
type TaggingRuleV2Args struct {
	// The basic expression which needs to be evaluated to be true for this rule to apply.
	BasicExpressions TaggingRuleV2BasicExpressionArrayInput
	// The expression which needs to be evaluated to be true for this rule to apply.
	Expression pulumi.StringPtrInput
	// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
	IsBasic pulumi.BoolInput
	// Service id.
	ServiceId pulumi.StringInput
	// The tags supposed to be set for a given payload(incident), Expression must be set when tags are empty and must contain addTags parameters.
	Tags TaggingRuleV2TagArrayInput
}

func (TaggingRuleV2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*taggingRuleV2Args)(nil)).Elem()
}

type TaggingRuleV2Input interface {
	pulumi.Input

	ToTaggingRuleV2Output() TaggingRuleV2Output
	ToTaggingRuleV2OutputWithContext(ctx context.Context) TaggingRuleV2Output
}

func (*TaggingRuleV2) ElementType() reflect.Type {
	return reflect.TypeOf((**TaggingRuleV2)(nil)).Elem()
}

func (i *TaggingRuleV2) ToTaggingRuleV2Output() TaggingRuleV2Output {
	return i.ToTaggingRuleV2OutputWithContext(context.Background())
}

func (i *TaggingRuleV2) ToTaggingRuleV2OutputWithContext(ctx context.Context) TaggingRuleV2Output {
	return pulumi.ToOutputWithContext(ctx, i).(TaggingRuleV2Output)
}

// TaggingRuleV2ArrayInput is an input type that accepts TaggingRuleV2Array and TaggingRuleV2ArrayOutput values.
// You can construct a concrete instance of `TaggingRuleV2ArrayInput` via:
//
//	TaggingRuleV2Array{ TaggingRuleV2Args{...} }
type TaggingRuleV2ArrayInput interface {
	pulumi.Input

	ToTaggingRuleV2ArrayOutput() TaggingRuleV2ArrayOutput
	ToTaggingRuleV2ArrayOutputWithContext(context.Context) TaggingRuleV2ArrayOutput
}

type TaggingRuleV2Array []TaggingRuleV2Input

func (TaggingRuleV2Array) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TaggingRuleV2)(nil)).Elem()
}

func (i TaggingRuleV2Array) ToTaggingRuleV2ArrayOutput() TaggingRuleV2ArrayOutput {
	return i.ToTaggingRuleV2ArrayOutputWithContext(context.Background())
}

func (i TaggingRuleV2Array) ToTaggingRuleV2ArrayOutputWithContext(ctx context.Context) TaggingRuleV2ArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TaggingRuleV2ArrayOutput)
}

// TaggingRuleV2MapInput is an input type that accepts TaggingRuleV2Map and TaggingRuleV2MapOutput values.
// You can construct a concrete instance of `TaggingRuleV2MapInput` via:
//
//	TaggingRuleV2Map{ "key": TaggingRuleV2Args{...} }
type TaggingRuleV2MapInput interface {
	pulumi.Input

	ToTaggingRuleV2MapOutput() TaggingRuleV2MapOutput
	ToTaggingRuleV2MapOutputWithContext(context.Context) TaggingRuleV2MapOutput
}

type TaggingRuleV2Map map[string]TaggingRuleV2Input

func (TaggingRuleV2Map) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TaggingRuleV2)(nil)).Elem()
}

func (i TaggingRuleV2Map) ToTaggingRuleV2MapOutput() TaggingRuleV2MapOutput {
	return i.ToTaggingRuleV2MapOutputWithContext(context.Background())
}

func (i TaggingRuleV2Map) ToTaggingRuleV2MapOutputWithContext(ctx context.Context) TaggingRuleV2MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TaggingRuleV2MapOutput)
}

type TaggingRuleV2Output struct{ *pulumi.OutputState }

func (TaggingRuleV2Output) ElementType() reflect.Type {
	return reflect.TypeOf((**TaggingRuleV2)(nil)).Elem()
}

func (o TaggingRuleV2Output) ToTaggingRuleV2Output() TaggingRuleV2Output {
	return o
}

func (o TaggingRuleV2Output) ToTaggingRuleV2OutputWithContext(ctx context.Context) TaggingRuleV2Output {
	return o
}

// The basic expression which needs to be evaluated to be true for this rule to apply.
func (o TaggingRuleV2Output) BasicExpressions() TaggingRuleV2BasicExpressionArrayOutput {
	return o.ApplyT(func(v *TaggingRuleV2) TaggingRuleV2BasicExpressionArrayOutput { return v.BasicExpressions }).(TaggingRuleV2BasicExpressionArrayOutput)
}

// The expression which needs to be evaluated to be true for this rule to apply.
func (o TaggingRuleV2Output) Expression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TaggingRuleV2) pulumi.StringPtrOutput { return v.Expression }).(pulumi.StringPtrOutput)
}

// is_basic will be true when users use the drop down selectors which will have lhs, op & rhs value, whereas it will be false when they use the advanced mode and it would have the expression for it's value
func (o TaggingRuleV2Output) IsBasic() pulumi.BoolOutput {
	return o.ApplyT(func(v *TaggingRuleV2) pulumi.BoolOutput { return v.IsBasic }).(pulumi.BoolOutput)
}

// Service id.
func (o TaggingRuleV2Output) ServiceId() pulumi.StringOutput {
	return o.ApplyT(func(v *TaggingRuleV2) pulumi.StringOutput { return v.ServiceId }).(pulumi.StringOutput)
}

// The tags supposed to be set for a given payload(incident), Expression must be set when tags are empty and must contain addTags parameters.
func (o TaggingRuleV2Output) Tags() TaggingRuleV2TagArrayOutput {
	return o.ApplyT(func(v *TaggingRuleV2) TaggingRuleV2TagArrayOutput { return v.Tags }).(TaggingRuleV2TagArrayOutput)
}

type TaggingRuleV2ArrayOutput struct{ *pulumi.OutputState }

func (TaggingRuleV2ArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TaggingRuleV2)(nil)).Elem()
}

func (o TaggingRuleV2ArrayOutput) ToTaggingRuleV2ArrayOutput() TaggingRuleV2ArrayOutput {
	return o
}

func (o TaggingRuleV2ArrayOutput) ToTaggingRuleV2ArrayOutputWithContext(ctx context.Context) TaggingRuleV2ArrayOutput {
	return o
}

func (o TaggingRuleV2ArrayOutput) Index(i pulumi.IntInput) TaggingRuleV2Output {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TaggingRuleV2 {
		return vs[0].([]*TaggingRuleV2)[vs[1].(int)]
	}).(TaggingRuleV2Output)
}

type TaggingRuleV2MapOutput struct{ *pulumi.OutputState }

func (TaggingRuleV2MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TaggingRuleV2)(nil)).Elem()
}

func (o TaggingRuleV2MapOutput) ToTaggingRuleV2MapOutput() TaggingRuleV2MapOutput {
	return o
}

func (o TaggingRuleV2MapOutput) ToTaggingRuleV2MapOutputWithContext(ctx context.Context) TaggingRuleV2MapOutput {
	return o
}

func (o TaggingRuleV2MapOutput) MapIndex(k pulumi.StringInput) TaggingRuleV2Output {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TaggingRuleV2 {
		return vs[0].(map[string]*TaggingRuleV2)[vs[1].(string)]
	}).(TaggingRuleV2Output)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TaggingRuleV2Input)(nil)).Elem(), &TaggingRuleV2{})
	pulumi.RegisterInputType(reflect.TypeOf((*TaggingRuleV2ArrayInput)(nil)).Elem(), TaggingRuleV2Array{})
	pulumi.RegisterInputType(reflect.TypeOf((*TaggingRuleV2MapInput)(nil)).Elem(), TaggingRuleV2Map{})
	pulumi.RegisterOutputType(TaggingRuleV2Output{})
	pulumi.RegisterOutputType(TaggingRuleV2ArrayOutput{})
	pulumi.RegisterOutputType(TaggingRuleV2MapOutput{})
}
