def is_happy(n):
	left = sum([int(x) for x in str(n//1000)])
	right = sum([int(x) for x in str(n%1000)])

	return left == right


print(len([x for x in range(1000000) if is_happy(x)]))

