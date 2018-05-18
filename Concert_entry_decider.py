#The program allows a concert organizer to decide on whether to allow the individual an entry to the concert based on their age and also
#validated if they can drink also.

#ask age at the counter
age = input("Please provide your age: ")

#verify proff
if age:
	age = int(age)
	if age >= 21:
		print("Please enter and you are allowed to drink, Enjoy the concert!!")
	elif age > 18:
		print("Please enter and you are not allowed to drink and always wear the wrist band, Enjoy!!")
	else:
		print("Sorry you are too young, we cannot allow you:(")
else:
	print("please provide age")
