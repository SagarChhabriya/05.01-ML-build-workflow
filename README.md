# 05.01-ML-build-workflow

## ML Build Workflow 1 – Code + Unit Tests

This repository implements **Workflow 1** of an ML build system: validating code using unit tests.  
The goal is to ensure that core components such as data loading and preprocessing behave correctly before introducing model training.

This workflow is the foundation of all ML CI pipelines.


## Roadmap

We will evolve this project in five stages:

1. Code + Unit Tests (Current)
2. Lightweight End-to-End Pipeline
3. Artifact-Based Build
4. Docker-Based Build
5. Full MLOps Pipeline

Each stage adds only one new layer of complexity.


## What This Workflow Validates

This workflow checks that:

- Python environment installs correctly
- Dependencies are installed without errors
- Preprocessing code runs
- Unit tests pass

It does **not** train a model yet.  
It only ensures that your data utilities and preprocessing logic are safe to use.


## 1. Project Structure

```

.
├── data/
│   └── sample.csv
├── src/
│   └── preprocess.py
├── tests/
│   └── test_preprocess.py
├── requirements.txt
├── README.md
└── .github/
└── workflows/
└── ci.yml

````


## 2. Sample Dataset (`data/sample.csv`)

Create a `data` folder and add this file:

```csv
age,income,education_years,experience,loan_amount,default
25,30000,14,2,5000,0
32,55000,16,7,12000,0
40,72000,18,15,20000,0
22,18000,12,1,3000,1
29,42000,15,4,8000,0
35,60000,16,10,15000,0
28,35000,14,3,7000,0
45,80000,18,20,25000,0
23,20000,12,1,4000,1
38,65000,17,12,18000,0
27,32000,14,2,6000,0
31,48000,15,6,10000,0
41,75000,18,17,22000,0
24,22000,12,1,3500,1
36,62000,16,11,16000,0
30,,15,5,9000,0
````

Dataset notes:

* This is synthetic data.
* It is small and safe to commit.
* It is only for validating code execution, not for building accurate models.
* The `default` column is the target label.


## 3. Preprocessing Code (`src/preprocess.py`)

```python
import pandas as pd

def load_data(path):
    """
    Loads a CSV file and drops rows with missing values.
    """
    df = pd.read_csv(path)
    return df.dropna()
```


## 4. Unit Test (`tests/test_preprocess.py`)

This test verifies that:

* The CSV file loads correctly
* Missing values are removed

```python
from src.preprocessing import load_data

def test_load_data():
    df = load_data("data/sample.csv")
    
    # Ensure dataframe is not empty
    assert not df.empty

    # Ensure missing values are removed
    assert df.isnull().sum().sum() == 0
```


## 5. Requirements (`requirements.txt`)

```text
pandas
pytest
```


## 6. CI Workflow (`.github/workflows/ci.yml`)

This GitHub Actions workflow runs the unit tests automatically on every push and pull request.

```yaml
name: ML CI - Workflow 1 (Unit Tests)

on:
  push:
    branches: [ "main" ]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run unit tests
        run: pytest
```


## How to Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run unit tests:

```
pytest
```

If all tests pass, Workflow 1 is correctly implemented.


## Why Workflow 1 Matters

Workflow 1 provides:

* Safe refactoring of preprocessing code
* Fast feedback on bugs
* Reproducibility
* A professional CI baseline for ML projects

Without this step, later workflows become unstable and harder to debug.


## Next Step

Workflow 2 will introduce:

* `src/train.py`
* Lightweight model training
* End-to-end pipeline execution in CI

Workflow 1 proves that your **code is correct**.
Workflow 2 will prove that your **ML system runs from start to finish**.
