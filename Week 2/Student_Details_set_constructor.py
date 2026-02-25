class student: # Here we define a class name student
    
    def __init__(self, name, roll_number): # This is the constructor method
        # private attribute
        self.__name = None
        self.__roll_number = None
        
        # setter method for name and roll_number in the constructor
        self.set_name(name)
        self.set_roll_number(roll_number)
        
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
student1 = student(name="arun", roll_number=38449) # Here we create an instance of the student class

# here we get the output
student1.show_details()

''' In this code, we have defined a class named student with private attributes __name and __roll_number.
We have provided setter methods set_name and set_roll_number to set the values of these attributes,
and a method show_details to display the student details. We have also added a constructor method __init__ that takes
name and roll_number as parameters and sets these values using the setter methods. Finally, we create an instance of the 
student class with specific name and roll number, and then print the student details using the show_details method. '''


''' here we set the name and roll number using the setter methods in the constructor, so we don't need to set them separately 
after creating the instance.
This way, we can create an instance of the student class with the required details right away, and
we can directly call the show_details method to display the information without needing to set the attributes separately. '''
