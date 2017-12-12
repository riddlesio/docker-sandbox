function ensureVirtualenv {

    # make sure we have got a virtualenv
    if [ ! -d ".venv" ]; then
        echo "Creating Virtualenv"
        python3 -m venv .venv
    fi

    if [ ! -d "$VIRTUAL_ENV" ]; then
        echo "Activating Virtualenv"
        source .venv/bin/activate
    fi

}
