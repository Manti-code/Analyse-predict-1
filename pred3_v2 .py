#!/usr/bin/env python
# coding: utf-8

# # Analyse - Predict
# 
# Functions are important in reducing the replication of code as well as giving the user the functionality of getting an ouput on varying inputs. The functions you will write all use Eskom data/variables.
# 
# ## Instructions to Students
# - **Do not add or remove cells in this notebook. Do not edit or remove the `### START FUNCTION` or `### END FUNCTION` comments. Do not add any code outside of the functions you are required to edit. Doing any of this will lead to a mark of 0%!**
# - Answer the questions according to the specifications provided.
# - Use the given cell in each question to to see if your function matches the expected outputs.
# - Do not hard-code answers to the questions.
# - The use of stackoverflow, google, and other online tools are permitted. However, copying fellow student's code is not permissible and is considered a breach of the Honour code. Doing this will result in a mark of 0%.
# - Good luck, and may the force be with you!

# ## Imports

# In[1]:


import pandas as pd
import numpy as np


# ## Data Loading and Preprocessing

# ### Electricification by province (EBP) data

# In[2]:


ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()


# ### Twitter data

# In[3]:


twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()


# ## Important Variables (Do not edit these!)

# In[4]:


# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}


# ## Function 1: Metric Dictionary
# 
# Write a function that calculates the mean, median, variance, standard deviation, minimum and maximum of of list of items. You can assume the given list is contains only numerical entries, and you may use numpy functions to do this.
# 
# **Function Specifications:**
# - Function should allow a list as input.
# - It should return a `dict` with keys `'mean'`, `'median'`, `'std'`, `'var'`, `'min'`, and `'max'`, corresponding to the mean, median, standard deviation, variance, minimum and maximum of the input list, respectively.
# - The standard deviation and variance values must be unbiased. **Hint:** use the `ddof` parameter in the corresponding numpy functions!
# - All values in the returned `dict` should be rounded to 2 decimal places.

# In[14]:


### START FUNCTION
def dictionary_of_metrics(items):
    
    """  Sort the list.
         Add elements in the list to get sum.
         Find the length of the list.     """
    
    list2 = sorted(items) 
    sum_list = sum(list2) 
    length_list = len(list2) 
    
    """Calc mean by dividing sum of list by no of elements in list and round mean to 2 decimal places. 
       Find the median and round to 2 decimal places.     """
    
    mean = sum_list/length_list 
    mean_r = round(mean,2)      
    median = round(np.median(items),2) 
    
    """ Find the lowest and highest values in list. """

    min_list2 = min(list2) 
    max_list2 = max(list2) 
    
    """ Create an empty list.
        Run a loop iterating through list.
        Take each value subtract the mean from it, then square that value.
        Add the value to list_diff_sq.  """
    
    list_diff_sq = [] 
    for i in items:   
        a = (i-mean)**2  
        list_diff_sq.append(a) 
        
    """ Get sum of new list divided by N-1 and rounded to 2 decimal places. 
        Calc sqrt of variance and round to 2 decimal places.        """    
    
    variance = round(sum(list_diff_sq)/(length_list-1),2) 
    std_dev = round(variance**0.5,2) 
    
    
    dict1 = {'mean':mean_r,'median':median,
             'var':variance,'std':std_dev,
             'min':min_list2,'max':max_list2}

    return dict1 

### END FUNCTION


# In[6]:


dictionary_of_metrics(gauteng)


# _**Expected Output**_:
# 
# ```python
# dictionary_of_metrics(gauteng) == {'mean': 26244.42,
#                                    'median': 24403.5,
#                                    'var': 108160153.17,
#                                    'std': 10400.01,
#                                    'min': 8842.0,
#                                    'max': 39660.0}
#  ```

# ## Function 2: Five Number Summary
# 
# Write a function which takes in a list of integers and returns a dictionary of the [five number summary.](https://www.statisticshowto.datasciencecentral.com/how-to-find-a-five-number-summary-in-statistics/).
# 
# **Function Specifications:**
# - The function should take a list as input.
# - The function should return a `dict` with keys `'max'`, `'median'`, `'min'`, `'q1'`, and `'q3'` corresponding to the maximum, median, minimum, first quartile and third quartile, respectively. You may use numpy functions to aid in your calculations.
# - All numerical values should be rounded to two decimal places.

# In[7]:


### START FUNCTION
def five_num_summary(items):
    
    """ Sorting the input list and saving it in a new variable.
        Finding the minimum value of list1 and saving it in a variable.
        Finding the maximum value of list1 and saving it in a variable.  """
    
    list1 = sorted(items)  
    min_list = min(list1)  
    max_list = max(list1)  
    
    """ Using median fintion from mumpy to find the median of input values.
        Using quantile method from numpy to find the first and third quantile. """
    
    median = np.median(items) 
    q1 = np.quantile(items,0.25) 
    q3 = np.quantile(items,0.75) 
    
    
    dict1 = {'max':max_list,'median':median,'min':min_list,'q1':q1,'q3':q3}
    
    return dict1

### END FUNCTION


# In[8]:


five_num_summary(gauteng)


# _**Expected Output:**_
# 
# ```python
# five_num_summary(gauteng) == {
#     'max': 39660.0,
#     'median': 24403.5,
#     'min': 8842.0,
#     'q1': 18653.0,
#     'q3': 36372.0
# }
# 
# ```

# ## Function 3: Date Parser
# 
# The `dates` variable (created at the top of this notebook) is a list of dates represented as strings. The string contains the date in `'yyyy-mm-dd'` format, as well as the time in `hh:mm:ss` formamt. The first three entries in this variable are:
# ```python
# dates[:3] == [
#     '2019-11-29 12:50:54',
#     '2019-11-29 12:46:53',
#     '2019-11-29 12:46:10'
# ]
# ```
# 
# Write a function that takes as input a list of these datetime strings and returns only the date in `'yyyy-mm-dd'` format.
# 
# **Function Specifications:**
# - The function should take a list of strings as input.
# - Each string in the input list is formatted as `'yyyy-mm-dd hh:mm:ss'`.
# - The function should return a list of strings where each element in the returned list contains only the date in the `'yyyy-mm-dd'` format.

# In[9]:


### START FUNCTION
def date_parser(dates):
    
    """ Initiating two empty lists """
    
    list1=[] 
    list2=[] 
    
    """ Running a for loop through input dates list.
        Using split fn to seperate date and time, saving it to list 1. """
    
    for i in dates:                  
        list1.append(i.split(" "))  
        
    """ Run loop through list 1.
        Taking the first value in list i.e dates and saving into another list.   """
        
    for j in list1:                  
        list2.append(j[0])           
        
    return list2

### END FUNCTION


# In[10]:


date_parser(dates[:3])


# _**Expected Output:**_
# 
# ```python
# date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
# date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']
# ```

# ## Function 4: Municipality & Hashtag Detector
# 
# Write a function which takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.
# 
# **Function Specifications:**
# * Function should take a pandas `dataframe` as input.
# * Extract the municipality from a tweet using the `mun_dict` dictonary given below, and insert the result into a new column named `'municipality'` in the same dataframe.
# * Use the entry `np.nan` when a municipality is not found.
# * Extract a list of hashtags from a tweet into a new column named `'hashtags'` in the same dataframe.
# * Use the entry `np.nan` when no hashtags are found.
# 
# **Hint:** you will need to `mun_dict` variable defined at the top of this notebook.
# 
# ```

# In[70]:


### START FUNCTION
def extract_municipality_hashtags(df):
    
    split_list=[]
    h_list=[]
    mun_list=[]

    for i in df["Tweets"]:
        
        split_list=i.split()
        c=0
        in_list=[]
        
        for a in split_list:
            if a.startswith("#"):
                in_list.append(a.lower())
                c+=1
        if c>0:
            h_list.append(in_list)
        else:
            h_list.append(np.nan)
            
        d=0
        for key in mun_dict:
            if key in i:
                mun_list.append(mun_dict[key])
                d+=1
        if d>0:
            pass
        else:
            mun_list.append(np.nan)
            
    df["municipality"] = mun_list        
    df["hashtags"] = h_list
    
    return df

### END FUNCTION


# In[69]:


extract_municipality_hashtags(twitter_df.copy())


# _**Expected Outputs:**_ 
# 
# ```python
# 
# extract_municipality_hashtags(twitter_df.copy())
# 
# ```
# > <table class="dataframe" border="1">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Tweets</th>
#       <th>Date</th>
#       <th>municipality</th>
#       <th>hashtags</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>@BongaDlulane Please send an email to mediades...</td>
#       <td>2019-11-29 12:50:54</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>@saucy_mamiie Pls log a call on 0860037566</td>
#       <td>2019-11-29 12:46:53</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>@BongaDlulane Query escalated to media desk.</td>
#       <td>2019-11-29 12:46:10</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>Before leaving the office this afternoon, head...</td>
#       <td>2019-11-29 12:33:36</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...</td>
#       <td>2019-11-29 12:17:43</td>
#       <td>NaN</td>
#       <td>[#eskomfreestate, #mediastatement]</td>
#     </tr>
#     <tr>
#       <th>...</th>
#       <td>...</td>
#       <td>...</td>
#       <td>...</td>
#       <td>...</td>
#     </tr>
#     <tr>
#       <th>195</th>
#       <td>Eskom's Visitors Centresâ€™ facilities include i...</td>
#       <td>2019-11-20 10:29:07</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>196</th>
#       <td>#Eskom connected 400 houses and in the process...</td>
#       <td>2019-11-20 10:25:20</td>
#       <td>NaN</td>
#       <td>[#eskom, #eskom, #poweringyourworld]</td>
#     </tr>
#     <tr>
#       <th>197</th>
#       <td>@ArthurGodbeer Is the power restored as yet?</td>
#       <td>2019-11-20 10:07:59</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>198</th>
#       <td>@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...</td>
#       <td>2019-11-20 10:07:41</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#     <tr>
#       <th>199</th>
#       <td>RT @GP_DHS: The @GautengProvince made a commit...</td>
#       <td>2019-11-20 10:00:09</td>
#       <td>NaN</td>
#       <td>NaN</td>
#     </tr>
#   </tbody>
# </table>

# ## Function 5: Number of Tweets per Day
# 
# Write a function which calculates the number of tweets that were posted per day. 
# 
# **Function Specifications:**
# - It should take a pandas dataframe as input.
# - It should return a new dataframe, grouped by day, with the number of tweets for that day.
# - The index of the new dataframe should be named `Date`, and the column of the new dataframe should be `'Tweets'`, corresponding to the date and number of tweets, respectively.
# - The date should be formated as `yyyy-mm-dd`, and should be a datetime object. **Hint:** look up `pd.to_datetime` to see how to do this.

# In[13]:


### START FUNCTION
def number_of_tweets_per_day(df):
    
    list1=[] #creating a blank list
    
    for i in df["Date"]:  #run loop through each row in Date column
        list1.append(i[0:10]) #slicing to remove just the date and appending it to blank list
 
    df['Date']  = list1  #making list into Date column
    
    fin = pd.DataFrame(df.groupby("Date").count().loc[:,"Tweets"]) #grouping date column by dates and counting dates
    return fin

### END FUNCTION


# In[14]:


number_of_tweets_per_day(twitter_df.copy())


# _**Expected Output:**_
# 
# ```python
# 
# number_of_tweets_per_day(twitter_df.copy())
# 
# ```
# 
# > <table class="dataframe" border="1">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Tweets</th>
#     </tr>
#     <tr>
#       <th>Date</th>
#       <th></th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>2019-11-20</th>
#       <td>18</td>
#     </tr>
#     <tr>
#       <th>2019-11-21</th>
#       <td>11</td>
#     </tr>
#     <tr>
#       <th>2019-11-22</th>
#       <td>25</td>
#     </tr>
#     <tr>
#       <th>2019-11-23</th>
#       <td>19</td>
#     </tr>
#     <tr>
#       <th>2019-11-24</th>
#       <td>14</td>
#     </tr>
#     <tr>
#       <th>2019-11-25</th>
#       <td>20</td>
#     </tr>
#     <tr>
#       <th>2019-11-26</th>
#       <td>32</td>
#     </tr>
#     <tr>
#       <th>2019-11-27</th>
#       <td>13</td>
#     </tr>
#     <tr>
#       <th>2019-11-28</th>
#       <td>32</td>
#     </tr>
#     <tr>
#       <th>2019-11-29</th>
#       <td>16</td>
#     </tr>
#   </tbody>
# </table>

# # Function 6: Word Splitter
# 
# Write a function which splits the sentences in a dataframe's column into a list of the separate words. The created lists should be placed in a column named `'Split Tweets'` in the original dataframe. This is also known as [tokenization](https://www.geeksforgeeks.org/nlp-how-tokenizing-text-sentence-words-works/).
# 
# **Function Specifications:**
# - It should take a pandas dataframe as an input.
# - The dataframe should contain a column, named `'Tweets'`.
# - The function should split the sentences in the `'Tweets'` into a list of seperate words, and place the result into a new column named `'Split Tweets'`. The resulting words must all be lowercase!
# - The function should modify the input dataframe directly.
# - The function should return the modified dataframe.

# In[39]:


### START FUNCTION
def word_splitter(df):
    
    tweet = df['Tweets'] #taking Tweet column data from dataframe and saving it as a new variable
    list1=[]             #intiating a blank list
    
    for i in tweet:     #run loop through each tweet 
        list1.append(i.lower().split()) #splitting words in tweet as a lowercase, appending it to blank lsit
        
            
    df["Split Tweets"] = list1 #making list into new column in dataframe
    
    return df

### END FUNCTION


# In[40]:


word_splitter(twitter_df.copy())


# _**Expected Output**_:
# 
# ```python
# 
# word_splitter(twitter_df.copy()) 
# 
# ```
# 
# > <table class="dataframe" border="1">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Tweets</th>
#       <th>Date</th>
#       <th>Split Tweets</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>@BongaDlulane Please send an email to mediades...</td>
#       <td>2019-11-29 12:50:54</td>
#       <td>[@bongadlulane, please, send, an, email, to, m...</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>@saucy_mamiie Pls log a call on 0860037566</td>
#       <td>2019-11-29 12:46:53</td>
#       <td>[@saucy_mamiie, pls, log, a, call, on, 0860037...</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>@BongaDlulane Query escalated to media desk.</td>
#       <td>2019-11-29 12:46:10</td>
#       <td>[@bongadlulane, query, escalated, to, media, d...</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>Before leaving the office this afternoon, head...</td>
#       <td>2019-11-29 12:33:36</td>
#       <td>[before, leaving, the, office, this, afternoon...</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...</td>
#       <td>2019-11-29 12:17:43</td>
#       <td>[#eskomfreestate, #mediastatement, :, eskom, s...</td>
#     </tr>
#     <tr>
#       <th>...</th>
#       <td>...</td>
#       <td>...</td>
#       <td>...</td>
#     </tr>
#     <tr>
#       <th>195</th>
#       <td>Eskom's Visitors Centresâ€™ facilities include i...</td>
#       <td>2019-11-20 10:29:07</td>
#       <td>[eskom's, visitors, centresâ€™, facilities, incl...</td>
#     </tr>
#     <tr>
#       <th>196</th>
#       <td>#Eskom connected 400 houses and in the process...</td>
#       <td>2019-11-20 10:25:20</td>
#       <td>[#eskom, connected, 400, houses, and, in, the,...</td>
#     </tr>
#     <tr>
#       <th>197</th>
#       <td>@ArthurGodbeer Is the power restored as yet?</td>
#       <td>2019-11-20 10:07:59</td>
#       <td>[@arthurgodbeer, is, the, power, restored, as,...</td>
#     </tr>
#     <tr>
#       <th>198</th>
#       <td>@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...</td>
#       <td>2019-11-20 10:07:41</td>
#       <td>[@muthambipaulina, @sabcnewsonline, @iol, @enc...</td>
#     </tr>
#     <tr>
#       <th>199</th>
#       <td>RT @GP_DHS: The @GautengProvince made a commit...</td>
#       <td>2019-11-20 10:00:09</td>
#       <td>[rt, @gp_dhs:, the, @gautengprovince, made, a,...</td>
#     </tr>
#   </tbody>
# </table>

# # Function 7: Stop Words
# 
# Write a function which removes english stop words from a tweet.
# 
# **Function Specifications:**
# - It should take a pandas dataframe as input.
# - Should tokenise the sentences according to the definition in function 6. Note that function 6 **cannot be called within this function**.
# - Should remove all stop words in the tokenised list. The stopwords are defined in the `stop_words_dict` variable defined at the top of this notebook.
# - The resulting tokenised list should be placed in a column named `"Without Stop Words"`.
# - The function should modify the input dataframe.
# - The function should return the modified dataframe.
# 

# In[12]:


### START FUNCTION
def stop_words_remover(df):
    
    list1=[] #initiating emply list1 and list2
    list2=[]
    
    for i in df["Tweets"]:                         #run loop through data each row in Tweets column
        list1.append(i.lower().split())            #splitting words in tweet as a lowercase, appending it to blank list1
    
    for a in list1:   #run a loop through list1
        list3=[]      #creating an empty temp list
        for j in a:   #run a loop into each list in list1
            
            if j in stop_words_dict['stopwords']:  #check if word is a stopword
       l         del j #delete word if it is a stopword
            else:
                list3.append(j) #append word to temp list if it is not a stopword
                
        list2.append(list3)  #add temp list to list2
        
    df["Without Stop Words"] = list2  #making list into new column in dataframe
    
    return df            
### END FUNCTION


# In[13]:


stop_words_remover(twitter_df.copy())


# _**Expected Output**_:
# 
# Specific rows:
# 
# ```python
# stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
# stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit']
# ```
# 
# Whole table:
# ```python
# stop_words_remover(twitter_df.copy())
# ```
# 
# > <table class="dataframe" border="1">
#   <thead>
#     <tr style="text-align: right;">
#       <th></th>
#       <th>Tweets</th>
#       <th>Date</th>
#       <th>Without Stop Words</th>
#     </tr>
#   </thead>
#   <tbody>
#     <tr>
#       <th>0</th>
#       <td>@BongaDlulane Please send an email to mediades...</td>
#       <td>2019-11-29 12:50:54</td>
#       <td>[@bongadlulane, send, email, mediadesk@eskom.c...</td>
#     </tr>
#     <tr>
#       <th>1</th>
#       <td>@saucy_mamiie Pls log a call on 0860037566</td>
#       <td>2019-11-29 12:46:53</td>
#       <td>[@saucy_mamiie, pls, log, 0860037566]</td>
#     </tr>
#     <tr>
#       <th>2</th>
#       <td>@BongaDlulane Query escalated to media desk.</td>
#       <td>2019-11-29 12:46:10</td>
#       <td>[@bongadlulane, query, escalated, media, desk.]</td>
#     </tr>
#     <tr>
#       <th>3</th>
#       <td>Before leaving the office this afternoon, head...</td>
#       <td>2019-11-29 12:33:36</td>
#       <td>[leaving, office, afternoon,, heading, weekend...</td>
#     </tr>
#     <tr>
#       <th>4</th>
#       <td>#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...</td>
#       <td>2019-11-29 12:17:43</td>
#       <td>[#eskomfreestate, #mediastatement, :, eskom, s...</td>
#     </tr>
#     <tr>
#       <th>...</th>
#       <td>...</td>
#       <td>...</td>
#       <td>...</td>
#     </tr>
#     <tr>
#       <th>195</th>
#       <td>Eskom's Visitors Centresâ€™ facilities include i...</td>
#       <td>2019-11-20 10:29:07</td>
#       <td>[eskom's, visitors, centresâ€™, facilities, incl...</td>
#     </tr>
#     <tr>
#       <th>196</th>
#       <td>#Eskom connected 400 houses and in the process...</td>
#       <td>2019-11-20 10:25:20</td>
#       <td>[#eskom, connected, 400, houses, process, conn...</td>
#     </tr>
#     <tr>
#       <th>197</th>
#       <td>@ArthurGodbeer Is the power restored as yet?</td>
#       <td>2019-11-20 10:07:59</td>
#       <td>[@arthurgodbeer, power, restored, yet?]</td>
#     </tr>
#     <tr>
#       <th>198</th>
#       <td>@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...</td>
#       <td>2019-11-20 10:07:41</td>
#       <td>[@muthambipaulina, @sabcnewsonline, @iol, @enc...</td>
#     </tr>
#     <tr>
#       <th>199</th>
#       <td>RT @GP_DHS: The @GautengProvince made a commit...</td>
#       <td>2019-11-20 10:00:09</td>
#       <td>[rt, @gp_dhs:, @gautengprovince, commitment, e...</td>
#     </tr>
#   </tbody>
# </table>
