### START FUNCTION
def dictionary_of_metrics(items):

    """ Calculates the mean,median,min value,max value,variance and standard deviation for dataset

    Parameters
    ----------
    items: list

    Returns
    -------
    dict1: dictionary
        Resultant dictionary of calculated data
    """
    sorted_list = sorted(items)         #sort the list
    sum_list = sum(sorted_list)         #add elements in the list to get sum
    length_list = len(sorted_list)      #find the length of the list

    mean = sum_list/length_list   #calc mean by dividing sum of list by no. of elements in list
    mean_r = round(mean,2)        # round mean to 2 decimal places

    median = round(np.median(items),2)  #find the median, round to 2 decimals

    min_list2 = min(sorted_list)   #find the lowest value in list
    max_list2 = max(sorted_list)   #find the highest value in list

    list_diff_sq = []          #create an empty list
    for i in items:            #run a loop iterating through list
        a = (i-mean)**2        #take each value subtract the mean from it, then square that value
        list_diff_sq.append(a) #add the value to the new list

    variance = round(sum(list_diff_sq)/(length_list-1),2) #get sum of new list div by N-1 and rounded to 2 decimal places

    std_dev = round(variance**0.5,2) #calc sqrt of variance and round to 2 decimal places


    dict1 = {'mean':mean_r,'median':median,
             'var':variance,'std':std_dev,
             'min':min_list2,'max':max_list2}

    return dict1

### END FUNCTION
