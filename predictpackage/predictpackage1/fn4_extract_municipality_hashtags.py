### START FUNCTION
def extract_municipality_hashtags(df):
    """ Extracts the municipality and hashtags from tweets. Adds extracted data to new columns

    Parameters
    ----------
    df: Pandas dataframe
       The dataframe which muncipality and hashtag will be added to.

    Returns
    -------
    df: Pandas dataFrame
          Returns data in a column named "hashtags" and a column named "municipality"
    """

    split_list=[]  #initiating empty lists
    h_list=[]
    mun_list=[]

    for i in df["Tweets"]:                      #run loop through tweets column

        split_list=i.split()                    #split each tweet
        flag1=False                             #creating a boolean variable
        in_list=[]                              #creating a blank inner list

        for a in split_list:                    #run loop through split tweet list
            if a.startswith("#"):               #extracting words that begin with a hashtag
                in_list.append(a.lower())       #making hashtag words to lowercase and appending it
                flag1=True                      #setting flag to true

        if flag1 == True:                       #checking flag condition
            h_list.append(in_list)              #append inner list to hashtag list
        else:
            h_list.append(np.nan)               #append a NuN

        flag2=False                             #declaring a new boolean variable
        for key in mun_dict:                    #looping through keys in dictionary
            if key in i:                        #finding if key is in tweet
                mun_list.append(mun_dict[key])  #appending value of key to municpality list
                flag2 = True                    #setting flag to true if key is found

        if flag2==True:                         #checking flag2 condition
            pass
        else:
            mun_list.append(np.nan)             #append NuN if flag condition is not met

    df["municipality"] = mun_list               #creating municipality column in df
    df["hashtags"] = h_list                     #creating hashtag column in df

    return df

### END FUNCTION
