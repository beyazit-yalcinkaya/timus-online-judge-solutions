x, y, c = map(int, raw_input().split())
if ( x + y - c ) >= 0 :
	if ( c - x ) <= y and ( c - x ) >= 0 :
		print x, c - x
	elif ( c - y ) <= x and ( c - y ) >= 0 :
		print c - y, y
	elif c <= x :
		print c, 0
	elif c <= y :
		print 0, c
else:
	print "Impossible"