// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package escalation

import (
	"context"
	"reflect"

	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// [Escalation Policies](https://support.squadcast.com/docs/escalation-policies) defines rules indicating when and how alerts will escalate to various Users, Squads and (or) Schedules within your Organization.Use this data source to get information about a specific escalation policy that you can use for other Squadcast resources.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast/escalation"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := escalation.LookupPolicy(ctx, &escalation.LookupPolicyArgs{
//				Name:   squadcast_escalation_policy.Test.Name,
//				TeamId: "team id",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupPolicy(ctx *pulumi.Context, args *LookupPolicyArgs, opts ...pulumi.InvokeOption) (*LookupPolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPolicyResult
	err := ctx.Invoke("squadcast:escalation/getPolicy:getPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPolicy.
type LookupPolicyArgs struct {
	// Name of the Escalation Policy
	Name string `pulumi:"name"`
	// Team id.
	TeamId string `pulumi:"teamId"`
}

// A collection of values returned by getPolicy.
type LookupPolicyResult struct {
	// Detailed description about the nature & purpose Escalation policy
	Description string `pulumi:"description"`
	// Escalation policy owner
	EntityOwners []GetPolicyEntityOwner `pulumi:"entityOwners"`
	// Escalation Policy id.
	Id string `pulumi:"id"`
	// Name of the Escalation Policy
	Name string `pulumi:"name"`
	// You can choose to repeat the entire policy, if no one acknowledges the incident even after the Escalation Policy has been executed fully once
	Repeats []GetPolicyRepeat `pulumi:"repeats"`
	// Rules will have the details of who to notify and when to notify and how to notify them.
	Rules []GetPolicyRule `pulumi:"rules"`
	// Team id.
	TeamId string `pulumi:"teamId"`
}

func LookupPolicyOutput(ctx *pulumi.Context, args LookupPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPolicyResult, error) {
			args := v.(LookupPolicyArgs)
			r, err := LookupPolicy(ctx, &args, opts...)
			var s LookupPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPolicyResultOutput)
}

// A collection of arguments for invoking getPolicy.
type LookupPolicyOutputArgs struct {
	// Name of the Escalation Policy
	Name pulumi.StringInput `pulumi:"name"`
	// Team id.
	TeamId pulumi.StringInput `pulumi:"teamId"`
}

func (LookupPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPolicyArgs)(nil)).Elem()
}

// A collection of values returned by getPolicy.
type LookupPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPolicyResult)(nil)).Elem()
}

func (o LookupPolicyResultOutput) ToLookupPolicyResultOutput() LookupPolicyResultOutput {
	return o
}

func (o LookupPolicyResultOutput) ToLookupPolicyResultOutputWithContext(ctx context.Context) LookupPolicyResultOutput {
	return o
}

// Detailed description about the nature & purpose Escalation policy
func (o LookupPolicyResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPolicyResult) string { return v.Description }).(pulumi.StringOutput)
}

// Escalation policy owner
func (o LookupPolicyResultOutput) EntityOwners() GetPolicyEntityOwnerArrayOutput {
	return o.ApplyT(func(v LookupPolicyResult) []GetPolicyEntityOwner { return v.EntityOwners }).(GetPolicyEntityOwnerArrayOutput)
}

// Escalation Policy id.
func (o LookupPolicyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPolicyResult) string { return v.Id }).(pulumi.StringOutput)
}

// Name of the Escalation Policy
func (o LookupPolicyResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPolicyResult) string { return v.Name }).(pulumi.StringOutput)
}

// You can choose to repeat the entire policy, if no one acknowledges the incident even after the Escalation Policy has been executed fully once
func (o LookupPolicyResultOutput) Repeats() GetPolicyRepeatArrayOutput {
	return o.ApplyT(func(v LookupPolicyResult) []GetPolicyRepeat { return v.Repeats }).(GetPolicyRepeatArrayOutput)
}

// Rules will have the details of who to notify and when to notify and how to notify them.
func (o LookupPolicyResultOutput) Rules() GetPolicyRuleArrayOutput {
	return o.ApplyT(func(v LookupPolicyResult) []GetPolicyRule { return v.Rules }).(GetPolicyRuleArrayOutput)
}

// Team id.
func (o LookupPolicyResultOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPolicyResult) string { return v.TeamId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPolicyResultOutput{})
}
