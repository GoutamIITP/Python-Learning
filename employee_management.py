"""
Build a console-based employee management system to add, delete, and view employee records using employee ID as key and a dictionary for storage.
"""

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"
    
class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if emp_id in self.employees:
            print("Employee ID already exists.")
            return
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")

        emp = Employee(emp_id, name, salary)
        self.employees[emp_id] = emp
        print("Employee added successfully.")
    
    def delete_employee(self):
        emp_id = input("Enter Employee id to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee ID not found.")

    def view_employees(self):
        if not self.employees:
            print("No employees to display.")
            return
        print("Employee Records:")
        for emp in self.employees.values():
            print(emp)

def main():
    manager = EmployeeManager()
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. View Employees")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.delete_employee()
        elif choice == '3':
            manager.view_employees()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()