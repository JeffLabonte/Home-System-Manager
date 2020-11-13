with import<nixpkgs> {};

stdenv.mkDerivation rec {
    name = "home_infra";
    buildInputs = [
        docker-compose
        pgcli
        python38
        python38Packages.pip
        python38Packages.django
        python38Packages.djangorestframework
        python38Packages.psycopg2
    ];
    shellHook = ''
        export DJANGO_SECRET_KEY=$(uuidgen)
        export DB_HOST=localhost
        export DB_PORT=5432
        export POSTGRES_DB=home_infra_dev
        export POSTGRES_USERNAME=home_infra_dev
        export POSTGRES_PASSWORD=$(uuidgen)

        if [ ! -d .venv/ ]; then
            python3 -m venv .venv
        fi
        .venv/bin/pip install --upgrade pip
        .venv/bin/pip install -r requirements/requirements.dev.txt
        source .venv/bin/activate
    '';
}
