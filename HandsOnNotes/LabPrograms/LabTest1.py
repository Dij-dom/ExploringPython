class StudentDictionary:
    def __init__(self):
        self.students = {}
    def add_student(self, reg_no, name, gender, email):
        self.students[reg_no] = {"name": name, "gender": gender, "email": email}
    def get_register_numbers(self):
        return list(self.students.keys())
    def get_emails(self):
        return tuple(student["email"] for student in self.students.values())
    def mark_attendance(self):
        lab_attendance = set()
        lab_register = set(self.students.keys())
        absen = int(input("How many absentees?"))
        print("Enter the register number of the absentees.")
        for i in range(absen):
            print(f"Enter the register number of the student {i+1}")
            reg = int(input())
            lab_attendance.add(reg)
        print("The absentees are ", lab_register.difference(lab_attendance))
    def cal_cum_sum_avg(self,marks_list):
        valid_marks = []
        valid_marks = [valid_marks.append(mark) for mark in marks_list if isinstance(mark,int)]
        cal_total_marks = lambda marks: sum(mark for mark in valid_marks)
        total_marks = cal_total_marks(marks_list)
        print(f"The total marks obtained is {total_marks}")
        valid_marks = [marks_listv.append(i) for i in marks_list if isinstance(i,int)]
        avg = total_marks/len(valid_marks)
        print(f"The class average is {avg}")

student_dict = StudentDictionary() #object of the class Student Dictionary

for i in range(1, 6):
    print(f"Enter details for Student {i}:")
    name = input("Name: ")
    reg_no = input("Register Number: ")
    gender = input("Gender: ")
    email = input("Email: ")
    student_dict.add_student(reg_no, name, gender, email) #calling the method in the StudentDictionary class using it's object student_dict

#to get the register number of the students
register_numbers = student_dict.get_register_numbers()
#to get the mail-id's of the student
emails = student_dict.get_emails()

#to get the absentees details
absentees = student_dict.mark_attendance()

marks_list = [13, 18, 20, 'Ab', 0] #given list of marks
student_dict.cal_cum_sum_avg(marks_list)