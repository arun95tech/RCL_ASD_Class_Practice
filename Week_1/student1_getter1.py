class Student: # Here we define a class name student
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
    
    # getter method for name
    def get_name(self): 
        return self.__name 
    
    # getter method for roll_number
    def get_roll_number(self): 
        return self.__roll_number
    
    # testing the class and its methods
    
student1 = Student() # Here we create an instance of the student class

# taking input from the user for name and roll number
print("Enter Student deatils")
name = input("Enter name: ") 
roll_number = input("Enter roll number: ") 

student1.set_name(name)                     # Set the name using the setter method
student1.set_roll_number(roll_number)       # Set the roll number using the setter method


# here we get the output
print("Student Details:")
print("Student Name is: ", student1.get_name()) 
print("Student Roll Number is: ", student1.get_roll_number()) 


''' In this code, we have defined a class named Student with private attributes __name and __roll_number. 
We have provided setter methods set_name and set_roll_number to set the values of these attributes, and 
getter methods get_name and get_roll_number to retrieve their values. Finally, we create an instance of the Student class, 
take input from the user for name and roll number, set these values using the setter methods, 
and then print the student details using the getter methods. '''

''' geter method is used to retrieve the value of a private attribute, while a setter method is used to set the value of a 
private attribute.
In this code, we have used getter methods to retrieve the values of the private attributes __name and __roll_number,
and setter methods to set the values of these attributes. '''


