# Test lib.py
from lib import load_data


def test_load_data():
    dataset = "Billionaire_2021.csv"
    result_load = load_data(dataset)
    assert result_load is not None


if __name__ == "__main__":
    test_load_data()
