from numbers import Number


def addition(a: Number, b: Number, c=None, d=None) -> float:
    if c is None and d is None:
        return a + b
    elif d is None:
        return a + b + c
    else:
        return a + b + c + d


result1 = addition(10, 20)
result2 = addition(10, 20, 30)
result3 = addition(10, 20, 30, 40)

print(result1)
print(result2)
print(result3)