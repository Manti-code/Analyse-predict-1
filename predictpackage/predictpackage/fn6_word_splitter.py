### START FUNCTION
def word_splitter(df):
    """ Returns dataFrame with a new column of a list of indivdual words.
    Parameters
    -------
    df: pandas dataframe
        The dataFrame which contains the sentences(tweets) to be split into individual words
    Returns
    -------
    df: pandas dataframe
        The new dataFrame with a new column of a list of individual words.
    """
    tweet = df['Tweets']  #taking Tweet column data from dataframe and saving it as a new variable
    split_tweet=[]        #intiating a blank list

    for i in tweet:                             #run loop through each tweet
        split_tweet.append(i.lower().split())   #splitting words in tweet as a lowercase, appending it to blank lsit


    df["Split Tweets"] = split_tweet            #making list into new column in dataframe

    return df

### END FUNCTION
