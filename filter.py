# Example 1
print(list(filter(lambda number: number % 2 == 0, [1, 2, 3, 4, 5])))
# Example 2
print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))

# Example 3
my_list = [11, False, 18, 21, "", 12, 34, 0, [], {}]
print(list(filter(None, my_list)))

# Example 4
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))))

# Exercise 5
numbers = [-2, -1, 0, 1, 2]


def extract_positive(numbers):
	positive_numbers = []
	for number in numbers:
		if number > 0:
			positive_numbers.append(number)
	return positive_numbers

print(extract_positive(numbers))

# 1. write the equivalent of above code using filter() function
# 2. Replace filter() function with a generator expression
