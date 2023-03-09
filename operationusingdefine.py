def add(x,y):
	return x+y
def diff(x,y):
	return x-y
a=int(input("enter x"))
b=int(input("enter y"))
c=input("enter operation")
if c=="+":
	print(add(a,b))
else:
	print(diff(a,b))
