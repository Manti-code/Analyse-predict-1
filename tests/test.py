import pandas as pd
import numpy as np
from predictpackage import predictpackage

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)

gauteng = ebp_df['Gauteng'].astype(float).to_list()
dates = twitter_df['Date'].to_list()

def dictionary_of_metrics(items):
    assert functions.fn1_dictionary_of_metrics(gauteng)=={'mean': 26244.42,
                                                          'median': 24403.5,
                                                          'var': 108160153.17,
                                                          'std': 10400.01,
                                                          'min': 8842.0,
                                                          'max': 39660.0} ,"incorrect"

def five_num_summary(items):
    assert functions.fn2_five_num_summary(gauteng)== {'max': 39660.0,
                                                      'median': 24403.5,
                                                      'min': 8842.0,
                                                      'q1': 18653.0,
                                                      'q3': 36372.0} , "incorrect"
