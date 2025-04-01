> [!NOTE]
> This project has been archived, please reference the [Quickstart](https://docs.dagster.io/getting-started/quickstart) available in the Dagster documentation.

---

<div align="center">
  <a target="_blank" href="https://dagster.io" style="background:none">
    <img alt="dagster logo" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/7010804c-05a6-4ef4-bfc8-d9c88d458906" width="auto" height="120px">
  </a>
</div>

# Dagster Quickstart

Get up-and-running with the Dagster quickstart project -- open the project in a GitHub Codespace and start building data pipelines with no local installation required.

For more information on how to use this project, please reference the [Dagster Quickstart guide](https://docs.dagster.io/getting-started/quickstart).

## Running The Project

### Option 1. Using GitHub Codespaces

1. Fork this repository

2. From the **Code** dropdown, select **Create codespace on main**

<img width="300" alt="Create codespace" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/954493f0-99ac-4aa9-884b-3b2800d2a0d8">

3. Once the codespace has loaded, run `dagster dev` in the terminal to start Dagster:

    ```bash
    dagster dev
    ```

4. When prompted, click **Open in Browser**.

<img width="400" alt="Codespace Open In Browser" src="https://github.com/dagster-io/dagster-quickstart/assets/5807118/2d598c56-2bf5-4ffb-927f-5d2e4a5e6967">

> [!TIP]  
> If the popup to open Dagster is not visible, you can navigate to the **Forwarded Ports** tab, and open the **Forwarded Address** for port 3000.

5. **Success!** You'll be presented with the lineage of assets in the quickstart project.

![image](https://github.com/dagster-io/dagster-quickstart/assets/5807118/fe5dcf40-a086-42a3-974c-42c252e3a705)

### Option 2. Running Locally

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
