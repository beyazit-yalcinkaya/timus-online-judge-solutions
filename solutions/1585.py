n=int(raw_input().strip())
t=['Emperor Penguin', 'Little Penguin', 'Macaroni Penguin']
k=[raw_input().strip() for i in xrange(n)]
h=[k.count(q) for q in t]
print t[h.index(max(h))]