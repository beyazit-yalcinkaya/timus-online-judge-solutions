i, ii, iii, iv, r1, r2, r3 = map(int, raw_input().split())
lst = [(ii + iii + iv) % 2 == r1, (i + iii + iv) % 2 == r2, (i + ii + iv) % 2 == r3]
if lst.count(True) == 0:
	iv = 1 - iv
elif lst.count(True) == 1:
	if lst.index(True) == 0:
		i = 1 - i
	elif lst.index(True) == 1:
		ii = 1 - ii
	elif lst.index(True) == 2:
		iii = 1 - iii
elif lst.count(True) == 2:
	if lst.index(False) == 0:
		r1 = 1 - r1
	elif lst.index(False) == 1:
		r2 = 1 - r2
	elif lst.index(False) == 2:
		r3 = 1 - r3
print i, ii, iii, iv, r1, r2, r3