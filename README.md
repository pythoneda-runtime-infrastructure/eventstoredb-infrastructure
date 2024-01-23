# runtime-infrastructure/eventstoredb-infrastructure

This package provides the infrastructure to <https://github.com/pythoneda-runtime-infrastructure/eventstoredb>.

## How to declare it in your flake

Check the latest tag of the definition repository: https://github.com/pythoneda-runtime-infrastructure-def/eventstoredb-infrastructure/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-runtime-infrastructure-eventstoredb-infrastructure = {
      [optional follows]
      url =
        "github:pythoneda-runtime-infrastructure-def/eventstoredb-infrastructure/[version]";
    };
  };
  outputs = [..]
};
```

If your project depends upon [https://github.com/nixos/nixpkgs](nixpkgs "nixpkgs") and/or [https://github.com/numtide/flake-utils](flake-utils "flake-utils"), you might want to pin them under the `[optional follows]` above.

The Nix flake is provided by the [https://github.com/pythoneda-runtime-infrastructure-def/eventstoredb-infrastructure](pythoneda-runtime-infrastructure-def/eventstoredb-infrastructure "pythoneda-runtime-infrastructure-def/eventstoredb-infrastructure") repository.
