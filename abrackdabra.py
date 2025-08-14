#method 1
new_string = s[:pos] + char + s[pos+1:]


#method 2
l = list(s)
l[pos] = char
new_string = ''.join(l)
