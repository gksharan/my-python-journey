def count_by(x=2, n=5):
    result = []
    for i in range(1, n+1):
        multiple = x * i
        result.append(multiple)
    return result

print(count_by(2, 5))
