lst = raw_input()
dic ={}
for i in lst:
	if i not in dic.keys():
		dic.update({i : 1})
	else:
		dic[i] += 1
print max(dic, key=dic.get)