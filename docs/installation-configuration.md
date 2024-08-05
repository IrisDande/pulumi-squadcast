---
title: Squadcast Installation & Configuration
meta_desc: Information on how to install the Squadcast provider.
layout: installation
---

## Installation

The Pulumi Squadcast provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@irisdanded/pulumi-squadcast`](https://www.npmjs.com/package/@irisdanded/pulumi-squadcast)
* Python: [`irisdanded_squadcast_pulumi`](https://pypi.org/project/irisdanded_squadcast_pulumi/)
* Go: [`github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast`](https://pkg.go.dev/github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast)
* .NET: [`IrisDanded.Pulumi.Squadcast`](https://www.nuget.org/packages/IrisDanded.Pulumi.Squadcast)


### Configuring The Provider

Pulumi relies on the Squadcast SDK to authenticate requests from your computer to Squadcast. Your credentials are never sent
to pulumi.com. Once the credentials are obtained, there are two ways to communicate your configuration parameters to Pulumi:

The following configuration points are available for the `squadcast` provider:

1. Set the environment variable

- `squadcast:refreshToken` (environment: `SQUADCAST_REFRESHTOKEN`) - (String, Sensitive) The refresh token, This can be created from user profile
- `squadcast:region` (environment: `SQUADCAST_REGION`) - (String) The region you are currently hosted on.Supported values are "us" and "eu"

2. If you prefer that they be stored alongside your Pulumi stack for easy multi-user access:

```bash
$ pulumi config set --secret squadcast:refreshToken
$ pulumi config set squadcast:region
```
### Provider Binary

The Squadcast provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource squadcast <version> --server github://api.github.com/IrisDande
```

Replace the version string `<version>` with your desired version.
