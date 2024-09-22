import pandas as pd  # imports pandas and calls the imported version 'pd'
import polars as pl  # imports polars and calls the imported version 'pl'
import matplotlib.pyplot as plt  # imports the package and calls it 'plt'
from ydata_profiling import ProfileReport  # import it for EDA

# get a rough view of what the data looks like - the list of all the world's billionaires from 2021
df = pl.read_csv("Billionaire_2021.csv", schema_overrides={"Age": pl.Float64})
print(df.head())

# use dataprofiling to do EDA for this dataset
report = ProfileReport(
    df,
    title="Trending Books",
    dataset={
        "description": "This profiling report was generated for the EDA project.",
        "copyright_holder": "Forbes",
        "copyright_year": 2021,
        "url": "<https://www.forbes.com/>",
    },
    variables={
        "descriptions": {
            "NetWorth": "A numerical value representing an individual's total wealth, expressed in billions of US dollars and preceded by a dollar sign.",
            "Country": "The name of the nation where the individual primarily resides or holds citizenship.",
            "Source": "The primary company or companies responsible for generating the individual's wealth.",
            "Industry": "The broad economic sector or business category in which the individual's primary source of wealth operates.",
        }
    },
)

# generate the report
report.to_notebook_iframe()

# generate reports of different formats
report.to_fill("report.html")
report.to_markdown("report.md")
