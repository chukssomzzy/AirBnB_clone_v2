#!/usr/bin/python3


import ast
p = re.compile(
    r'(?P<key>\w+)='
    r'(?:(?P<quote>[\'\"])(?P<string>.*?)(?P=quote)'
    r'|'
    r'(?P<integer>[-+]?\d+)'
    r'|(?P<float>(?:[-+]?\d+(?:\.\d+)?|\.\d+)(?:[eE][-+]?\d+)?)'
    r'|(?P<boolean>True|False)'
    r'|(?P<none>None)'
    r'|(?P<complex>(?:[-+]?\d+(?:\.\d+)?|\d*\.\d+)(?:[-+]?\d+[jJ])?)'
    r')'
)


def process_input(input_str):
    data_dict = {}
    for pair in input_str.split(r"(?!:)?\s"):
        print(pair)
        split_str = pair.split(r"=")
        print(split_str)
        key = split_str[0]
        value = split_str[1]
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            pass
        data_dict[key] = value
    return data_dict


input_string = "key1='vale1' key2=42 key3=True key4=None key5=3.14 key6=1+2j key7={'nested_key': 'nested_value'}"
parsed_data = process_input(input_string)
print(parsed_data)
