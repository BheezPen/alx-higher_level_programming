#!/usr/bin/python3
def search_replace(my_list, search, replace):
    another_list = []
    for i in my_list:
        if i == search:
            another_list.append(replace)
        else:
            another_list.append(i)
    return another_list
