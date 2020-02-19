### START FUNCTION
def stop_words_remover(df):
    """ Removes stopwords from tweets and returns rest of the words from tweets.
    Parameters
    -------
    df: pandas dataframe
        The dataFrame which contains the sentences(tweets) to be split into individual words
    Returns
    -------
    df: pandas dataframe
        The new dataFrame with a new column of a list of individual words with stop words removed.
    """
    
    split_tweets=[] #Creating two empty lists
    no_stopwords=[]

    for i in df["Tweets"]:                      #Run loop through data each row in Tweets column
        split_tweets.append(i.lower().split())  #Splitting words in tweet as a lowercase, appending it to blank split_tweets


    for a in split_tweets:                          #Run a loop through split_tweets
        temp_list=[]                                #Creating an empty temp list
        for j in a:                                 #Run a loop into each list in list1

            if j in stop_words_dict['stopwords']:   #Check if word is a stopword. Delete word if it is a stopword
                del j
            else:
                temp_list.append(j)                 #Append word to temp list if it is not a stopword

        no_stopwords.append(temp_list)              #Add temp list to list2


    df["Without Stop Words"] = no_stopwords

    return df
### END FUNCTION
