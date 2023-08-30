import re
import os
class NoPatientAgesFoundException(Exception):
    pass
class Automate:
    def __init__(self, content):
        while True:
            print("Enter 1 to identify the Name of the Patient\nEnter 2 to identify the date of the report\nEnter 3 to identify the Email id of the technician\nEnter 4 to identify the Name of the Doctor\nEnter 5 to identify the Age of the Patient\nEnter 6 to identify Website if any\nEnter 7 to identify Replace the domain from .com to .in")
            ch = int(input("Enter the choice according to the condition above.\n"))
            if ch ==1:
                try:
                    patient_names = re.findall(r"Name of the Patient: (.+)", content)
                    for name in patient_names:
                        print(name)
                except NameError:
                    print("Can't find the name with respect to the pattern entered")
            elif ch == 2:
                report_dates = re.findall(r"Date of report: (.+)", content)
                for date in report_dates:
                    print(date)
            elif ch ==3:
                lab_technician_emails = re.findall(r"Email id of the lab technician: (\S+)", content)
                for email in lab_technician_emails:
                    print(email)
            elif ch ==4:
                doctor_names = re.findall(r"Name of the Doctor: (Dr\. .+)", content)
                for doctor in doctor_names:
                    print(doctor)
            elif ch ==5:
                try:
                    patient_ages = re.findall(r"Age of the patient: (\d+)", content)
                    if not patient_ages:
                        raise NoPatientAgesFoundException("No patient ages found in the content.")
                    
                    print("The age of the patients are:")
                    for age in patient_ages:
                        print(age)
                except NoPatientAgesFoundException as e:
                    print(e)
            elif ch ==6:
                websites = re.findall(r"Website if any: (www\.\S+)?", content) # add all the white space chatracter after this
                for website in websites:
                    print(website)
            elif ch ==7:
                updated_data = re.sub(r"(www\.\S+)\.com", r"\1.in", content) #\1: This is a special reference to the first capturing group (the part in parentheses) in the original pattern. In this case, it refers to the captured website URL without the ".com" part. and add .in
                print(updated_data)
            elif ch <1 or ch>9:
                print("Enter a valid input")
            else:
                break


print("Welcome to Women and Child Development Department Health Record Automation")
try:
    directory = "LabPrograms"
    file_name = input("Enter the file name with the format")
    file_path = os.path.join(directory, file_name)
    with open(file_path,'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file 'maternity.txt' was not found.")
data = Automate(content)