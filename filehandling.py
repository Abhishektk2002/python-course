file=open("numbers.txt",'r')
contents=file.readlines()
print(contents)
for x in contents:
    if int(x)%2==0:
        print(x)
file.close()