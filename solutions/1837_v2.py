n = int(raw_input())
lst = [raw_input().split() for number in range(n)]
check_lst = []
for i in lst:
	check_lst.extend(i)
main_dict = {"Isenbaev" : [0]}
con = True
while con:
	for name in main_dict.keys():
		for pick_lst in lst:
			if name in pick_lst:
				for item in pick_lst:
					if item != name:
						if item not in main_dict.keys():
							main_dict.update({item : [min(main_dict[name]) + 1]})
						else:
							main_dict[item].append(min(main_dict[name]) + 1)
				lst.remove(pick_lst)
	if all([all(name not in j for name in main_dict.keys()) for j in lst]):
		for p in lst:
			for k in p:
				main_dict.update({k : ["undefined"]})
		con = False

for i in sorted(list(set(check_lst))):
	print i, min(main_dict[i])