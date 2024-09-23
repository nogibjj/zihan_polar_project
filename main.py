import pandas as pd  # imports pandas and calls the imported version 'pd'
from ydata_profiling import ProfileReport  # import it for EDA
import matplotlib.pyplot as plt  # imports the package and calls it 'plt'
import polars as pl

# Read the data using polar and print the data
pl_df = pl.read_csv("Billionaire_2021.csv", null_values=["N/A"])
print(pl_df)
print(pl_df.describe())

# get the count of billionaires from each country
country_count = pl_df.Country.value_counts()
print(country_count)

def get_statistics():
    print(f'The size of the dataset is {pl_df.shape}')
    print(f'The count fo billionaires from each country is {country_count}')
    print(f'Mean of the count is {country_count.mean()}')
    print(f'Median of the count is {country_count.median()}')
    print(f'Standard deviation of the count is {country_count.std()}')

get_statistics()

# get a rough view of what the data looks like - the list of all the world's billionaires from 2021
df = pd.read_csv("Billionaire_2021.csv", dtype={"Age": float}, na_values=["N/A"])
print(df.head())

# Create a bar plot of where billionaires are from
def build_barplot():
    plt.figure(figsize=(15, 12))
    plt.bar(country_count.index, country_count)
    plt.title("Where Are Billionaires From (2021)")
    plt.xlabel("Country")
    plt.ylabel("Number of Millionaires")
    plt.xticks(rotation=90)                             ## rotate the x-label to make it visible
    plt.show()                                          ## for some reason, plt.show() don't work in the codespace but you won't have this problem when doing it locally
    plt.savefig('Where Are Billionaires From (2021)')   ## generate and save the picture

build_barplot()

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
report.to_file("report.html")
