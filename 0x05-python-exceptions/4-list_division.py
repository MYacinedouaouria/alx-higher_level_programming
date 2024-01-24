#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        try:
            if (isinstance(my_list_1[i], (int, float)) and
                    isinstance(my_list_2[i], (int, float))):
                list.append(my_list_1[i] / my_list_2[i])
            else:
                print("Wrong type")
                list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list.append(0)
        except IndexError:
            print("out of range")
            list.append(0)
        finally:
            continue
    return list
