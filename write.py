filetoread=open("numbers.txt",'r')
contents=filetoread.readlines()
print(contents)
filetowrite=open("evens.txt",'w')#new file evens.txt is created here and the following elements copied to this
for x in contents:#in w elements change each time we run but in using a elements add downward
    if int(x)%2==0:
        filetowrite.write(x)
        filetowrite.write("\n")
        print(x)