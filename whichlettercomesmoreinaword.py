x="abhishek"
y={}
for letter in x:
	if letter in y:
		y[letter]=y[letter]+1
	else:
		y[letter]=1
print(y)
z=0
for letter in y:
	if y[letter]>z:
		z=y[letter]
		c=letter
print(c)
