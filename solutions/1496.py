n = int(raw_input())
word_dict = {}
for i in range(n):
	temp = raw_input()
	if temp in word_dict:
		word_dict[temp] += 1
	else:
		word_dict.update({temp: 1})
for i in word_dict.keys():
	if word_dict[i] > 1:
		print i