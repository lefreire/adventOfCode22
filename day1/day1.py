def read_file():
	return open('input.txt').readlines()


def verify_input():
	input = read_file()
	best_elf = 0
	elf = 0
	for i in input:
		if i == '\n':
			if elf > best_elf: best_elf = elf
			elf = 0
		else:
			elf += int(i)
	if elf > best_elf: best_elf = elf
	print(best_elf)


def get_three_elf():
	input = read_file()
	best_elf = [0, 0, 0]
	elf = 0
	for i in input:
		if i == '\n':
			for i in best_elf:
				if elf > i: 
					best_elf[best_elf.index(min(best_elf))] = elf
					break
			elf = 0
		else:
			elf += int(i)
	for i in best_elf:
		if elf > i: 
			best_elf[best_elf.index(min(best_elf))] = elf
			break
	print(sum(best_elf))



if __name__ == '__main__':
	# verify_input()
	get_three_elf()