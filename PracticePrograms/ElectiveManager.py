#Your class teacher wants to finish some of the tasks, will you help her out? Feel free
# to use the concepts of lists, tuples, sets and dictionary implement the following
# tasks:
#  Storing the details of the students who have taken foundational electives
# (minimum 5 in stats and 5 in programming)
#  Calculating the grade of the student
#  Find out the absentees of the foundational elective

def get_valid_name():
    while True:
        name = input("Enter Name of the student based on the list.: ")
        if is_valid_name(name):
            return name
        else:
            print("Name already exist")
def is_valid_name(name):
    if name in StudentDataCS.keys():
        return False
    return True
def add_student_CS(StudentDataCS, name, phone_number, email, mark):
    if name not in StudentDataCS:
        StudentDataCS[name] = (phone_number, email, mark)
        print(f"Data of '{name}' added successfully.")
    else:
        print(f" '{name}' already exists in the StudentData.")

def add_student_Stats(StudentDataStats, name, phone_number, email, mark):
    if name not in StudentDataStats:
        StudentDataStats[name] = (phone_number, email, mark)
        print(f"Data of '{name}' added successfully.")
    else:
        print(f" '{name}' already exists in the StudentData.")

def remove_student_CS(StudentDataCS, name):
    if name in StudentDataCS:
        del StudentDataCS[name]
        print(f"Data of '{name}' deleted successfully.")
    else:
        print(f"Data of  '{name}' not found in the StudentData.")

def remove_student_Stats(StudentDataStats, name):
    if name in StudentDataStats:
        del StudentDataStats[name]
        print(f"Data of '{name}' deleted successfully.")
    else:
        print(f"Data of  '{name}' not found in the StudentData.")

def display_grade(StudentDataCS, StudentDataStats, name, mark):
    if name in StudentDataCS or StudentDataStats:
        if mark >80:
            gradee = "A"
            print(f"{name} got A grade.\n")
        elif (mark>60 and mark<=80):
            print(f"{name} got B grade.\n")
        elif (mark>40 and mark<=60):
            print(f"{name} got C grade.\n")
        else:
            print(f"{name} got D grade. Study well!\n")
    else:
        print(f"Data of {name} not found.")



CS_students = ['Kiya Jolley','Isaac Cote','Isaak Matlock','Kalli Connor','Dyllan Haynes','Bayleigh Ricker']
Stats_students = ['Francisco Fraser','Brayden Espinosa','Brayden Espinosa','Alfred Straub','Marina Bartholomew','Conrad Santos','Roland Tatum']

StudentDataCS = {}
StudentDataStats = {}
mark = 0
print("Welcome to Foundation elective manager.")
print("-------------------------------------------Students List for Foundation elective------------------------------------------")
print("For CS Elective: \n" ,CS_students)
print("For Statistics Elective: \n" ,Stats_students)
while True:
    print("Press 1 for Programming Foundation elective.\n"+"Press 2 for Statistics Foundation elective.\n"+ "Press 3 to Quit")
    f_ch = int(input())
    if f_ch == 1:
        print("Press 1 to add Student\n"+ "Press 2 to remove a student\n" + "Press 3 to display the grades of the student.\n" + "Press 4 to find the absentees in CS Programming elective.\n" +"Press 5 to Quit\n")
        ch = int(input())
        if ch ==1:
            name = get_valid_name()
            phone_number = int(input("Enter Phone Number: "))
            email = input("Enter Email: ")
            mark = int(input("Enter the mark obtained: "))
            add_student_CS(StudentDataCS, name, phone_number, email, mark)
        elif ch == 2:
            name = input("Enter the name of the student to be removed: ")
            remove_student_CS(StudentDataCS, name)
        elif ch ==  3:
            name = input("Enter the name of the student whose grade has to be displayed:  ")
            display_grade(StudentDataCS, StudentDataStats, name, mark)
        elif ch == 4:
            Set_CS = set(CS_students)
            Set_CS1 = set(StudentDataCS.keys())
            absentees = sorted(Set_CS.difference(Set_CS1 ))
            print("The absentees are:")
            print(absentees)
        elif ch == 5:
            break
        else:
            print("Invalid choice. Try again.")
    elif f_ch ==2:
        print("Press 1 to add Student\n"+ "Press 2 to remove a student\n" + "Press 3 to display the grades of the student.\n"+"Press 4 to find the absentees in Statisitics elective.\n" + "Press 5 to Quit\n")
        ch = int(input())
        if ch ==1:
            name = get_valid_name()
            if name in StudentDataStats.keys():
                print(f"{name} already exist.")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            mark = int(input("Enter the mark obtained: "))
            add_student_Stats(StudentDataStats, name, phone_number, email, mark)
        elif ch == 2:
            name = input("Enter the name of the student to be removed: ")
            remove_student_Stats(StudentDataStats, name)
        elif ch ==  3:
            name = input("Enter the name of the student whose grade has to be displayed:  ")
            display_grade(StudentDataCS, StudentDataStats, name, mark)
        elif ch == 4:
            Set_Stats = set(Stats_students)
            Set_Stats1 = set(StudentDataStats.keys())
            absentees = sorted(Set_Stats.difference(Set_Stats1 ))
            print("The absentees are:")
            print(absentees)
        elif ch == 5:
            break
        else:
            print("Invalid choice. Try again.")
    else:
        break