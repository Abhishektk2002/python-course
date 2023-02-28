x=int(input("Enter your mark "))
if x>30:
	print("you have passed the exam")
	if x>=90:
		print("you have A+")
	if x>80 and x<90:
		print("you have A")
else:
	print("you have failed the exam")
print("end of program")
