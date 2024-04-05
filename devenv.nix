{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.11.6";
    poetry.enable = true;
  };
  processes = {
    server.exec = ''
      uvicorn main:app --reload
    '';
  };
  services = {
    postgres = {
      enable = true;
      listen_addresses = "*";
      extensions = extensions: [
        extensions.pgaudit
      ];
      initialScript = ''
        CREATE USER postgres SUPERUSER;
      '';
      settings = {
         shared_preload_libraries = "pgaudit";
         logging_collector = false;
         log_statement = "none";
      };
      initialDatabases = [
        {
          name = "test-db";
        }
      ];
    };
  };
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ pkgs.git ];

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo hello from $GREET";

  enterShell = ''
    hello
    git --version
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep "2.42.0"
  '';

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/languages/
  # languages.nix.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
