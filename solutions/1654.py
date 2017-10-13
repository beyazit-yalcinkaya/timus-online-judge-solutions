inp = raw_input()
stack = [inp[0]]
lst = list(inp[1:])[::-1]
while lst != [] :
	item = lst.pop()
	if stack != [] :
		if 	item == stack[-1] :
			del stack[-1]
		else :
			stack.append(item)
	else :
		stack.append(item)
print "".join(stack)