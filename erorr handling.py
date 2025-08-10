x = 47
y = 0
print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print("not allowed to divided by zero")
else:
    print("something went wrong")
finally:
    print("this is our cleanup code")