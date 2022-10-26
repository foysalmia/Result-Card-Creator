from pyautogui import alert
import json
from pdfCreator import pdf_generate

admins = [{'name': 'amit', 'pass': '12345'},
          {'name': 'foysal', 'pass': '54321'}]
students = []

try:
    file = open('database.json')
    students = json.load(file)
    file.close()
    print("Successfully Loaded data from database")
except:
    print("No data in database")


class Student:
    def __init__(self, name, className, roll) -> None:
        self.name = name
        self.className = className
        self.roll = roll
        self.marks = {}

    def addMarks(self, subject, mark):
        self.marks[subject] = mark


isAdmin = False
while True:
    option = input("Are you admin/student ? (a/s) : ")
    if option == 'a':
        name = input("Enter Admin Name : ")
        password = input('Enter Admin Password : ')
        for x in admins:
            if x['name'] == name and x['pass'] == password:
                isAdmin = True
                print(f"Congrats {name} , You are logged in as an Admin ")
        while isAdmin:
            opt = input("Do you want add student (Y/N) :").lower()
            if opt == 'y':
                st_name = input("Student Name : ")
                st_class = input("Student class : ")
                st_roll = input("Student roll : ")
                student = Student(st_name, st_class, st_roll)
                number = int(input("How many subject : "))
                for i in range(number):
                    subject_name = input(f'Subject {i+1} Name : ')
                    mark = int(input(f"Enter mark {i+1} :"))
                    student.addMarks(subject_name, mark)
                students.append(student.__dict__)
            else:
                break

    elif option == 's':
        class_name = input("Enter your class : ")
        roll = input("Enter your roll :")

        for k in students:
            if k['className'] == class_name and k['roll'] == roll:
                response = pdf_generate(k)
                if response:
                    alert(
                        f"{k['name']},Your result downloaded successfully . Please Check the root directory")
                    break
                else:
                    alert(
                        f"{k['name']}, your result is not created. Please try again later..")
                    break
    else:
        with open('database.json', 'w') as file:
            json.dump(students, file)
        break

file.close()
