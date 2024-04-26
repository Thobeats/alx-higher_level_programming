#!/usr/bin/python3
complex_delete = __import__('102-complex_delete').complex_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

my_dict = { 'a': "a", 'b': "b" , 'c': "c", 'd': "d", 'e': "e" }
value = 'a'
new_dict = complex_delete(my_dict, value)
print_sorted_dictionary(my_dict)
print("xx")
print_sorted_dictionary(new_dict)
