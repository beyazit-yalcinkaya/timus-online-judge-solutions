def fact(x):
	if x == 1: return 1
	else: return x * fact(x-1)
n = int(raw_input())
lst = raw_input().split()
main_dict = {}
for i in lst:
	if i in main_dict:
		main_dict[i] += 1
	else:
		main_dict.update({i : 1})
out = 1
for i in main_dict.keys():
	out *= fact(main_dict[i])
if (fact(n) - n * out) >= 6:
	print 'Yes'
else:
	'No'