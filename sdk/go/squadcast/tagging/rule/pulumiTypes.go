// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rule

import (
	"context"
	"reflect"

	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type V2BasicExpression struct {
	// left hand side dropdown value
	Lhs string `pulumi:"lhs"`
	// operator (is, is*not, matches, not*contains)
	Op string `pulumi:"op"`
	// right hand side value
	Rhs string `pulumi:"rhs"`
}

// V2BasicExpressionInput is an input type that accepts V2BasicExpressionArgs and V2BasicExpressionOutput values.
// You can construct a concrete instance of `V2BasicExpressionInput` via:
//
//	V2BasicExpressionArgs{...}
type V2BasicExpressionInput interface {
	pulumi.Input

	ToV2BasicExpressionOutput() V2BasicExpressionOutput
	ToV2BasicExpressionOutputWithContext(context.Context) V2BasicExpressionOutput
}

type V2BasicExpressionArgs struct {
	// left hand side dropdown value
	Lhs pulumi.StringInput `pulumi:"lhs"`
	// operator (is, is*not, matches, not*contains)
	Op pulumi.StringInput `pulumi:"op"`
	// right hand side value
	Rhs pulumi.StringInput `pulumi:"rhs"`
}

func (V2BasicExpressionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*V2BasicExpression)(nil)).Elem()
}

func (i V2BasicExpressionArgs) ToV2BasicExpressionOutput() V2BasicExpressionOutput {
	return i.ToV2BasicExpressionOutputWithContext(context.Background())
}

func (i V2BasicExpressionArgs) ToV2BasicExpressionOutputWithContext(ctx context.Context) V2BasicExpressionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(V2BasicExpressionOutput)
}

// V2BasicExpressionArrayInput is an input type that accepts V2BasicExpressionArray and V2BasicExpressionArrayOutput values.
// You can construct a concrete instance of `V2BasicExpressionArrayInput` via:
//
//	V2BasicExpressionArray{ V2BasicExpressionArgs{...} }
type V2BasicExpressionArrayInput interface {
	pulumi.Input

	ToV2BasicExpressionArrayOutput() V2BasicExpressionArrayOutput
	ToV2BasicExpressionArrayOutputWithContext(context.Context) V2BasicExpressionArrayOutput
}

type V2BasicExpressionArray []V2BasicExpressionInput

func (V2BasicExpressionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]V2BasicExpression)(nil)).Elem()
}

func (i V2BasicExpressionArray) ToV2BasicExpressionArrayOutput() V2BasicExpressionArrayOutput {
	return i.ToV2BasicExpressionArrayOutputWithContext(context.Background())
}

func (i V2BasicExpressionArray) ToV2BasicExpressionArrayOutputWithContext(ctx context.Context) V2BasicExpressionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(V2BasicExpressionArrayOutput)
}

type V2BasicExpressionOutput struct{ *pulumi.OutputState }

func (V2BasicExpressionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*V2BasicExpression)(nil)).Elem()
}

func (o V2BasicExpressionOutput) ToV2BasicExpressionOutput() V2BasicExpressionOutput {
	return o
}

func (o V2BasicExpressionOutput) ToV2BasicExpressionOutputWithContext(ctx context.Context) V2BasicExpressionOutput {
	return o
}

// left hand side dropdown value
func (o V2BasicExpressionOutput) Lhs() pulumi.StringOutput {
	return o.ApplyT(func(v V2BasicExpression) string { return v.Lhs }).(pulumi.StringOutput)
}

// operator (is, is*not, matches, not*contains)
func (o V2BasicExpressionOutput) Op() pulumi.StringOutput {
	return o.ApplyT(func(v V2BasicExpression) string { return v.Op }).(pulumi.StringOutput)
}

// right hand side value
func (o V2BasicExpressionOutput) Rhs() pulumi.StringOutput {
	return o.ApplyT(func(v V2BasicExpression) string { return v.Rhs }).(pulumi.StringOutput)
}

type V2BasicExpressionArrayOutput struct{ *pulumi.OutputState }

func (V2BasicExpressionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]V2BasicExpression)(nil)).Elem()
}

func (o V2BasicExpressionArrayOutput) ToV2BasicExpressionArrayOutput() V2BasicExpressionArrayOutput {
	return o
}

func (o V2BasicExpressionArrayOutput) ToV2BasicExpressionArrayOutputWithContext(ctx context.Context) V2BasicExpressionArrayOutput {
	return o
}

func (o V2BasicExpressionArrayOutput) Index(i pulumi.IntInput) V2BasicExpressionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) V2BasicExpression {
		return vs[0].([]V2BasicExpression)[vs[1].(int)]
	}).(V2BasicExpressionOutput)
}

type V2Tag struct {
	// Tag color, hex values
	Color string `pulumi:"color"`
	// key
	Key string `pulumi:"key"`
	// value
	Value string `pulumi:"value"`
}

// V2TagInput is an input type that accepts V2TagArgs and V2TagOutput values.
// You can construct a concrete instance of `V2TagInput` via:
//
//	V2TagArgs{...}
type V2TagInput interface {
	pulumi.Input

	ToV2TagOutput() V2TagOutput
	ToV2TagOutputWithContext(context.Context) V2TagOutput
}

type V2TagArgs struct {
	// Tag color, hex values
	Color pulumi.StringInput `pulumi:"color"`
	// key
	Key pulumi.StringInput `pulumi:"key"`
	// value
	Value pulumi.StringInput `pulumi:"value"`
}

func (V2TagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*V2Tag)(nil)).Elem()
}

func (i V2TagArgs) ToV2TagOutput() V2TagOutput {
	return i.ToV2TagOutputWithContext(context.Background())
}

func (i V2TagArgs) ToV2TagOutputWithContext(ctx context.Context) V2TagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(V2TagOutput)
}

// V2TagArrayInput is an input type that accepts V2TagArray and V2TagArrayOutput values.
// You can construct a concrete instance of `V2TagArrayInput` via:
//
//	V2TagArray{ V2TagArgs{...} }
type V2TagArrayInput interface {
	pulumi.Input

	ToV2TagArrayOutput() V2TagArrayOutput
	ToV2TagArrayOutputWithContext(context.Context) V2TagArrayOutput
}

type V2TagArray []V2TagInput

func (V2TagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]V2Tag)(nil)).Elem()
}

func (i V2TagArray) ToV2TagArrayOutput() V2TagArrayOutput {
	return i.ToV2TagArrayOutputWithContext(context.Background())
}

func (i V2TagArray) ToV2TagArrayOutputWithContext(ctx context.Context) V2TagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(V2TagArrayOutput)
}

type V2TagOutput struct{ *pulumi.OutputState }

func (V2TagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*V2Tag)(nil)).Elem()
}

func (o V2TagOutput) ToV2TagOutput() V2TagOutput {
	return o
}

func (o V2TagOutput) ToV2TagOutputWithContext(ctx context.Context) V2TagOutput {
	return o
}

// Tag color, hex values
func (o V2TagOutput) Color() pulumi.StringOutput {
	return o.ApplyT(func(v V2Tag) string { return v.Color }).(pulumi.StringOutput)
}

// key
func (o V2TagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v V2Tag) string { return v.Key }).(pulumi.StringOutput)
}

// value
func (o V2TagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v V2Tag) string { return v.Value }).(pulumi.StringOutput)
}

type V2TagArrayOutput struct{ *pulumi.OutputState }

func (V2TagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]V2Tag)(nil)).Elem()
}

func (o V2TagArrayOutput) ToV2TagArrayOutput() V2TagArrayOutput {
	return o
}

func (o V2TagArrayOutput) ToV2TagArrayOutputWithContext(ctx context.Context) V2TagArrayOutput {
	return o
}

func (o V2TagArrayOutput) Index(i pulumi.IntInput) V2TagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) V2Tag {
		return vs[0].([]V2Tag)[vs[1].(int)]
	}).(V2TagOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*V2BasicExpressionInput)(nil)).Elem(), V2BasicExpressionArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*V2BasicExpressionArrayInput)(nil)).Elem(), V2BasicExpressionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*V2TagInput)(nil)).Elem(), V2TagArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*V2TagArrayInput)(nil)).Elem(), V2TagArray{})
	pulumi.RegisterOutputType(V2BasicExpressionOutput{})
	pulumi.RegisterOutputType(V2BasicExpressionArrayOutput{})
	pulumi.RegisterOutputType(V2TagOutput{})
	pulumi.RegisterOutputType(V2TagArrayOutput{})
}
