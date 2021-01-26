from datetime import datetime
import json
from odd_utils import *

VERSION = "1.0"


def shallow_copy(data) -> dict:
    if type(data) is list:
        return traverse(data)
    elif(type(data) is str):
        with open(data, "r") as f:
            return shallow_copy(json.load(f))
    else:
        return traverse(data)
def traverse(data) -> dict:
    fields = dict()
    if(type(data) in odd_primitives):
        return odd_primitives[type(data)]
    elif(data is None or len(data) < 1):
        raise Exception("Data provided is either invalid or empty")
    elif(type(data) is list and len(data) > 0):
        temp_list = list()
        temp_list.append(traverse(data[0]))
        return temp_list
    elif(type(data) is dict and len(data) > 0):
        for key, value in data.items():
            d_type = type(value)
            if(d_type in odd_primitives):
                fields[key] = odd_primitives[d_type]
            elif(d_type is dict and len(value) > 0):
                fields[key] = traverse(value)
            elif(d_type is list and len(value) > 0):
                temp_list = list()
                temp_list.append(traverse(value[0]))
                fields[key] = temp_list
            else:
                fields[key] = odd.EMPTY.value
    else:
        fields[key] = odd.EMPTY.value
    return fields

