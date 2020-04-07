import pandas as pd
from scipy.stats import ks_2samp
df = pd.read_csv('./constituents-financials_csv.csv')
'''features is a set of example features from the sample of stocks I use in this program'''
features = ['Price/Earnings', 'Dividend Yield', 'Earnings/Share', 'Price/Sales', 'Price/Book']

def samples(df, total_size, samp_size):
    tot = df.sample(total_size) #sample total number of stocks of all 10 subsets
    vals= list()
    for i in range(10):
        vals.append(tot[(i*samp_size):(i*samp_size+samp_size)]) #allot enough stocks for each sample in a list
    return vals
    
def testDistribution (sample, df, features, criteria):
    for x in features:
        if ks_2samp(sample[x], df[x])[1] < criteria: #test each feature of sample
            return True
    return False
    
def testSuite(df, total_size, samp_size, features, criteria):
    ''' df: DataFrame of stocks 
        total_size: total number of stocks in 10 samples (int)
        samp_size: number of stocks in each sample (int)
        features: the 5 features being tested (list of strings)
        criteria: p-val limit for acceptance
    '''
    vals = samples(df, total_size, samp_size) #return list of 10 subsets of 50 unique stocks
    badSample = False
    #test the distribution of each feature in each sample
    for i in range(10):
        badSample = testDistribution(vals[i], df, features, criteria)
    if (badSample == True): #if a distribution fails KS test, resample sets
        testSuite(df, total_size, samp_size, features, criteria)
    else:
        print("Good samples")
        return vals #return statistically matching samples


vals = testSuite(df, 500, 50, features, .05)