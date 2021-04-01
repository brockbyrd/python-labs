employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

#print(employee_file.readlines())

employee_file.close()