# def decorator_1(func):
#     def iner_func(*args):
#         print(f"calling function {func.__name__}")
#         return func(*args)
#     return iner_func
#
# @decorator_2
# @decorator_1
# def func_main(a):
#     print(a)
#
#
# func_main(3)
# # decorator_1(func_main)(3)
#

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def square_it(func):
    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        square_r = result ** 2
        print(square_r)
        return square_r
    return inner_func



@square_it
@document_it
def add_ints(a, b):
    return a + b


add_ints(2, 5)


# document_it(add_ints)


@document_it
def square(a):
    return a ** 2


# print(square(4))




