### START FUNCTION
import numpy as np
def five_num_summary(items):
    """" Calculates the min,max,median,first quartile and third quartile of input data
    Paremeters
    -----------
    items: list

    Returns
    -------
    dict1: dictionary
        Resultant dictionary of calculated data
    """
    sorted_list = sorted(items)  #sorting the input list and saving it in a new variable
    min_list = min(sorted_list)  #finding the minimum value of list1 and saving it in a variable
    max_list = max(sorted_list)  #finding the maximum value of list1 and saving it in a variable

    median = np.median(items)    #using median fintion from mumpy to find the median of input values

    q1 = np.quantile(items,0.25) #using quantile method from numpy to find the first quantile
    q3 = np.quantile(items,0.75) #using quantile method from numpy to find the third quantile


    dict1 = {'max':max_list,'median':median,'min':min_list,'q1':q1,'q3':q3}

    return dict1

### END FUNCTION
