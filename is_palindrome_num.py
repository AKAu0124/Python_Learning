import math

x = int(input("Enter a number: "))

def is_palindrome_num(x):
	if x <= 0:
		return 0
	# round a number down to nearest integer (math.floor) + 1
	num_digits = math.floor(math.log10(x)) + 1
	# 10 raise power of num_digits - 1
	msd_mask = 10 ** (num_digits - 1)
	# range == num_digits // 2 (round down to nearest integer)
	for i in range(num_digits // 2):
		if x // msd_mask != x % 10:
			return False
		x %= msd_mask
		x //=10
		msd_mask //= 100
	return True
print(is_palindrome_num(x))

