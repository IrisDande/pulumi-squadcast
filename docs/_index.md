---
title: Squadcast
meta_desc: Provides an overview of the Squadcast Provider for Pulumi.
layout: overview
---

The Squadcast provider for Pulumi can be used to provision any of the cloud resources available in [Squadcast](https://squadcast.com).

## Example

{{< chooser language "go,javascript,typescript,python,csharp" >}}

{{% choosable language go %}}

```go
import (
	squadcast "github.com/IrisDande/pulumi-squadcast/sdk/go/squadcast"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := squadcast.NewUser(ctx, "test-user", &squadcast.UserArgs{
			Email:     pulumi.String("test@example.com"),
			FirstName: pulumi.String("Test"),
			LastName:  pulumi.String("Example"),
			Role:      pulumi.String("stakeholder"),
		})
		if err != nil {
			return err
		}
		return nil
	})
}

```

{{% /choosable %}}
{{% choosable language javascript %}}

```javascript
Coming soon
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
Coming soon
```

{{% /choosable %}}
{{% choosable language python %}}

```python
Coming soon
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
Coming soon
```

{{% /choosable %}}

{{< /chooser >}}
