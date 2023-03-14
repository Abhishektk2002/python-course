with open("numbers.txt",'r') as filetoread:
    contents=filetoread.readlines()
with open("evens.txt",'w') as filetowrite:
    for x in contents:
        if int(x)%2==0:
            filetowrite.write(x)
            filetowrite.write("\n")
            print(x)