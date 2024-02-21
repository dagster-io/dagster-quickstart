<div align="center">
  <a target="_blank" href="https://dagster.io" style="background:none">
    <img alt="dagster logo" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/7010804c-05a6-4ef4-bfc8-d9c88d458906" width="auto" height="120px">
  </a>
</div>

# Dagster Quickstart

## Getting started

If you are running the Dagster Quickstart in a GitHub Codepsace, the requirements have already been installed! Simply run:

```sh
source .venv/bin/activate
```

And then, start Dagster:

```bash
dagster dev
```

Navigate to the port forwarding for your Codespace, and open the URL mapped to port 3000.

If running locally, then navigate to http://localhost:3000 in your browser.

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
