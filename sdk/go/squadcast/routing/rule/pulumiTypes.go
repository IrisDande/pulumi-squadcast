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

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*V2BasicExpressionInput)(nil)).Elem(), V2BasicExpressionArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*V2BasicExpressionArrayInput)(nil)).Elem(), V2BasicExpressionArray{})
	pulumi.RegisterOutputType(V2BasicExpressionOutput{})
	pulumi.RegisterOutputType(V2BasicExpressionArrayOutput{})
}
