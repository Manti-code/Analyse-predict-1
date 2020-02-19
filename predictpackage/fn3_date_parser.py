### START FUNCTION
def date_parser(dates):
    """Returns date in yyyy-mm-dd format from 'yyyy-mm-dd hh:mm:ss' string input

    Parameters
    ----------
    dates: list

    Returns
    -------
    date_list: list
       date strings in the format yyyy-mm-dd
    """

    split_list=[]  #initiating empty list
    date_list=[]   #initiating empty list

    for i in dates:                       #running a for loop through input dates list
        split_list.append(i.split(" "))   #using split fn to seperate dtae and time, saving it to list 1

    for j in split_list:                  #run loop through list 1
        date_list.append(j[0])            #taking the first value in list i.e dates and saving into another list

    return date_list

### END FUNCTION
