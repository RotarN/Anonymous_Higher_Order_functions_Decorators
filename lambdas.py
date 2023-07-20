def double(n):
	return n * 2


print(double(7))  # prints 7 * 2

# equivalent to
double = lambda x: x * 2
print(double(7))


def reverse(s):
	return s[::-1]


print(reverse('This is a string'))

# equivalent to
reverse = lambda s: s[::-1]
print(reverse('This is a string'))

# equivalent to
print((lambda s: s[::-1])('This is a string'))

some_lambda_func = lambda: 42
some_lambda_func()

some_lambda_func = lambda x: 42
some_lambda_func(4)

some_lambda_func = lambda x, y: x + y
some_lambda_func(4, 5)

# syntax_err = lambda x: return 2


even_odd = lambda x: print(f'{x} is an Even Number') if x % 2 == 0 else print(f'{x} is an Odd Number')
print((lambda x: f'{x} is an Even Number' if x % 2 == 0 else f'{x} is an Odd Number')(14))
even_odd(4)
even_odd(5)

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(3, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))

