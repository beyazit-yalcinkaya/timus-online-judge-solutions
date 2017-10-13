n = int(raw_input())
dic = {}
for i in range(n):
	dic.update({i+1 : map(int, raw_input().split())[:-1]})
lst = []
c = 0
while len(dic) > 0:
	pivot = max(dic, key = lambda x: len(dic[x]))
	if c % 2 == 0:
		lst.extend(dic[pivot])
		if pivot in lst:
			lst.remove(pivot)
		c += 1
	else:
		lst.extend([pivot])
		c += 1
	del dic[pivot]
lst = list(set(lst))
print len(lst)
for i in range(len(lst)):
	print lst[i],