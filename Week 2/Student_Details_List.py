class Student:
    def __init__(self, name, roll_number):
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
    
# testing the class and its methods
#make sure to instantiate the class to allocate memory for many students
students = [] # Create an empty list to store student instances
while True:
    print("\n--student menu--:")
    print("1. Add student details")
    print("2. show student details")
    print("3. Exit")
    
    choice = input("Select an option: ")
    if choice == "1":
        name = input("Name: ")  
        roll_number = input("Roll Number: ")
        
        
        student = Student(name, roll_number) # Here we create an instance of the Student class
        students.append(student) # Add the student instance to the students list
    elif choice == "2":
        if not students:
            print("No student details available. Please add student details first.")
        else:
            for student in students:
                student.show_details()
            
    elif choice == "3":
        print("Thank you for using the student management system.")
        break
    else:
        print("Invalid option. Please try again.")
    
    ''' In this code, we have defined a class named Student with private attributes name and roll_number.
    We have provided setter methods set_name and set_roll_number to set the values of these attributes,
    and a method show_details to display the student details. We have also added a constructor method __init__ that takes
    name and roll_number as parameters and initializes the private attributes using the setter methods.
    We have implemented a menu-driven program that allows the user to add student details and show student details.
    The program continues to run until the user chooses to exit. The student details are stored in a list, 
    allowing for multiple students to be added and displayed. '''
    
    ''' here we set the name and roll number using the setter methods in the constructor, so we don't need to set them separately 
    after creating the instance. This way, we can create an instance of the Student class with
    the required details right away, and we can directly call the show_details method to display the information 
    without needing to set the attributes separately. '''
    
    ''' here we use a list to store multiple student instances, allowing us to add and display details for multiple students.
    The menu-driven program provides a user-friendly interface for managing student details, making it easy to add and 
    view information as needed. '''
    
    
    
    
    