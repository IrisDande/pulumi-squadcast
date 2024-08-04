---
title: Squadcast Installation & Configuration
meta_desc: Information on how to install the Squadcast provider.
layout: installation
---

## Installation

The Pulumi Squadcast provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@irisdanded/pulumi-squadcast`](https://www.npmjs.com/package/@irisdanded/pulumi-squadcast)
* Python: [`irisdadded_squadcast_pulumi`](https://pypi.org/project/irisdadded_squadcast_pulumi/)
* Go: [`github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast`](https://pkg.go.dev/github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast)
* .NET: [`IrisDanded.Pulumi.Squadcast`](https://www.nuget.org/packages/IrisDanded.Pulumi.Squadcast)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `squadcast` provider:

- `squadcast:apiKey` (environment: `squadcast_API_KEY`) - the API key for `squadcast`
- `squadcast:region` (environment: `squadcast_REGION`) - the region in which to deploy resources

### Provider Binary

The Squadcast provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource squadcast <version>
```

Replace the version string `<version>` with your desired version.
