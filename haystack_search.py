def find_needle(haystack):
    for i in range(len(haystack)):   # loop over indexes
        if haystack[i] == "needle":
            return f"found the needle at position {i}"
