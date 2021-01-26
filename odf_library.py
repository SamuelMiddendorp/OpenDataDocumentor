import json
from datetime import datetime
VERSION = "1.0"
SHALLOW = "shallow"
DEEP = "deep"
primitives = {str: "string", int: "integer", float: "float", bool: "boolean"}

def shallow_copy(data: dict) -> dict:
    if type(data) is list:
        return shallow_copy_list(data)
    elif(type(data) is str):
        with open(data, "r") as f:
            return shallow_copy(json.load(f))
    else:
        return shallow_copy_dict(data)
def shallow_copy_dict(data: dict) -> dict:
    odf_result = dict()
    #set date and method
    odf_result["created"] = datetime.now().strftime("%c")
    odf_result["documentType"] = SHALLOW
    odf_result["fields"] = dict()
    for key, value in data.items():
        d_type = type(value)
        if(d_type in primitives.keys()):
            odf_result["fields"][key] = primitives[d_type]
        else:
            odf_result["fields"][key] = recursive_add(value)
    return odf_result
def recursive_add(data: dict) -> dict:
    fields = dict()
    for key, value in data.items():
        d_type = type(value)
        if(d_type in primitives):
            fields[key] = primitives[d_type]
        else:
            fields[key] = recursive_add(value)
    return fields

def shallow_copy_list(data: list) -> dict:
    odf_result = dict()
    #set date and method
    odf_result["created"] = datetime.now().strftime("%c")
    odf_result["documentType"] = SHALLOW
    odf_result["fields"] = dict()
    record = data[0]
    if(record != None):
        for key, value in record.items():
            d_type = type(value)
            if(d_type in primitives.keys()):
                odf_result["fields"][key] = primitives[d_type]
            else:
                odf_result["fields"][key] = recursive_add(value)

    return odf_result

