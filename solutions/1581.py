n = int(raw_input())
lst = raw_input().split()
stack = [lst[0]]
s_lst = lst[1:]
while True:
	if s_lst == []:
		print len(stack), stack[-1]
		break
	if s_lst[0] == stack[-1]:
		stack.append(s_lst[0])
		s_lst = s_lst[1:]
	else:
		print len(stack), stack[-1],
		stack = [s_lst[0]]
		s_lst = s_lst[1:]