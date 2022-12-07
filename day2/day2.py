def read_file():
	return open('input.txt').readlines()


def sum_rounds():
	"""
		A - pedra 
		B - papel 
		C - tesoura
		X - pedra - vale 1
		Y - papel - vale 2
		Z - tesoura - vale 3
		[A, B, C] - oponente
		[X, Y, Z] - eu
		0 - caso eu perca
		3 - se for empate
		6 - caso eu vença

	"""
	input_file = read_file()
	sum_round = 0
	for _round in input_file:
		players = _round.split(' ')
		if players[0] == 'A':
			if players[1].split('\n')[0] == 'X': sum_round += 4
			elif players[1].split('\n')[0] == 'Y': sum_round += 8
			else: sum_round += 3
		elif players[0] == 'B':
			if players[1].split('\n')[0] == 'X': sum_round += 1
			elif players[1].split('\n')[0] == 'Y': sum_round += 5
			else: sum_round += 9	
		else:
			if players[1].split('\n')[0] == 'X': sum_round += 7
			elif players[1].split('\n')[0] == 'Y': sum_round += 2
			else: sum_round += 6
	print(sum_round)


def sum_rounds_part_two():
	"""
		X - precisa perder - vale 1
		Y - empata - vale 2
		Z - vence - vale 3
		[A, B, C] - oponente
		[X, Y, Z] - eu
		0 - caso eu perca
		3 - se for empate
		6 - caso eu vença

	"""
	input_file = read_file()
	sum_round = 0
	for _round in input_file:
		players = _round.split(' ')
		if players[0] == 'A':
			if players[1].split('\n')[0] == 'X': sum_round += 3
			elif players[1].split('\n')[0] == 'Y': sum_round += 4
			else: sum_round += 8
		elif players[0] == 'B':
			if players[1].split('\n')[0] == 'X': sum_round += 1
			elif players[1].split('\n')[0] == 'Y': sum_round += 5
			else: sum_round += 9	
		else:
			if players[1].split('\n')[0] == 'X': sum_round += 2
			elif players[1].split('\n')[0] == 'Y': sum_round += 6
			else: sum_round += 7
	print(sum_round)


if __name__ == '__main__':
	#sum_rounds()
	sum_rounds_part_two()
