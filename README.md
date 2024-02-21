# Dagster Quickstart

## Getting started

If you are running the Dagster Quickstart in a GitHub Codepsace, the requirements have already been installed. Simply run:

```sh
source .venv/bin/activate
```

Then, start Dagster:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

---

If you aren't using Codespaces, you'll need to install the dependencies yourself:

```sh
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_quickstart_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_quickstart_tests
```

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.
