#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    answer = 0
    
    try:
        for i in range(list_length):
            try:
                answer = my_list_1[i] / my_list_2[i]
                result.append(answer)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
            except (ValueError, TypeError):
                print("wrong type")
                result.append(0)
    finally:
        return result


