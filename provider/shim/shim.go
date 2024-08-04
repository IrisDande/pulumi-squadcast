package shim

import (
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/squadcast/terraform-provider-squadcast/internal/provider"
	"github.com/IrisDande/pulumi-squadcast/provider/pkg/version"
)

func NewProvider() *schema.Provider {
	return provider.New(version.Version)()
}
