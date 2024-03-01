#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    product = 0
    denominator = 0

    for i in my_list:
        product += i[0] * i[1]
        denominator += i[1]

    average = product / denominator
    return average
