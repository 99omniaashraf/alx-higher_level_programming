#!/usr/bin/env python3
def no_c(my_string):
    new_str = list(my_string)
    for i in new_str:
        if i == 'c' or i == 'C':
            new_str.remove(i)
    return("".join(new_str))
