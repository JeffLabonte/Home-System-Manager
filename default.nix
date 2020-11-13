with import<nixpkgs> {};

stdenv.mkDerivation rec {
    name = "home_infra";
    buildInputs = [
        docker-compose
        pgcli
        python38
        python38Packages.pip
        python38Packages.setuptools
        python38Packages.psycopg2
    ];
    shellHook = ''
        export DJANGO_SECRET_KEY=$(uuidgen)
        export DB_HOST=localhost
        export DB_PORT=5432
        export POSTGRES_DB=home_infra_dev
        export POSTGRES_USERNAME=home_infra_dev

	      PASSWORD_FILE=".generated_password"
	      if [ ! -f $PASSWORD_FILE ]; then
            echo "$(uuidgen | base64)" > $PASSWORD_FILE
	      fi

        export POSTGRES_PASSWORD=$(cat $PASSWORD_FILE)

        if [ ! -d .venv/ ]; then
            python3 -m venv .venv
        fi
        .venv/bin/pip install --upgrade pip
        .venv/bin/pip install -r requirements/requirements.dev.txt
        source .venv/bin/activate
    '';
}
