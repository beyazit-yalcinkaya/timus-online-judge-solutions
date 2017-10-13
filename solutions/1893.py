inp = raw_input().strip()
num = int(inp[:-1])
let = inp[-1]
ans='neither'
if num <= 2:
    if let=='A' or let=='D':
        ans = 'window'
    else:
        ans = 'aisle'
elif num <= 20:
    if let=='A' or let=='F':
        ans = 'window'
    else:
        ans = 'aisle'
elif num <= 65 and num >= 21:
    if let=='A' or let=='K':
        ans = 'window'
    elif let=='C' or let=='D' or let=='G' or let=='G' or let=='H':
        'aisle'
    else:
        ans = 'neither'
print ans
