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

// You can manage the members of a Team here.
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
//			exampleTeamRole, err := squadcast.LookupTeamRole(ctx, &squadcast.LookupTeamRoleArgs{
//				Name:   "example role name",
//				TeamId: exampleTeam.Id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squadcast.NewTeamMember(ctx, "exampleTeamMember", &squadcast.TeamMemberArgs{
//				TeamId: pulumi.String(exampleTeam.Id),
//				UserId: pulumi.String(exampleUser.Id),
//				RoleIds: pulumi.StringArray{
//					pulumi.String(exampleTeamRole.Id),
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
// teamID:emailID
//
// Use 'Get All Teams' API to get the id of the team
//
// ```sh
// $ pulumi import squadcast:index/teamMember:TeamMember example_resource_name 62d2fe23a57381088224d726:test@example.com
// ```
type TeamMember struct {
	pulumi.CustomResourceState

	// role ids.
	RoleIds pulumi.StringArrayOutput `pulumi:"roleIds"`
	// Team id.
	TeamId pulumi.StringOutput `pulumi:"teamId"`
	// user id (ObjectId).
	UserId pulumi.StringOutput `pulumi:"userId"`
}

// NewTeamMember registers a new resource with the given unique name, arguments, and options.
func NewTeamMember(ctx *pulumi.Context,
	name string, args *TeamMemberArgs, opts ...pulumi.ResourceOption) (*TeamMember, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RoleIds == nil {
		return nil, errors.New("invalid value for required argument 'RoleIds'")
	}
	if args.TeamId == nil {
		return nil, errors.New("invalid value for required argument 'TeamId'")
	}
	if args.UserId == nil {
		return nil, errors.New("invalid value for required argument 'UserId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TeamMember
	err := ctx.RegisterResource("squadcast:index/teamMember:TeamMember", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTeamMember gets an existing TeamMember resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeamMember(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TeamMemberState, opts ...pulumi.ResourceOption) (*TeamMember, error) {
	var resource TeamMember
	err := ctx.ReadResource("squadcast:index/teamMember:TeamMember", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TeamMember resources.
type teamMemberState struct {
	// role ids.
	RoleIds []string `pulumi:"roleIds"`
	// Team id.
	TeamId *string `pulumi:"teamId"`
	// user id (ObjectId).
	UserId *string `pulumi:"userId"`
}

type TeamMemberState struct {
	// role ids.
	RoleIds pulumi.StringArrayInput
	// Team id.
	TeamId pulumi.StringPtrInput
	// user id (ObjectId).
	UserId pulumi.StringPtrInput
}

func (TeamMemberState) ElementType() reflect.Type {
	return reflect.TypeOf((*teamMemberState)(nil)).Elem()
}

type teamMemberArgs struct {
	// role ids.
	RoleIds []string `pulumi:"roleIds"`
	// Team id.
	TeamId string `pulumi:"teamId"`
	// user id (ObjectId).
	UserId string `pulumi:"userId"`
}

// The set of arguments for constructing a TeamMember resource.
type TeamMemberArgs struct {
	// role ids.
	RoleIds pulumi.StringArrayInput
	// Team id.
	TeamId pulumi.StringInput
	// user id (ObjectId).
	UserId pulumi.StringInput
}

func (TeamMemberArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*teamMemberArgs)(nil)).Elem()
}

type TeamMemberInput interface {
	pulumi.Input

	ToTeamMemberOutput() TeamMemberOutput
	ToTeamMemberOutputWithContext(ctx context.Context) TeamMemberOutput
}

func (*TeamMember) ElementType() reflect.Type {
	return reflect.TypeOf((**TeamMember)(nil)).Elem()
}

func (i *TeamMember) ToTeamMemberOutput() TeamMemberOutput {
	return i.ToTeamMemberOutputWithContext(context.Background())
}

func (i *TeamMember) ToTeamMemberOutputWithContext(ctx context.Context) TeamMemberOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamMemberOutput)
}

// TeamMemberArrayInput is an input type that accepts TeamMemberArray and TeamMemberArrayOutput values.
// You can construct a concrete instance of `TeamMemberArrayInput` via:
//
//	TeamMemberArray{ TeamMemberArgs{...} }
type TeamMemberArrayInput interface {
	pulumi.Input

	ToTeamMemberArrayOutput() TeamMemberArrayOutput
	ToTeamMemberArrayOutputWithContext(context.Context) TeamMemberArrayOutput
}

type TeamMemberArray []TeamMemberInput

func (TeamMemberArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TeamMember)(nil)).Elem()
}

func (i TeamMemberArray) ToTeamMemberArrayOutput() TeamMemberArrayOutput {
	return i.ToTeamMemberArrayOutputWithContext(context.Background())
}

func (i TeamMemberArray) ToTeamMemberArrayOutputWithContext(ctx context.Context) TeamMemberArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamMemberArrayOutput)
}

// TeamMemberMapInput is an input type that accepts TeamMemberMap and TeamMemberMapOutput values.
// You can construct a concrete instance of `TeamMemberMapInput` via:
//
//	TeamMemberMap{ "key": TeamMemberArgs{...} }
type TeamMemberMapInput interface {
	pulumi.Input

	ToTeamMemberMapOutput() TeamMemberMapOutput
	ToTeamMemberMapOutputWithContext(context.Context) TeamMemberMapOutput
}

type TeamMemberMap map[string]TeamMemberInput

func (TeamMemberMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TeamMember)(nil)).Elem()
}

func (i TeamMemberMap) ToTeamMemberMapOutput() TeamMemberMapOutput {
	return i.ToTeamMemberMapOutputWithContext(context.Background())
}

func (i TeamMemberMap) ToTeamMemberMapOutputWithContext(ctx context.Context) TeamMemberMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TeamMemberMapOutput)
}

type TeamMemberOutput struct{ *pulumi.OutputState }

func (TeamMemberOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TeamMember)(nil)).Elem()
}

func (o TeamMemberOutput) ToTeamMemberOutput() TeamMemberOutput {
	return o
}

func (o TeamMemberOutput) ToTeamMemberOutputWithContext(ctx context.Context) TeamMemberOutput {
	return o
}

// role ids.
func (o TeamMemberOutput) RoleIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TeamMember) pulumi.StringArrayOutput { return v.RoleIds }).(pulumi.StringArrayOutput)
}

// Team id.
func (o TeamMemberOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v *TeamMember) pulumi.StringOutput { return v.TeamId }).(pulumi.StringOutput)
}

// user id (ObjectId).
func (o TeamMemberOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v *TeamMember) pulumi.StringOutput { return v.UserId }).(pulumi.StringOutput)
}

type TeamMemberArrayOutput struct{ *pulumi.OutputState }

func (TeamMemberArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*TeamMember)(nil)).Elem()
}

func (o TeamMemberArrayOutput) ToTeamMemberArrayOutput() TeamMemberArrayOutput {
	return o
}

func (o TeamMemberArrayOutput) ToTeamMemberArrayOutputWithContext(ctx context.Context) TeamMemberArrayOutput {
	return o
}

func (o TeamMemberArrayOutput) Index(i pulumi.IntInput) TeamMemberOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *TeamMember {
		return vs[0].([]*TeamMember)[vs[1].(int)]
	}).(TeamMemberOutput)
}

type TeamMemberMapOutput struct{ *pulumi.OutputState }

func (TeamMemberMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*TeamMember)(nil)).Elem()
}

func (o TeamMemberMapOutput) ToTeamMemberMapOutput() TeamMemberMapOutput {
	return o
}

func (o TeamMemberMapOutput) ToTeamMemberMapOutputWithContext(ctx context.Context) TeamMemberMapOutput {
	return o
}

func (o TeamMemberMapOutput) MapIndex(k pulumi.StringInput) TeamMemberOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *TeamMember {
		return vs[0].(map[string]*TeamMember)[vs[1].(string)]
	}).(TeamMemberOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TeamMemberInput)(nil)).Elem(), &TeamMember{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamMemberArrayInput)(nil)).Elem(), TeamMemberArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TeamMemberMapInput)(nil)).Elem(), TeamMemberMap{})
	pulumi.RegisterOutputType(TeamMemberOutput{})
	pulumi.RegisterOutputType(TeamMemberArrayOutput{})
	pulumi.RegisterOutputType(TeamMemberMapOutput{})
}
