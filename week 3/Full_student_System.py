class student:
    def __def__(self, name, roll_number):
        self.name = None
        self.roll_number = None

        # setters methods in constructor
        self.set_name(name)
        self.set_roll_number(roll_number)
    # setter method for name
    def set_name(self, name):
        self.name = name
    # setter method for roll_number
    def set_roll_number(self, roll_number):
        self.roll_number = roll_number
    # show details method to display student details
    def show_details(self):
        print("Student Name is: ", self.name)
        print("Student Roll Number is: ", self.roll_number)

# full time studnet class
class full_time_student(student):
    def __init__(self, name, roll_number, hours_per_week):
        super().__init__(name, roll_number) 
        self.hours_per_week = hours_per_week

    def get_hours_per_week(self):
        return self.hours_per_week
        self.course = course

    def show_details(self):
        super().show_details()
        print("Hours per week: ", self.hours_per_week) 
# part time student class
class part_time_student(student):
    def __init__(self, name, roll_number, hours_per_week):
        super().__init__(name, roll_number) 
        self.hours_per_week = hours_per_week

    def get_hours_per_week(self):
        return self.hours_per_week

    def show_details(self):
        super().show_details()
        print("Hours per week: ", self.hours_per_week)

# helper fumction to find the student with roll number
def find_student(roll_number, students):
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None

# list to store student instances
new_students = []

# menu driven program to add and show student details
while True:
    print("\n--- Student Menu ---")
    print("1. Enter Student Details")
    print("2. Show Student Details")
    print("3. Search Student Details")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        name = input("Name: ")  
        roll_number = input("Roll Number: ")
        hours_per_week = input("Hours per week: ")
        student_type = input("Is the student full-time or part-time? (Enter 'full' or 'part'): ")

        if student_type.lower() == "full":
            new_student = full_time_student(name, roll_number, hours_per_week)
        elif student_type.lower() == "part":
            new_student = part_time_student(name, roll_number, hours_per_week)
        else:
            print("Invalid student type. Please enter 'full' or 'part'.")
            continue

        students.append(new_student)
        print("Student details added successfully.")
    elif choice == "2":
        if not students:
            print("No student details available. Please add student details first.")
        else:
            for student in students:
                student.show_details()
    elif choice == "3":
        roll_number = input("Enter the roll number to search: ")
        student = find_student(roll_number, students)
        if student:
            student.show_details()
        else:
            print("Student with roll number", roll_number, "not found.")
    elif choice == "4":
        print("Thank you for using the student management system.")
        break
    else:
        print("Invalid option. Please try again.")
    
