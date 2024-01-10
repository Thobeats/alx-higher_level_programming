#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list.copy()
    for j, i in enumerate(list_copy):
        if i == search:
            list_copy[j] = replace
    return list_copy
