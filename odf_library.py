import json
from datetime import datetime
VERSION = "1.0"
SHALLOW = "shallow"
DEEP = "deep"
type_dict = {str: "string", int: "integer", bool: "boolean"}

def shallow_copy(data: dict) -> dict:
    if type(data) is list:
        return shallow_copy_list(data)
    elif(type(data) is str):
        with open(data, "r") as f:
            return shallow_copy(json.load(f))
    else:
        return shallow_copy_dict(data)
def shallow_copy_dict(data: dict) -> dict:
    types = dict()
    #set date and method
    types["created"] = datetime.now()
    types["documentType"] = SHALLOW
    for key, value in data.items():
            d_type = type(value)
            types[key] = str(d_type)
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
            odf_result["fields"][key] = type_dict[d_type]
    return odf_result

