
def getFirstSwimmer(p, first_swimmer, second_swimmer, third_swimmer):
	
	max_amongst_three = max(first_swimmer, second_swimmer, third_swimmer)
	if p > max_amongst_three:
		multiplier = (p // max_amongst_three) + 1
		first_swimmer *= multiplier
		second_swimmer *= multiplier
		third_swimmer *= multiplier

	return min(abs(p - first_swimmer), abs(p - second_swimmer), abs(p - third_swimmer))
	pass


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		p, a, b, c = map(int, input().split(' '))
		print(getFirstSwimmer(p, a, b, c))