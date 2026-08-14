def swap_case_iterative(s):
    new_string = []
    for char in s:
        if char.islower():
            new_string.append(char.upper())
        elif char.isupper():
            new_string.append(char.lower())
        else:
            new_string.append(char)
    return "".join(new_string)