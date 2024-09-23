import pandas as pd  # import pandas and call the imported version 'pd'
from ydata_profiling import ProfileReport  # import it for EDA
import matplotlib.pyplot as plt  # import the package and call it 'plt'
import polars as pl  # import polars and call it 'pl'
from lib import load_data

# Read the data using polar and print the data & statistics
pl_df = load_data("Billionaire_2021.csv", null_values=["N/A"])
print(pl_df)
print(pl_df.describe())

# get the count of billionaires from each country
country_count = pl_df.select(pl.col("Country").value_counts())
print(country_count)

def get_statistics():
    count_values = country_count.select(
        pl.col("Country").struct.field("count").alias("count")
    )
    # get the statistics for the distribution of billionaires
    stats = count_values.select(
        [
            pl.col("count").mean().alias("Mean"),
            pl.col("count").median().alias("Median"),
            pl.col("count").std().alias("Standard_Deviation"),
        ]
    )
    print(stats)

get_statistics()

# get value from country_count DataFrame since its a pl dataframe
countries = country_count.select(pl.col("Country").struct.field("Country")).to_series()
counts = country_count.select(pl.col("Country").struct.field("count")).to_series()
# sort the value
sorted_data = sorted(zip(countries, counts), key=lambda x: x[1], reverse=True)
countries, counts = zip(*sorted_data)

# Create a bar plot of where billionaires are from
def build_barplot():
    # plot
    plt.figure(figsize=(15, 12))
    plt.bar(countries, counts)
    plt.title("Where Are Billionaires From")
    plt.xlabel("Country")
    plt.ylabel("Number of Billionaires")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("Where Are Billionaires From (2021)")  ## generate and save the picture


build_barplot()

# get a rough view of what the data looks like
df = pd.read_csv("Billionaire_2021.csv", dtype={"Age": float}, na_values=["N/A"])
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
            "NetWorth": "A numerical value representing an individual's total wealth, \
                    expressed in billions of US dollars and preceded by a dollar sign.",
            "Country": "The name of the nation where the individual primarily resides \
                    or holds citizenship.",
            "Source": "The primary company or companies responsible for generating \
                    the individual's wealth.",
            "Industry": "The broad economic sector or business category in which the \
                    individual's primary source of wealth operates.",
        }
    },
)

# generate the report
report.to_notebook_iframe()
report.to_file("report.html")