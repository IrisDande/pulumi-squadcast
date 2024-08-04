module github.com/IrisDande/pulumi-squadcast/provider

go 1.22

replace (
	github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20240520223432-0c0bf0d65f10
	github.com/squadcast/terraform-provider-squadcast/shim => ./shim
)

replace github.com/squadcast/terraform-provider-squadcast => github.com/SquadcastHub/terraform-provider-squadcast v1.8.0

require (
	github.com/ettle/strcase v0.1.1
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.88.0
	github.com/pulumi/pulumi/sdk/v3 v3.126.0
)
