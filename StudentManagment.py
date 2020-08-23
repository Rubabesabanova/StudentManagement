# OOP
class Student:
    def __init__(self, name, surname, email, phone, code):
        self.studentname = name.capitalize()
        self.studentsurname = surname.capitalize()
        self.studentemail = email
        self.studentphone = phone
        self.studentcode = code

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
# FUNCTIONS

# Main functions of program
# Deleting student according to ID
def DeleteForCode(deletecode):
    IsDeleteForCode=False
    for i in students:
        if i.studentcode == deletecode:
            students.remove(i)
            print("You deleted the student sucessfully !")
            IsDeleteForCode=True
    if not IsDeleteForCode:
        print('There is no such student !')
# Changing student according to ID
def ChangeForCode(changecode):
    IsChangeCode = True
    for i in students:
        if i.studentcode == changecode:
            name = input("Student name : ").lower()
            name = FillGaps(name)
            name = CheckLength(name, 1)
            name = CheckLetters(name, "name")
            surname = input("Student surname : ").lower()
            surname = FillGaps(surname)
            surname = CheckLength(surname, 1)
            surname = CheckLetters(surname, "surname")
            email = input("Student e-mail : ").lower()
            email = FillGaps(email)
            email = CheckLength(email, 3)
            email = CheckStudentEmail(email)
            phone = input("Student Phone Number : ")
            phone = FillGaps(phone)
            phone = CheckPhoneNumber(phone)
            i.studentname = name.capitalize()
            i.studentsurname = surname.capitalize()
            i.studentemail = email
            i.studentphone = phone
            break
        else:
            IsChangeCode = False
    if not IsChangeCode:
         print("Such student doesn't exist")
# Showing the information according to Name
def ShowForName(showname):
    IsShowForName = False
    for i in students:
        if i.studentname == showname.capitalize():
            IsShowForName = True
            print('''Student Name : {}
Student Surname : {} 
Student Email : {}
Student Phone Number : {}
Student Code : {}'''.format(i.studentname, i.studentsurname, i.studentemail, i.studentphone, i.studentcode))
    if IsShowForName == False:
        print("There is no such student")
#Showing the information of all students
def ShowAll():
    for i in students:
        print('''Information about student({}): 
Student Name : {}
Student Surname : {}
Student Email : {}
Student Phone Number : {}
Student Code : {}'''.format(i.studentcode, i.studentname, i.studentsurname, i.studentemail, i.studentphone, i.studentcode))

# Common functions
def InputInfo():
    operation = input('''What do you want to do ?
For full information about keywords type "info" or "i" : ''').lower()
    return operation
# The information about keywords
def FullInputInfo():
    operation = input('''If you want to add a new student, type "add" or "a",
If you want to delete the particular student, type "delete" or "d",
If you want to change the information of the particular student , type "change" or "c" ,
If you want to see the information of the particular student, type "student" or "s",
If you want to see the information of all students, type "all" or "l", 
If you want to quit, type "quit" or "q",
What do you want to do ? : ''').lower()
    return operation
# Input validation
# Cheking if the input is empty
def FillGaps(x):
    while not x:
        x = input("Please fill the gaps : ")
    return x
# Validation of Student Code
def CheckStudentCode(x):
    for i in students:
         if x==i.studentcode:
            x=input("This ID is already taken. Enter new ID : ")
    while not x.isdigit() or len(x) != 3:
        x = input("Please enter 3 digits of positive number : ")
    else:
        print("You added a new student successfully !")
    return x
#Validation of Student Email
def CheckStudentEmail(x):
    emailsign = False
    for i in x[1:]:
        if i == "@":
            emailsign = True
            break
    while not emailsign:
        x = input("Please enter correct e-mail address : ")
        FillGaps(x)
        CheckLength(x, 3)
        emailsign = False
        for i in x:
            if i == "@":
                emailsign = True
                break
    return x
# Validation of Phone Number
def CheckPhoneNumber(x):
    x = "".join(x.split(" "))
    while len(x) != 13 or x[:4] != "+994" or not x[1:].isdigit():
        x = input("Please enter correct Azerbaijani number : ")
        x = "".join(x.split(" "))
    return x
# Cheking the lengths of inputs
def CheckLength(x, limitnumber):
    while len(x) < limitnumber:
        x = input("Enter full information : ")
        FillGaps(x)
    return x
# Checking if input contains of only letters
def CheckLetters(x, str):
    while not x.isalpha():
        x = input("Please enter correct {}: ".format(str))
    return x
# THE PROCESS

# Entry point
students = []
print("Welcome to Student Managment program.")
operation = InputInfo()

# Workflow of program
while operation != "quit" and operation != "q":
    if operation == "add" or operation == "a":
        print("Fill the gaps to add a new student.")
        name = input("Student name : ").lower()
        name=FillGaps(name)
        name=CheckLength(name, 1)
        name = CheckLetters(name, "name")
        surname = input("Student surname : ").lower()
        surname=FillGaps(surname)
        surname=CheckLength(surname, 1)
        surname = CheckLetters(surname, "surname")
        email = input("Student e-mail : ")
        email=FillGaps(email)
        email=CheckLength(email, 3)
        email = CheckStudentEmail(email)
        phone = input("Student Phone Number : ")
        phone = FillGaps(phone)
        phone = CheckPhoneNumber(phone)
        code = input("Student ID(enter positive 3 digits number) : ")
        code = FillGaps(code)
        code = CheckStudentCode(code)
        student = Student(name, surname, email, phone, code)
        students.append(student)
        operation = InputInfo()
    elif operation == "delete" or operation == "d":
        deletecode = input("Enter the ID of the student you want to delete : ")
        DeleteForCode(deletecode)
        operation = InputInfo()
    elif operation == "change" or operation == "c":
        changecode = input("Enter the ID of the student whom you want to change the information of : ")
        ChangeForCode(changecode)
        operation = InputInfo()
    elif operation == "student" or operation == "s":
        showname = input("Enter the name of the student whom you want to see the information of : ").lower()
        ShowForName(showname)
        operation = InputInfo()
    elif operation == "all" or operation == "l":
        ShowAll()
        operation = InputInfo()
    elif operation == "info" or operation == "i":
        operation = FullInputInfo()
    else:
        operation = input("Enter correct keyword : ").lower()
else:
    print("Thank you for visiting Student Managment program")
    pass
