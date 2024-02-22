<div align="center">
  <a target="_blank" href="https://dagster.io" style="background:none">
    <img alt="dagster logo" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/7010804c-05a6-4ef4-bfc8-d9c88d458906" width="auto" height="120px">
  </a>
</div>

# Dagster Quickstart

Get up-and-running with a Dagster quickstart project -- open the project in a GitHub Codespace and start building data pipelines with no local installation necessary.

## Running The Project

### Option 1. - Using GitHub Codespaces

1. 


In the terminal of the VSCode editor, start Dagster by running the following command:

```bash
dagster dev
```

When prompted, click **Open in Browser**, or navigate to the **Forwarded Ports** tab, and open the **Forwarded Address** for port 3000.

If running locally, then navigate to http://localhost:3000 in your browser.

<img width="468" style="border: 1px solid black;" alt="Codespace Open In Browser" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/2d598c56-2bf5-4ffb-927f-5d2e4a5e6967">

You'll be presented with the lineage of assets in the quickstart project.

![Dagster Landing Page](https://github.com/dagster-io/dagster-quickstart/assets/5807118/85d6500f-2264-4ad6-adee-f88d8cb2bfe8)


### Option 2. - Running Locally

1. Clone the Dagster Quickstart repository:

    ```sh
    git clone https://github.com/dagster-io/dagster-quickstart

    cd dagster-quickstart
    ```

2. Install the required dependencies.

    Here we are using `-e`, for ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs), so that when Dagster code is modified, the changes automatically apply. 

    ```sh
    pip install -e ".[dev]"
    ```

3. Run the project!

    ```sh
    dagster dev
    ```

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_quickstart_tests` directory and you can run tests using `pytest`.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.
