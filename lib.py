# Build lib.py to adjust any system
import polars as pl


# Load the dataset, which is .csv.
def load_data(dataset, null_values=["N/A"]):
    """
    Load data from a file and return a DataFrame.
    """
    data = pl.read_csv(dataset, null_values)
    return data