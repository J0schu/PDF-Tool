{
  description = "PDF Tool Flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-25.11";
  };

  outputs =
    { nixpkgs, ... }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; });
    in
    {
      # The package definition
      packages = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        {
          default = pkgs.python3Packages.buildPythonApplication {
            pname = "pdf-tool";
            version = "0.2.0";
            format = "pyproject";
            src = ./.;
            # Runtime dependencies
            propagatedBuildInputs = with pkgs.python3Packages; [
              pyside6
              pymupdf
            ];
            nativeBuildInputs = [
              pkgs.python3Packages.setuptools
              pkgs.python3Packages.wheel
            ];

            # Non-Python dependencies
            buildInputs = [ ];

            doCheck = false;
          };
        }
      );
      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgsFor.${system};
        in
        {
          default = pkgs.mkShell {
            buildInputs = with pkgs; [
              (python3.withPackages (
                ps: with ps; [
                  ocrmypdf
                  pyside6
                  pymupdf
                ]
              ))
            ];
          };
        }
      );
    };
}
