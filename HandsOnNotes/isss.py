# name=str(input("Enter the name of the employee="))
# reg_no=int(input("Enter the register number="))
# designation=str(input("Enter the designation of the employee="))
# date_of_joining=str(input("Enter the date of joining in dd-mm-yy format="))
# phone_number=int(input("Enter the phone number"))
# employee_list=[name,reg_no,designation,date_of_joining,phone_number]
# print(employee_list)

# #salary details
# working_days=int(input("enter the number of working days="))
# leave_availed=int(input("enter the no of leaves availed="))
# perday_payment=int(input("enter the per day payment="))
# spl_incentives=int(input("enter the incentive value="))
# income_tax_percent=int(input("Enter the income tax percent="))
# salary_details=[working_days,leave_availed,perday_payment,spl_incentives,income_tax_percent]

# #calculating salary components
# basic_salary=((working_days -leave_availed)*perday_payment)+spl_incentives
# income_tax=basic_salary*(income_tax_percent/100)
# salary=basic_salary-income_tax

# employee_list.append(basic_salary)
# employee_list.append(income_tax)
# employee_list.append(salary)
# print(employee_list)


# for el in employee_list:
#     print("\n","Employee name=",el[0],"\n",
#           "Reg no=",el[1],"\n",
#           "Designation=",el[2],"\n",
#           "date of joining=",el[3],"\n",
#           "phone number=",el[4],"\n",
#           "basic salary=",el[5],"\n",
#           "income tax=",el[6],"\n",
#           "salary=",el[7])

num_employees = int(input("Enter the number of employees: "))

for i in range(num_employees):
    name = input("Enter employee name: ")
    eid = input("Enter employee ID: ")
    designation =input("Enter employee designation: ")
    date_of_joining = input("Enter date of joining (YYYY-MM-DD): ")
    phone_no = input("Enter employee phone number: ")

    employee = [name, eid, designation, date_of_joining, phone_no]
    print(employee)



for j in range(num_employees):
    working_days = int(input("Enter number of working days: "))
    leaves_availed = int(input("Enter number of leaves availed: "))
    pay_per_day = float(input("Enter pay per day: "))
    spl_incentive = float(input("Enter special incentive: "))
    tax_percentage = float(input("Enter income tax percentage: "))
    employee_details=[working_days, leaves_availed, pay_per_day, spl_incentive, tax_percentage]
    print(employee_details)
    
    # Calculation of salary
net_salary=[]
for k in employee_details:
    basic_salary = (working_days - leaves_availed) * pay_per_day
    income_tax = (tax_percentage / 100) * basic_salary
    net_salary = basic_salary + spl_incentive - income_tax

print(net_salary)
employee_details.append(net_salary)
print(employee_details)
    

# Display updated employee details with salary
print("\nEmployee Details with Salary:")
for emp in employee:
    print("Name:", emp[0])
    print("Employee ID:", emp[1])
    print("Designation:", emp[2])
    print("Date of Joining:", emp[3])
    print("Phone Number:", emp[4])
    print("Net Salary:", emp[5])
    print("=" * 40)