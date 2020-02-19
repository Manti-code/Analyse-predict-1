### START FUNCTION
def number_of_tweets_per_day(df):
    """Returns the number of tweets per day.

    Parameters:
    ----------
    df: pandas dataframe
        The dataFrame from which the columns 'Date' and 'Tweets' are extracted from

    Returns:
    -------
    fin: pandas dataframe
        The output dataFrame with  index named 'Date' and column named 'Tweets'
    """

    date_list=[] #creating a blank list

    for i in df["Date"]:          #run loop through each row in Date column
        date_list.append(i[0:10]) #slicing to remove just the date and appending it to blank list

    df['Date']  = date_list       #making list into Date column

    fin = pd.DataFrame(df.groupby("Date").count().loc[:,"Tweets"])  #grouping date column by dates and counting dates
    return fin

### END FUNCTION
