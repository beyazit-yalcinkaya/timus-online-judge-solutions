n ,k = map(int, raw_input().split())
lst = [reduce(lambda x, y : x - y - 2, map(int, raw_input().split())) for i in range(n)]
out = k - 2 + sum(lst)
if out < 0 : print "Big Bang!"
else : print out