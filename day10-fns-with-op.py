def format_name(f_name,l_name):
	if(f_name == "" or l_name == ""):
		return "Invalid input!!!"
	return f"{f_name.title()} {l_name.title()}"	


f_name = input("Enter your first name : ")
l_name = input("Enter your last name : ")
print(format_name(f_name, l_name))
