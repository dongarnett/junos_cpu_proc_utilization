import math

def determine_list_highest_value(list_name):
    if len(list_name) > 0:
        list_max = max(list_name)
    else:
        list_max = 0.00
    return list_max

def determine_list_average(list_name):
    new_list = list_name
    element_cnt = len(new_list)
    if element_cnt > 0:
        sum_of_numbers = float(sum(new_list))
        avg = round(sum_of_numbers / element_cnt, 2)
    else:
        avg = 0.00
    return avg
