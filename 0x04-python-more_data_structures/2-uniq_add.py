#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list = list(set(my_list))
    for k in my_list:
        sum += k
    return sum
