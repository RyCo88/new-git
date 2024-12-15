def is_paired(input_string):
    brackets = '()[]}{'
    new_string = ''
    if brackets in input_string:
        for char in input_string:
            if char in brackets:
                new_string += char
    if new_string.count('(') != new_string.count(')') and new_string.count('[') != new_string.count(']') and new_string.count('{') != new_string.count('}'):
        return False
    if new_string[0] == '(':
        if new_string[-1] == ')':
            if len(new_string) > 2:
                if new_string[1] == '[' and new_string[-2] == ']':
                    return True
                if new_string[1] == '{' and new_string[-2] == '}':
                    return True
                return False
            return True
    if new_string[0] == '[':
        if new_string[-1] == ']':
            if len(new_string) > 2:
                if new_string[1] == '(' and new_string[-2] == ')':
                    return True
                if new_string[1] == '{' and new_string[-2] == '}':
                    return True
                return False
            return True
    if new_string[0] == '{':
        if new_string[-1] == '}':
            if len(new_string) > 2:
                if new_string[1] == '[' and new_string[-2] == ']':
                    return True
                if new_string[1] == '(' and new_string[-2] == ')':
                    return True
                return False
            return True