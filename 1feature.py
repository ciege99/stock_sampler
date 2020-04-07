import pandas as pd
from scipy.stats import ks_2samp
df = pd.read_csv('./constituents-financials_csv.csv')
'''
this program demonstrates the ease of creating a matching distr. for 1 feature
'''

def randomSample(df, feature):
    vals = pd.DataFrame(columns=df.columns)
    for i in range(10): #select 10 features from each bucket
        vals = vals.append( df[(df[feature] == i)].sample(10) )

    return vals

df['PE Rank'] = pd.qcut(df['Price/Earnings'], q=10, duplicates='drop', labels=False)
df['DY Rank'] = pd.qcut(df['Dividend Yield'], q=10, duplicates='drop', labels=False)
df['ES Rank'] = pd.qcut(df['Earnings/Share'], q=10, duplicates='drop', labels=False)
df['PS Rank'] = pd.qcut(df['Price/Sales'], q=10, duplicates='drop', labels=False)
df['PB Rank'] = pd.qcut(df['Price/Book'], q=10, duplicates='drop', labels=False)

test = randomSample(df, 'PE Rank')
print(ks_2samp(test['Price/Earnings'], df['Price/Earnings']))