class student:
    def __init__(self):
        self.__name = None
        self.__roll_number = None
    
    def set_name(self, name):
        self.__name = name
    
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number
        
    def show_details(self):
        print("Student Name is: ", self.__name)
        print("Student Roll Number is: ", self.__roll_number)
    
# testing the class and its methods
student1 = student()

# taking input from the user for name and roll number but using a loop to allow multiple entries

while True:
    print("\n --Student Menu--")
    print("1. Enter Student Details")
    print("2. Show Student Details")
    print("3. Exit")
    
    choice = input("Select an Option: ")

    if choice == '1':
         name = input("Enter name: ")
         roll_number = input("Enter roll number: ")
    
         student1.set_name(name)
         student1.set_roll_number(roll_number)
    elif choice == '2':
        print("Student Details:")
        student1.show_details()
    elif choice == '3':
         print("Exiting the program.")
         break
    else:
        print("Invalid choice. Please select a valid option.")

''' In this code, we have added a loop to allow the user to enter multiple student details and show them as needed. 
The user can select an option from the menu to either enter student details, show student details, or exit the program. 
The loop will continue until the user chooses to exit by selecting option 3. This way, the user can manage multiple entries
without having to restart the program each time. '''
