n = int(raw_input())
dic = {}
out = 0
for i in range(n):
	temp = raw_input()
	if temp not in dic.keys():
		dic.update({temp : 1})
	else:
		dic[temp] += 1
for i in dic.keys():
	if dic[i] >= 4:
		out += dic[i] / 4
print out