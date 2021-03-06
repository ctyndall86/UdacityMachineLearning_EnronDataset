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
   ### your code goes here
    for i in range(len(predictions)):
        cleaned_data.append((ages[i], net_worths[i], net_worths[i] - predictions[i]))
        cleaned_data = sorted(cleaned_data, key = lambda x:x[-1], reverse = True)
        cleaned_data = cleaned_data[:int(0.9*len(predictions))] #grab only first 90% of values
    
    return cleaned_data

