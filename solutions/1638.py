a, b, c, d = map(int, raw_input().split())
if (d - c) > 0:
	print (d-c)*(2*b+a)-a
elif (d-c) < 0:
	print (c-d)*(2*b+a)+a
else:
	print a