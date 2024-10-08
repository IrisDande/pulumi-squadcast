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

// User resource.
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
//			_, err := squadcast.NewUser(ctx, "exampleUser", &squadcast.UserArgs{
//				Abilities: pulumi.StringArray{
//					pulumi.String("manage-billing"),
//				},
//				Email:     pulumi.String("test@example.com"),
//				FirstName: pulumi.String("test"),
//				LastName:  pulumi.String("lastname"),
//				Role:      pulumi.String("stakeholder"),
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
// emailID
//
// ```sh
// $ pulumi import squadcast:index/user:User example_resource_name test@example.com
// ```
type User struct {
	pulumi.CustomResourceState

	// user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
	Abilities pulumi.StringArrayOutput `pulumi:"abilities"`
	// User email.
	Email pulumi.StringOutput `pulumi:"email"`
	// User first name.
	FirstName pulumi.StringOutput `pulumi:"firstName"`
	// User last name.
	LastName pulumi.StringOutput `pulumi:"lastName"`
	// User role.
	Role pulumi.StringOutput `pulumi:"role"`
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOption) (*User, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Email == nil {
		return nil, errors.New("invalid value for required argument 'Email'")
	}
	if args.FirstName == nil {
		return nil, errors.New("invalid value for required argument 'FirstName'")
	}
	if args.LastName == nil {
		return nil, errors.New("invalid value for required argument 'LastName'")
	}
	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource User
	err := ctx.RegisterResource("squadcast:index/user:User", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *UserState, opts ...pulumi.ResourceOption) (*User, error) {
	var resource User
	err := ctx.ReadResource("squadcast:index/user:User", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering User resources.
type userState struct {
	// user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
	Abilities []string `pulumi:"abilities"`
	// User email.
	Email *string `pulumi:"email"`
	// User first name.
	FirstName *string `pulumi:"firstName"`
	// User last name.
	LastName *string `pulumi:"lastName"`
	// User role.
	Role *string `pulumi:"role"`
}

type UserState struct {
	// user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
	Abilities pulumi.StringArrayInput
	// User email.
	Email pulumi.StringPtrInput
	// User first name.
	FirstName pulumi.StringPtrInput
	// User last name.
	LastName pulumi.StringPtrInput
	// User role.
	Role pulumi.StringPtrInput
}

func (UserState) ElementType() reflect.Type {
	return reflect.TypeOf((*userState)(nil)).Elem()
}

type userArgs struct {
	// user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
	Abilities []string `pulumi:"abilities"`
	// User email.
	Email string `pulumi:"email"`
	// User first name.
	FirstName string `pulumi:"firstName"`
	// User last name.
	LastName string `pulumi:"lastName"`
	// User role.
	Role string `pulumi:"role"`
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
	Abilities pulumi.StringArrayInput
	// User email.
	Email pulumi.StringInput
	// User first name.
	FirstName pulumi.StringInput
	// User last name.
	LastName pulumi.StringInput
	// User role.
	Role pulumi.StringInput
}

func (UserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*userArgs)(nil)).Elem()
}

type UserInput interface {
	pulumi.Input

	ToUserOutput() UserOutput
	ToUserOutputWithContext(ctx context.Context) UserOutput
}

func (*User) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (i *User) ToUserOutput() UserOutput {
	return i.ToUserOutputWithContext(context.Background())
}

func (i *User) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserOutput)
}

// UserArrayInput is an input type that accepts UserArray and UserArrayOutput values.
// You can construct a concrete instance of `UserArrayInput` via:
//
//	UserArray{ UserArgs{...} }
type UserArrayInput interface {
	pulumi.Input

	ToUserArrayOutput() UserArrayOutput
	ToUserArrayOutputWithContext(context.Context) UserArrayOutput
}

type UserArray []UserInput

func (UserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (i UserArray) ToUserArrayOutput() UserArrayOutput {
	return i.ToUserArrayOutputWithContext(context.Background())
}

func (i UserArray) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserArrayOutput)
}

// UserMapInput is an input type that accepts UserMap and UserMapOutput values.
// You can construct a concrete instance of `UserMapInput` via:
//
//	UserMap{ "key": UserArgs{...} }
type UserMapInput interface {
	pulumi.Input

	ToUserMapOutput() UserMapOutput
	ToUserMapOutputWithContext(context.Context) UserMapOutput
}

type UserMap map[string]UserInput

func (UserMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (i UserMap) ToUserMapOutput() UserMapOutput {
	return i.ToUserMapOutputWithContext(context.Background())
}

func (i UserMap) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(UserMapOutput)
}

type UserOutput struct{ *pulumi.OutputState }

func (UserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**User)(nil)).Elem()
}

func (o UserOutput) ToUserOutput() UserOutput {
	return o
}

func (o UserOutput) ToUserOutputWithContext(ctx context.Context) UserOutput {
	return o
}

// user abilities/permissions. (manage-api-tokens, manage-billing, manage-extensions, manage-teams, manage-users, manage-webhooks, manage-organization-analytics, manage-postmortem-templates)
func (o UserOutput) Abilities() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *User) pulumi.StringArrayOutput { return v.Abilities }).(pulumi.StringArrayOutput)
}

// User email.
func (o UserOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Email }).(pulumi.StringOutput)
}

// User first name.
func (o UserOutput) FirstName() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.FirstName }).(pulumi.StringOutput)
}

// User last name.
func (o UserOutput) LastName() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.LastName }).(pulumi.StringOutput)
}

// User role.
func (o UserOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *User) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

type UserArrayOutput struct{ *pulumi.OutputState }

func (UserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*User)(nil)).Elem()
}

func (o UserArrayOutput) ToUserArrayOutput() UserArrayOutput {
	return o
}

func (o UserArrayOutput) ToUserArrayOutputWithContext(ctx context.Context) UserArrayOutput {
	return o
}

func (o UserArrayOutput) Index(i pulumi.IntInput) UserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *User {
		return vs[0].([]*User)[vs[1].(int)]
	}).(UserOutput)
}

type UserMapOutput struct{ *pulumi.OutputState }

func (UserMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*User)(nil)).Elem()
}

func (o UserMapOutput) ToUserMapOutput() UserMapOutput {
	return o
}

func (o UserMapOutput) ToUserMapOutputWithContext(ctx context.Context) UserMapOutput {
	return o
}

func (o UserMapOutput) MapIndex(k pulumi.StringInput) UserOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *User {
		return vs[0].(map[string]*User)[vs[1].(string)]
	}).(UserOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*UserInput)(nil)).Elem(), &User{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserArrayInput)(nil)).Elem(), UserArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*UserMapInput)(nil)).Elem(), UserMap{})
	pulumi.RegisterOutputType(UserOutput{})
	pulumi.RegisterOutputType(UserArrayOutput{})
	pulumi.RegisterOutputType(UserMapOutput{})
}
