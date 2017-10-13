n, k=map(int, raw_input().strip().split())
k=[k]*n
t=map(int, raw_input().strip().split())
r=map(lambda x, y: x-y, k, t)
print abs(sum(q for q in r if q<=0)), sum(w for w in r if w>0)