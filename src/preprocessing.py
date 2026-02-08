import pandas as pd

def load_data(path):
    """
    Loads a CSV file and drops rows with missing values.
    """
    df = pd.read_csv(path)
    return df.dropna()
