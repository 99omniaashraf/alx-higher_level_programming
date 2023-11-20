#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    new_list = []
    for i in range(list_length):
        try:
            r = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            new_list.oppend(r)
    return new_list
                
