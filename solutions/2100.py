n = int(raw_input())
out = sum([2 if raw_input().split('+')[-1] == 'one' else 1 for i in range(n)]) * 100 + 200
if out == 1300: print 1400
else: print out