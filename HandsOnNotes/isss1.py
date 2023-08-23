num_employees = int(input("Enter the number of employees: "))

employees = []

for i in range(num_employees):
    name = input("Enter employee name: ")
    eid = input("Enter employee ID: ")
    designation = input("Enter employee designation: ")
    date_of_joining = input("Enter date of joining (YYYY-MM-DD): ")
    phone_no = input("Enter employee phone number: ")

    employee = [name, eid, designation, date_of_joining, phone_no]
    employees.append(employee)

for j in range(num_employees):
    working_days = int(input("Enter number of working days: "))
    leaves_availed = int(input("Enter number of leaves availed: "))
    pay_per_day = float(input("Enter pay per day: "))
    spl_incentive = float(input("Enter special incentive: "))
    tax_percentage = float(input("Enter income tax percentage: "))
    employee_details = [working_days, leaves_availed, pay_per_day, spl_incentive, tax_percentage]
    # Calculation of salary
    basic_salary = (working_days - leaves_availed) * pay_per_day
    income_tax = (tax_percentage / 100) * basic_salary
    net_salary = basic_salary + spl_incentive - income_tax
    employee_details.append(net_salary)
    employees[j].extend(employee_details)
# Display updated employee details with salary
print("\nEmployee Details with Salary:")
for emp in employees:
    print("Name:", emp[0])
    print("Employee ID:", emp[1])
    print("Designation:", emp[2])
    print("Date of Joining:", emp[3])
    print("Phone Number:", emp[4])
    print("Net Salary:", emp[10])
    print("=" * 40)
