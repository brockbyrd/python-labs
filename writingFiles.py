#appending to a file
#employee_file = open("employees.txt", "a")

#override or write a new file
employee_file = open("employees.txt", "w")
employee_file.write("Toby - Human Resources")

#uses new line character
employee_file.write("\nKelly - Customer Service")

employee_file.close()