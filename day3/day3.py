import string

def read_file():
	return open('input.txt').readlines()


def get_types():
	"""

	"""
	input_file = read_file()
	all_types = []
	for rucksack in input_file:
		all_types.extend(list(set(rucksack[:int(len(rucksack)/2)]).intersection(set(rucksack[int(len(rucksack)/2):]))))
	numbers = list(range(1, 27))
	letters =list(string.ascii_lowercase)
	sum_types = 0
	print(len(all_types))
	for i in all_types:
		res = 0
		if i >= 'a' and i <= 'z':
			sum_types += numbers[letters.index(i)]
			res = numbers[letters.index(i)]
		else:
			sum_types += numbers[letters.index(i.lower())]+26
			res = numbers[letters.index(i.lower())]+26
		print(i, res)
	print(sum_types)



if __name__ == '__main__':
	get_types()