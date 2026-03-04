class Employee: # Here we define a class named Employee
    def __init__(self, empno, empname, email, department):
        self.empno = None
        self.empname = None
        self.email = None
        self.department = None
        
        # Using setter methods
        self.set_empno(empno)
        self.set_empname(empname)
        self.set_email(email)
        self.set_department(department)
        

    # Setter methods
    def set_empno(self, empno):
        if empno.isdigit():
            self.empno = empno
        else:
            print("Invalid Employee Number.")

    def set_empname(self, empname):
        self.empname = empname

    def set_email(self, email):
        if "@" in email and "." in email:
            self.email = email
        else:
            print("Invalid Email format.")

    def set_department(self, department):
        self.department = department

    
    # Method to display employee details
    def show_details(self):
        print("\n--- Employee Details ---")
        print("Employee Number:", self.empno)
        print("Employee Name:", self.empname)
        print("Email:", self.email)
        print("Department:", self.department)
        


# List to store employees
employees = []

# Menu-driven system to add and show employee details
while True:
    print("\n--- Employee Menu ---")
    print("1. Add Employee")
    print("2. Show All Employees")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        empno = input("Employee Number: ")
        empname = input("Employee Name: ")
        email = input("Email: ")
        department = input("Department: ")
        

        new_employee = Employee(empno, empname, email, department)
        employees.append(new_employee)
        print("Employee added successfully.")

    elif choice == "2":
        if not employees:
            print("No employee records found.")
        else:
            for emp in employees:
                emp.show_details()
    elif choice == "3":
        print("Thank you for using the employee management system.")
        break

    else:
        print("Invalid option. Please try again.")
