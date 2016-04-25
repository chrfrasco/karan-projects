def collatz_conjecture(n):
	if n <= 1 or type(n) != int:
		print("Please enter an integer greater than one.\n")
		return

	count = 0

	while n != 1:
		count += 1
		if n%2 == 0:
			n = n/2
		else:
			n = 1 + n * 3

	return count
