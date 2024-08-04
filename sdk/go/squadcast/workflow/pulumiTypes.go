// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package workflow

import (
	"context"
	"reflect"

	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type ActionChannel struct {
	// The display text of the communication channel
	DisplayText string `pulumi:"displayText"`
	// The link of the communication channel
	Link string `pulumi:"link"`
	// The type of the communication channel
	Type string `pulumi:"type"`
}

// ActionChannelInput is an input type that accepts ActionChannelArgs and ActionChannelOutput values.
// You can construct a concrete instance of `ActionChannelInput` via:
//
//	ActionChannelArgs{...}
type ActionChannelInput interface {
	pulumi.Input

	ToActionChannelOutput() ActionChannelOutput
	ToActionChannelOutputWithContext(context.Context) ActionChannelOutput
}

type ActionChannelArgs struct {
	// The display text of the communication channel
	DisplayText pulumi.StringInput `pulumi:"displayText"`
	// The link of the communication channel
	Link pulumi.StringInput `pulumi:"link"`
	// The type of the communication channel
	Type pulumi.StringInput `pulumi:"type"`
}

func (ActionChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionChannel)(nil)).Elem()
}

func (i ActionChannelArgs) ToActionChannelOutput() ActionChannelOutput {
	return i.ToActionChannelOutputWithContext(context.Background())
}

func (i ActionChannelArgs) ToActionChannelOutputWithContext(ctx context.Context) ActionChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionChannelOutput)
}

// ActionChannelArrayInput is an input type that accepts ActionChannelArray and ActionChannelArrayOutput values.
// You can construct a concrete instance of `ActionChannelArrayInput` via:
//
//	ActionChannelArray{ ActionChannelArgs{...} }
type ActionChannelArrayInput interface {
	pulumi.Input

	ToActionChannelArrayOutput() ActionChannelArrayOutput
	ToActionChannelArrayOutputWithContext(context.Context) ActionChannelArrayOutput
}

type ActionChannelArray []ActionChannelInput

func (ActionChannelArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionChannel)(nil)).Elem()
}

func (i ActionChannelArray) ToActionChannelArrayOutput() ActionChannelArrayOutput {
	return i.ToActionChannelArrayOutputWithContext(context.Background())
}

func (i ActionChannelArray) ToActionChannelArrayOutputWithContext(ctx context.Context) ActionChannelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionChannelArrayOutput)
}

type ActionChannelOutput struct{ *pulumi.OutputState }

func (ActionChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionChannel)(nil)).Elem()
}

func (o ActionChannelOutput) ToActionChannelOutput() ActionChannelOutput {
	return o
}

func (o ActionChannelOutput) ToActionChannelOutputWithContext(ctx context.Context) ActionChannelOutput {
	return o
}

// The display text of the communication channel
func (o ActionChannelOutput) DisplayText() pulumi.StringOutput {
	return o.ApplyT(func(v ActionChannel) string { return v.DisplayText }).(pulumi.StringOutput)
}

// The link of the communication channel
func (o ActionChannelOutput) Link() pulumi.StringOutput {
	return o.ApplyT(func(v ActionChannel) string { return v.Link }).(pulumi.StringOutput)
}

// The type of the communication channel
func (o ActionChannelOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v ActionChannel) string { return v.Type }).(pulumi.StringOutput)
}

type ActionChannelArrayOutput struct{ *pulumi.OutputState }

func (ActionChannelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionChannel)(nil)).Elem()
}

func (o ActionChannelArrayOutput) ToActionChannelArrayOutput() ActionChannelArrayOutput {
	return o
}

func (o ActionChannelArrayOutput) ToActionChannelArrayOutputWithContext(ctx context.Context) ActionChannelArrayOutput {
	return o
}

func (o ActionChannelArrayOutput) Index(i pulumi.IntInput) ActionChannelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ActionChannel {
		return vs[0].([]ActionChannel)[vs[1].(int)]
	}).(ActionChannelOutput)
}

type ActionComponentAndImpact struct {
	// The ID of the component
	ComponentId int `pulumi:"componentId"`
	// The ID of the impact status
	ImpactStatusId int `pulumi:"impactStatusId"`
}

// ActionComponentAndImpactInput is an input type that accepts ActionComponentAndImpactArgs and ActionComponentAndImpactOutput values.
// You can construct a concrete instance of `ActionComponentAndImpactInput` via:
//
//	ActionComponentAndImpactArgs{...}
type ActionComponentAndImpactInput interface {
	pulumi.Input

	ToActionComponentAndImpactOutput() ActionComponentAndImpactOutput
	ToActionComponentAndImpactOutputWithContext(context.Context) ActionComponentAndImpactOutput
}

type ActionComponentAndImpactArgs struct {
	// The ID of the component
	ComponentId pulumi.IntInput `pulumi:"componentId"`
	// The ID of the impact status
	ImpactStatusId pulumi.IntInput `pulumi:"impactStatusId"`
}

func (ActionComponentAndImpactArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionComponentAndImpact)(nil)).Elem()
}

func (i ActionComponentAndImpactArgs) ToActionComponentAndImpactOutput() ActionComponentAndImpactOutput {
	return i.ToActionComponentAndImpactOutputWithContext(context.Background())
}

func (i ActionComponentAndImpactArgs) ToActionComponentAndImpactOutputWithContext(ctx context.Context) ActionComponentAndImpactOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionComponentAndImpactOutput)
}

// ActionComponentAndImpactArrayInput is an input type that accepts ActionComponentAndImpactArray and ActionComponentAndImpactArrayOutput values.
// You can construct a concrete instance of `ActionComponentAndImpactArrayInput` via:
//
//	ActionComponentAndImpactArray{ ActionComponentAndImpactArgs{...} }
type ActionComponentAndImpactArrayInput interface {
	pulumi.Input

	ToActionComponentAndImpactArrayOutput() ActionComponentAndImpactArrayOutput
	ToActionComponentAndImpactArrayOutputWithContext(context.Context) ActionComponentAndImpactArrayOutput
}

type ActionComponentAndImpactArray []ActionComponentAndImpactInput

func (ActionComponentAndImpactArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionComponentAndImpact)(nil)).Elem()
}

func (i ActionComponentAndImpactArray) ToActionComponentAndImpactArrayOutput() ActionComponentAndImpactArrayOutput {
	return i.ToActionComponentAndImpactArrayOutputWithContext(context.Background())
}

func (i ActionComponentAndImpactArray) ToActionComponentAndImpactArrayOutputWithContext(ctx context.Context) ActionComponentAndImpactArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionComponentAndImpactArrayOutput)
}

type ActionComponentAndImpactOutput struct{ *pulumi.OutputState }

func (ActionComponentAndImpactOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionComponentAndImpact)(nil)).Elem()
}

func (o ActionComponentAndImpactOutput) ToActionComponentAndImpactOutput() ActionComponentAndImpactOutput {
	return o
}

func (o ActionComponentAndImpactOutput) ToActionComponentAndImpactOutputWithContext(ctx context.Context) ActionComponentAndImpactOutput {
	return o
}

// The ID of the component
func (o ActionComponentAndImpactOutput) ComponentId() pulumi.IntOutput {
	return o.ApplyT(func(v ActionComponentAndImpact) int { return v.ComponentId }).(pulumi.IntOutput)
}

// The ID of the impact status
func (o ActionComponentAndImpactOutput) ImpactStatusId() pulumi.IntOutput {
	return o.ApplyT(func(v ActionComponentAndImpact) int { return v.ImpactStatusId }).(pulumi.IntOutput)
}

type ActionComponentAndImpactArrayOutput struct{ *pulumi.OutputState }

func (ActionComponentAndImpactArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionComponentAndImpact)(nil)).Elem()
}

func (o ActionComponentAndImpactArrayOutput) ToActionComponentAndImpactArrayOutput() ActionComponentAndImpactArrayOutput {
	return o
}

func (o ActionComponentAndImpactArrayOutput) ToActionComponentAndImpactArrayOutputWithContext(ctx context.Context) ActionComponentAndImpactArrayOutput {
	return o
}

func (o ActionComponentAndImpactArrayOutput) Index(i pulumi.IntInput) ActionComponentAndImpactOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ActionComponentAndImpact {
		return vs[0].([]ActionComponentAndImpact)[vs[1].(int)]
	}).(ActionComponentAndImpactOutput)
}

type ActionHeader struct {
	// The key of the header
	Key string `pulumi:"key"`
	// The value of the header
	Value string `pulumi:"value"`
}

// ActionHeaderInput is an input type that accepts ActionHeaderArgs and ActionHeaderOutput values.
// You can construct a concrete instance of `ActionHeaderInput` via:
//
//	ActionHeaderArgs{...}
type ActionHeaderInput interface {
	pulumi.Input

	ToActionHeaderOutput() ActionHeaderOutput
	ToActionHeaderOutputWithContext(context.Context) ActionHeaderOutput
}

type ActionHeaderArgs struct {
	// The key of the header
	Key pulumi.StringInput `pulumi:"key"`
	// The value of the header
	Value pulumi.StringInput `pulumi:"value"`
}

func (ActionHeaderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionHeader)(nil)).Elem()
}

func (i ActionHeaderArgs) ToActionHeaderOutput() ActionHeaderOutput {
	return i.ToActionHeaderOutputWithContext(context.Background())
}

func (i ActionHeaderArgs) ToActionHeaderOutputWithContext(ctx context.Context) ActionHeaderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionHeaderOutput)
}

// ActionHeaderArrayInput is an input type that accepts ActionHeaderArray and ActionHeaderArrayOutput values.
// You can construct a concrete instance of `ActionHeaderArrayInput` via:
//
//	ActionHeaderArray{ ActionHeaderArgs{...} }
type ActionHeaderArrayInput interface {
	pulumi.Input

	ToActionHeaderArrayOutput() ActionHeaderArrayOutput
	ToActionHeaderArrayOutputWithContext(context.Context) ActionHeaderArrayOutput
}

type ActionHeaderArray []ActionHeaderInput

func (ActionHeaderArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionHeader)(nil)).Elem()
}

func (i ActionHeaderArray) ToActionHeaderArrayOutput() ActionHeaderArrayOutput {
	return i.ToActionHeaderArrayOutputWithContext(context.Background())
}

func (i ActionHeaderArray) ToActionHeaderArrayOutputWithContext(ctx context.Context) ActionHeaderArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionHeaderArrayOutput)
}

type ActionHeaderOutput struct{ *pulumi.OutputState }

func (ActionHeaderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionHeader)(nil)).Elem()
}

func (o ActionHeaderOutput) ToActionHeaderOutput() ActionHeaderOutput {
	return o
}

func (o ActionHeaderOutput) ToActionHeaderOutputWithContext(ctx context.Context) ActionHeaderOutput {
	return o
}

// The key of the header
func (o ActionHeaderOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ActionHeader) string { return v.Key }).(pulumi.StringOutput)
}

// The value of the header
func (o ActionHeaderOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ActionHeader) string { return v.Value }).(pulumi.StringOutput)
}

type ActionHeaderArrayOutput struct{ *pulumi.OutputState }

func (ActionHeaderArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionHeader)(nil)).Elem()
}

func (o ActionHeaderArrayOutput) ToActionHeaderArrayOutput() ActionHeaderArrayOutput {
	return o
}

func (o ActionHeaderArrayOutput) ToActionHeaderArrayOutputWithContext(ctx context.Context) ActionHeaderArrayOutput {
	return o
}

func (o ActionHeaderArrayOutput) Index(i pulumi.IntInput) ActionHeaderOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ActionHeader {
		return vs[0].([]ActionHeader)[vs[1].(int)]
	}).(ActionHeaderOutput)
}

type ActionStatusAndMessage struct {
	// The messages to be set for the issue
	Messages []string `pulumi:"messages"`
	// The ID of the status
	StatusId int `pulumi:"statusId"`
}

// ActionStatusAndMessageInput is an input type that accepts ActionStatusAndMessageArgs and ActionStatusAndMessageOutput values.
// You can construct a concrete instance of `ActionStatusAndMessageInput` via:
//
//	ActionStatusAndMessageArgs{...}
type ActionStatusAndMessageInput interface {
	pulumi.Input

	ToActionStatusAndMessageOutput() ActionStatusAndMessageOutput
	ToActionStatusAndMessageOutputWithContext(context.Context) ActionStatusAndMessageOutput
}

type ActionStatusAndMessageArgs struct {
	// The messages to be set for the issue
	Messages pulumi.StringArrayInput `pulumi:"messages"`
	// The ID of the status
	StatusId pulumi.IntInput `pulumi:"statusId"`
}

func (ActionStatusAndMessageArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionStatusAndMessage)(nil)).Elem()
}

func (i ActionStatusAndMessageArgs) ToActionStatusAndMessageOutput() ActionStatusAndMessageOutput {
	return i.ToActionStatusAndMessageOutputWithContext(context.Background())
}

func (i ActionStatusAndMessageArgs) ToActionStatusAndMessageOutputWithContext(ctx context.Context) ActionStatusAndMessageOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionStatusAndMessageOutput)
}

// ActionStatusAndMessageArrayInput is an input type that accepts ActionStatusAndMessageArray and ActionStatusAndMessageArrayOutput values.
// You can construct a concrete instance of `ActionStatusAndMessageArrayInput` via:
//
//	ActionStatusAndMessageArray{ ActionStatusAndMessageArgs{...} }
type ActionStatusAndMessageArrayInput interface {
	pulumi.Input

	ToActionStatusAndMessageArrayOutput() ActionStatusAndMessageArrayOutput
	ToActionStatusAndMessageArrayOutputWithContext(context.Context) ActionStatusAndMessageArrayOutput
}

type ActionStatusAndMessageArray []ActionStatusAndMessageInput

func (ActionStatusAndMessageArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionStatusAndMessage)(nil)).Elem()
}

func (i ActionStatusAndMessageArray) ToActionStatusAndMessageArrayOutput() ActionStatusAndMessageArrayOutput {
	return i.ToActionStatusAndMessageArrayOutputWithContext(context.Background())
}

func (i ActionStatusAndMessageArray) ToActionStatusAndMessageArrayOutputWithContext(ctx context.Context) ActionStatusAndMessageArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ActionStatusAndMessageArrayOutput)
}

type ActionStatusAndMessageOutput struct{ *pulumi.OutputState }

func (ActionStatusAndMessageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ActionStatusAndMessage)(nil)).Elem()
}

func (o ActionStatusAndMessageOutput) ToActionStatusAndMessageOutput() ActionStatusAndMessageOutput {
	return o
}

func (o ActionStatusAndMessageOutput) ToActionStatusAndMessageOutputWithContext(ctx context.Context) ActionStatusAndMessageOutput {
	return o
}

// The messages to be set for the issue
func (o ActionStatusAndMessageOutput) Messages() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ActionStatusAndMessage) []string { return v.Messages }).(pulumi.StringArrayOutput)
}

// The ID of the status
func (o ActionStatusAndMessageOutput) StatusId() pulumi.IntOutput {
	return o.ApplyT(func(v ActionStatusAndMessage) int { return v.StatusId }).(pulumi.IntOutput)
}

type ActionStatusAndMessageArrayOutput struct{ *pulumi.OutputState }

func (ActionStatusAndMessageArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ActionStatusAndMessage)(nil)).Elem()
}

func (o ActionStatusAndMessageArrayOutput) ToActionStatusAndMessageArrayOutput() ActionStatusAndMessageArrayOutput {
	return o
}

func (o ActionStatusAndMessageArrayOutput) ToActionStatusAndMessageArrayOutputWithContext(ctx context.Context) ActionStatusAndMessageArrayOutput {
	return o
}

func (o ActionStatusAndMessageArrayOutput) Index(i pulumi.IntInput) ActionStatusAndMessageOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ActionStatusAndMessage {
		return vs[0].([]ActionStatusAndMessage)[vs[1].(int)]
	}).(ActionStatusAndMessageOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ActionChannelInput)(nil)).Elem(), ActionChannelArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionChannelArrayInput)(nil)).Elem(), ActionChannelArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionComponentAndImpactInput)(nil)).Elem(), ActionComponentAndImpactArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionComponentAndImpactArrayInput)(nil)).Elem(), ActionComponentAndImpactArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionHeaderInput)(nil)).Elem(), ActionHeaderArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionHeaderArrayInput)(nil)).Elem(), ActionHeaderArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionStatusAndMessageInput)(nil)).Elem(), ActionStatusAndMessageArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ActionStatusAndMessageArrayInput)(nil)).Elem(), ActionStatusAndMessageArray{})
	pulumi.RegisterOutputType(ActionChannelOutput{})
	pulumi.RegisterOutputType(ActionChannelArrayOutput{})
	pulumi.RegisterOutputType(ActionComponentAndImpactOutput{})
	pulumi.RegisterOutputType(ActionComponentAndImpactArrayOutput{})
	pulumi.RegisterOutputType(ActionHeaderOutput{})
	pulumi.RegisterOutputType(ActionHeaderArrayOutput{})
	pulumi.RegisterOutputType(ActionStatusAndMessageOutput{})
	pulumi.RegisterOutputType(ActionStatusAndMessageArrayOutput{})
}
