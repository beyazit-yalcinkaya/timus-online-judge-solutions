def register(inp):
	if inp[1] not in dic.keys():
		dic.update({inp[1] : inp[2]})
		out.append("success: new user added")
	else:
		out.append("fail: user already exists")
def login(inp):
	if inp[1] not in dic.keys():
		out.append("fail: no such user")
	else:
		if dic[inp[1]] != inp[2]:
			out.append("fail: incorrect password")
		else:
			if inp[1] not in lst:
				lst.append(inp[1])
				out.append("success: user logged in")
			else:
				out.append("fail: already logged in")
def logout(inp):
	if inp[1] not in dic.keys():
		out.append("fail: no such user")
	else:
		if inp[1] in lst:
			lst.remove(inp[1])
			out.append("success: user logged out")
		else:
			out.append("fail: already logged out")
n = int(raw_input())
dic = {'register' : register, 'login' : login, 'logout' : logout}
lst = []
out = []
for i in range(n):
	inp = raw_input().split()
	dic[inp[0]](inp)
for i in range(n):
	print out[i]