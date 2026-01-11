# GitHub Action Testing: Time Sum Artifact

## Project Overview

This repository demonstrates a GitHub Action workflow that calculates the sum of digits of the current Indian Standard Time (IST) and publishes the result as a workflow artifact. It's designed for testing and learning GitHub Action scheduling and artifact handling.

## Key Features

- **Time Sum Calculation**: A Python script determines the sum of digits from the current hour and minute in IST.
- **Scheduled Execution**: The workflow runs automatically every 5 minutes.
- **Manual Trigger**: You can manually run the workflow from the GitHub Actions tab.
- **Artifact Output**: The calculated time and sum are saved to `output.txt` and uploaded as a downloadable artifact.

## How it Works

The workflow (`.github/workflows/time-sum.yml`) performs the following steps:

1. **Checks out** the repository.
2. **Sets up Python 3.11**.
3. **Installs** the `pytz` library.
4. **Runs** the `time_sum.py` script, which calculates the sum and writes it to `output.txt`.
5. **Uploads** `output.txt` as a workflow artifact named `time-sum-output`.

To view results:

- Navigate to the **Actions** tab in the repository.
- Select the "Time Sum Artifact Job" workflow.
- Click on any completed run to view logs and download the `time-sum-output` artifact.

## Example Output (from `output.txt`)

```
Current Indian Time (IST): 10:35
Sum of digits: 9
```
