def decorator_1(func):
	def wrapper(*args, **kwargs):
		print('start')
		result = func(*args, **kwargs)
		print('end')
		return result
	return wrapper


@decorator_1
def say_hello():
	print('hello')


say_hello()