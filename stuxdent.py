import tkinter as tk

class Student():
    def __init__(self, firstname, lastname, age_min, age_max):
        self.firstname = firstname
        self.lastname = lastname
        self.age_min = age_min
        self.age_max = age_max
        
    def display(self):
        print(self.firstname, self.lastname, self.age_min, self.age_max)

class Course():
    def __init__(self, title, HV, description):
        self.title = title
        self.HV = HV
        self.description = description
        
    def display(self):
        print(self.title, self.HV, self.description)

class Lecturer():
    def __init__(self, listofcourses, lastname,age ):
        self.listofcourses = listofcourses
        self.lastname = lastname
        self.age= age 
        
    def display(self):
        print(self.listofcourses, self.lastname)

class Program():
    def __init__(self, nameofcourses, description, search_id):
        self.nameofcourses = nameofcourses
        self.description = description
        self.search_id = search_id
        
    def display(self): 
        print(self.nameofcourses, self.description)

class School():
    def __init__(self, student_list):
        self.student_list = student_list
    def display(self):
        print(self.student_list)
        
    def add_student(self):
        firstname = input("Enter student first name: ")
        lastname = input("Enter student last name: ")
        age_min = int(input("Enter minimum student age: "))
        age_max = int(input("Enter maximum student age: "))
        student = Student(firstname, lastname, age_max, age_min)
        self.student_list.append(student)
        print("Student is added successfully")

    def remove_student(self): 
        firstname = input("Enter student first name: ")
        lastname = input("Enter student last name: ")
        while firstname.isnumeric():
            firstname = input("Invalid input. student name can not be number ")
            print("Enter correct expression")
            lastname = input("Invalid input. student name can not be number ")
            print("Enter correct Expression")
        for i in range(len(self.student_list)):
            if self.student_list[i].firstname == firstname and self.student_list[i].lastname == lastname:
                del self.student_list[i]
                print("Student removed successfully")
                break

    def update_student(self):
        firstname = input("Enter student's first name: ")
        lastname = input("Enter student's last name: ")
        age = int(input("Enter student's age: "))
        while not str(age).isnumeric() or age < 18 or age > 25:
            print("Enter valid age range")
            age = int(input("Enter student's age: "))
        found = False
        for i, s in enumerate(self.student_list):
            if s.firstname == firstname and s.lastname == lastname and s.age == age:
                found = True
                new_firstname = input("Enter new first name: ")
                new_lastname = input("Enter new last name: ")
                new_age = int(input("Enter new age: "))
                while not str(new_age).isnumeric() or new_age < 18 or new_age > 25:
                    print("Enter valid age range")
                    new_age = int(input("Enter new age: "))
                s.firstname = new_firstname
                s.lastname = new_lastname
                s.age = new_age
                break
        if found:
            print("Student updated successfully!")
        else:
            print("Student not found.")
        for s in self.student_list:
            s.display()


    def add_lecturer(self):
        name = input("Enter lecturer's name: ")
        while name.isnumeric():
            name = input("Invalid input. Enter lecturer's name: ")
        listofcourses = input("Enter lecturer's list of courses: ")
        lecturer = Lecturer(listofcourses, name)
        print("Lecturer added successfully!")
        lecturer.display()

    def remove_lecturer(self):
        lecturer_list = [Lecturer(['Object oriented programming 59'], "Mr Adams"), 
                         Lecturer(['Data Science'], "Mr Achraf"), 
                         Lecturer(['Quality Software Development'], "Mr Younes")]
        name = input("Enter lecturer name: ")
        found = False
        if name.isnumeric():
            print("Invalid input! Name cannot be a numeric value.")
            return
        for i, lecturer in enumerate(lecturer_list):
            if lecturer.lastname.lower() == name.lower():
                found = True
                del lecturer_list[i]
                print(f"Lecturer {name} removed successfully!")
                break
        if not found:
            print(f"Lecturer {name} not found.")
    def display_menu(self):
        print("Welcome to the Student Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student Data")
        print("4. Add Lecturer")
        print("5. Remove Lecturer")
        print("6. Exit")
    
        
def main():
    Qualitysoft = Course('Qualitysoftware Development', 30, 'This is a good course for you')
    Qualitysoft.display()
    Student1 = Student("John", "Doe", 18, 25)
    Student1.display()
    Younes = Lecturer("Object oriented programming" ,"59", "Younes")
    Younes.display()
    Program1 = Program("Solftware Engineeringm", "name")
    Program1.display() 
    School1 = School("The total number of student in our campuse are 34")
    School1.display 
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
         add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            add_lecturer()
        elif choice == "5":
            remove_lecturer()
        elif choice == "6":
            print("Exiting program...")
            break
        



