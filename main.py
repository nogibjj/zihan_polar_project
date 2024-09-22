import pandas as pd  # imports pandas and calls the imported version 'pd'
import matplotlib.pyplot as plt  # imports the package and calls it 'plt'

# get a rough view of what the data looks like - the list of all the world's billionaires from 2021
df = pd.read_csv("Billionaire_2021.csv")
print(df.head())

# get the count of billionaires from each country
country_count = df.Country.value_counts()
print(country_count)

# get the descriptive statistics
def get_statistics():
    print(f'The size of the dataset is {df.shape}')
    print(f'The count fo billionaires from each country is {country_count}')
    print(f'Mean of the count is {country_count.mean()}')
    print(f'Median of the count is {country_count.median()}')
    print(f'Standard deviation of the count is {country_count.std()}')

get_statistics()

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