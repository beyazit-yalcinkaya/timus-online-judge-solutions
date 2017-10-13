n = int(raw_input())
lst = [raw_input().split() for number in range(n)]
check_lst = []
for i in lst:
	check_lst.extend(i)
check_lst = sorted(list(set(check_lst)))
for i in lst:
	check_lst.extend(i)
main_dict = {0 : ["Isenbaev"]}
con = True
while con:
	pivot = main_dict[max(main_dict)]
	max_lev = max(main_dict)
	for name in pivot:
		for pick_lst in lst:
			if name in pick_lst:
				for item in pick_lst:
					if item != name:
						if (max_lev+1) not in main_dict.keys():
							main_dict.update({max_lev+1 : [item]})
						else:
							main_dict[max_lev+1] += [item]
				lst.remove(pick_lst)
	temp = [all(j not in i for j in main_dict[max(main_dict)]) for i in lst]
	if all(temp):
		for name in pivot:
			for pick_lst in lst:
				if name in pick_lst:
					for item in pick_lst:
						if item != name:
							if (max_lev+1) not in main_dict.keys():
								main_dict.update({max_lev+1 : [item]})
							else:
								main_dict[max_lev+1] += [item]
					lst.remove(pick_lst)
		con = False
if lst != []:
	lst_temp = []
	for i in lst:
		lst_temp.extend(i)
	main_dict.update({"undefined" : lst_temp})
other_dict = {}
for i in check_lst:
	for j in main_dict.keys():
		if i in main_dict[j]:
			if i not in other_dict.keys():
				other_dict.update({i : [j]})
			else:
				(other_dict[i]).append(j)

for i in sorted(other_dict.keys()):
	print i, min(other_dict[i])