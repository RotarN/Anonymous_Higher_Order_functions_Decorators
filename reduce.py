from functools import reduce
numbers = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y, numbers))
print(reduce(lambda a, b: a + b, filter(lambda x: x % 2 == 0, numbers)))
