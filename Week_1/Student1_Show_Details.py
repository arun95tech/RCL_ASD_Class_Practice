class student: # Here we define a class name student
    
    def __init__(self): # This is the constructor method
        # private attribute
        self.__name = None
        self.__roll_number = None
        
    # setter method for name
    def set_name(self, name):
        self.__name = name
        
    # setter method for roll_number
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number
    
    # show details method to display student details
    def show_details(self):
        print("Student Name is: ", self.__name)
        print("Student Roll Number is: ", self.__roll_number)
        
# testing the class and its methods
student1 = student() # Here we create an instance of the student class

# taking input from the user for name and roll number
print("Enter Student deatils")
name = input("Enter name: ")
roll_number = input("Enter roll number: ")

# here we set the name and roll number using the setter methods
student1.set_name(name)
student1.set_roll_number(roll_number)

# here we get the output
print("Student Details:")
student1.show_details()

''' In this code, we have defined a class named student with private attributes __name and __roll_number. 
We have provided setter methods set_name and set_roll_number to set the values of these attributes, 
and a method show_details to display the student details. Finally, we create an instance of the student class, 
take input from the user for name and roll number, set these values using the setter methods, 
and then print the student details using the show_details method. '''   

''' Diffrence between getter and show method:-
Is that getter method is used to retrieve the value of a private attribute, 
while a show method is used to display the details of an object. 
In this code, we have used a show_details method to display the student details,
and we have not used any getter methods to retrieve the values of the private attributes __name and __roll_number.'''

