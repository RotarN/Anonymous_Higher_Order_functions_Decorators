base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 5]
print(list(map(pow, base_numbers, powers)))
print(list(map(lambda x, y: x ** y, base_numbers, powers)))

# write with lambda instead of pow

students = [
	dict(id=0, credits=dict(math=9, physics=6, history=7, latin=8)),
	dict(id=1, credits=dict(math=6, physics=7, latin=10, history=9)),
	dict(id=2, credits=dict(history=8, physics=9, chemistry=10, math=10)),
	dict(id=3, credits=dict(math=5, physics=5, geography=7, history=9)),
]


def sum_credits(dict_elem):
	return sum(dict_elem['credits'].values()), dict_elem


def remove_sum_credits(decorated_student):
	return decorated_student[1]


print(students)
from pprint import pprint
pprint(students)
student_credits_rank = sorted(map(sum_credits, students), reverse=True)
pprint(student_credits_rank)

student_credits_rank_lmbd = sorted(map(lambda x: (sum(x['credits'].values()), x), students), reverse=True)
pprint(student_credits_rank_lmbd)
assert student_credits_rank == student_credits_rank_lmbd

student_list = list(map(remove_sum_credits, student_credits_rank))
pprint(student_list)

chemistry_high = sorted(student_list, key=lambda x: x['credits']['math'], reverse=True)
pprint(chemistry_high)
