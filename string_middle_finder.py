def get_middle(s):
    n = len(s)  # get length of string
    if n % 2 == 0:  # even length
        return s[n//2 - 1 : n//2 + 1]  # return 2 middle characters
    else:  # odd length
        return s[n//2]  # return the single middle character
