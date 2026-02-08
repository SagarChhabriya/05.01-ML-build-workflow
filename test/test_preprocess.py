from src.preprocessing import load_data

def test_load_data():
    df = load_data("data/sample.csv")
    
    # Ensure dataframe is not empty
    assert not df.empty

    # Ensure missing values are removed
    assert df.isnull().sum().sum() == 0
