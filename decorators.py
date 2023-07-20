def my_decorator(f):
	def inner(*args):
		print(f"Calling function '{f.__name__}' with args {args}'")
		return f(*args)
	return inner


@my_decorator
def my_print(x):
	print(f"With argument '{x}'")


my_print('string arg')
# or remove the decorator and call it manually
# enhanced_func = my_decorator(my_print)
# enhanced_func('string arg')


def document_it(func):
	def new_function(*args, **kwargs):
		print('Running function:', func.__name__)
		print('Positional arguments:', args)
		print('Keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('Result:', result)
		return result
	return new_function


def add_ints(a, b):
	return a + b


documented_add_ints = document_it(add_ints)
documented_add_ints(67, 33)
# or with named arguments
documented_add_ints(a=67, b=33)


# or use @ decorator syntax
@document_it
def add_ints(a, b):
	return a + b


add_ints(12, 23)


def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		return result * result
	return new_function


@document_it
@square_it
def add_ints(a, b):
	return a + b


result = add_ints(11, 22)
print(result)


@square_it
@document_it
def add_ints(a, b):
	return a + b


result = add_ints(11, 22)
print(result)
