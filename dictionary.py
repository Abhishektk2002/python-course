x={"abhi":"1234","sidh":"4567","abhishek":"12345"}
username=input("Enter username \n")
correctpassword=x[username]
if username in x:
	password=input("Enter password \n")
	if password==correctpassword:
		print("login sucess")
	else:
		print("wrong password")
else:
	print("wrong username")
