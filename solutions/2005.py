lst = [raw_input().split() for i in range(5)]
brute_lst = []
for z in (1,3):
	for y in (1,2,3):
		for x in (1,2,3):
			if x != y and y != z and x != z:
				brute_lst.append([int(lst[0][x]) + int(lst[x][y]) + int(lst[y][z]) + int(lst[z][4]), (x, y, z)])
temp = min(brute_lst)
for i in range(len(temp)):
	if i == 0:
		print temp[i]
	else:
		print 1, temp[i][0] + 1, temp[i][1] + 1, temp[i][2] + 1, 5