from functools import partial


def power(base, exponent):
	return base ** exponent


square_func = partial(power, exponent=2)
print(square_func(10))

cube_func = partial(power, exponent=3)
print(cube_func(4))

print(list(map(cube_func, [2, 3, 5, 10])))
