#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except IndexError:
            result = 0
            print("out of range")
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        finally:
            pass
        new_list.append(result)
    return new_list
