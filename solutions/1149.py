n = int(raw_input())
def A(n):
	if n == 1:
		return "sin(" + str(n)
	if n % 2 == 1:
		return A(n-1) + "+sin(" + str(n)
	else:
		return A(n-1) + "-sin(" + str(n)
def S(n, x = 1):
	if n == 1:
		return  A(x) + ")" * x + "+" + str(n)
	return A(x) + ")" * x + "+" + str(n) + ")" + S(n-1, x + 1)
print "(" * (n - 1) + S(n)