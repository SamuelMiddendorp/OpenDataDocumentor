from enum import Enum

odd_primitives = {str: "string", int: "integer", float: "float", bool: "boolean"}

class odd(Enum):
    SHALLOW = "shallow"
    DEEP = "deep"
    LIST = "list"
    DICT = "dict"
    EMPTY = "empty"