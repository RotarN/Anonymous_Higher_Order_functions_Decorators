def extract_positive(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers


number_list = []
filter(lambda x: x > 0, number_list)
print(list(filter(lambda x: x > 0, number_list)))


@extract_positive
def extract_negative(numbers):
    negative_numbers = []
    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
    return negative_numbers
