file=open("numbers.txt",'r')
contents=file.read()
contents=contents.split(',')
print(contents)
file.close()