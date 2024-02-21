<div align="center">
  <a target="_blank" href="https://dagster.io" style="background:none">
    <img alt="dagster logo" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/7010804c-05a6-4ef4-bfc8-d9c88d458906" width="auto" height="120px">
  </a>
</div>

# Dagster Quickstart

A Dagster demo project to get up-and-running ASAP -- launch a GitHub Codespace and start building data pipelines with no local installation necessary.

## Getting started

If you are running the Dagster Quickstart in a GitHub Codepsace, the requirements have already been installed! Simply run:

```bash
dagster dev
```

Click **Open in Browser** when prompted, or navigate to the **Forwarded Ports** tab, and open the **Forwarded Address** for port 3000.

If running locally, then navigate to http://localhost:3000 in your browser.

<img width="468" style="border: 1px solid black;" alt="Codespace Open In Browser" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/2d598c56-2bf5-4ffb-927f-5d2e4a5e6967">

You'll be presented with the lineage of assets in the quickstart project.

![Dagster Landing Page](https://github.com/dagster-io/dagster-quickstart/assets/5807118/85d6500f-2264-4ad6-adee-f88d8cb2bfe8)

---

If you are not using Codespaces, then you'll need to install the dependencies yourself before running `dagster dev`:

```sh
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
