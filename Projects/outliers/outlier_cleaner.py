#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    data = []

    for i in range(len(ages)):
        error = (net_worths[i][0]-predictions[i][0]) ** 2
        data.append((ages[i][0], net_worths[i][0], error))

       

    for i in range(0, len(data), 1):
        for j in range(0, len(data)-1, 1):
            if data[j][2] > data[j+1][2]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

    cleaned_data = data[:int(len(data)*0.9)]

    
    return cleaned_data

