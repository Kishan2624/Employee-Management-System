# employee_management_system/services/employee_service.py

from models.employee import Employee


class EmployeeService:
    @staticmethod
    def add_employee(name, department, salary, position, hire_date):
        """
        Creates a new Employee instance and adds it to the database.
        """
        new_employee = Employee(name, department, salary, position, hire_date)
        Employee.add_employee(new_employee)
        print("Employee added through service.")

    @staticmethod
    def get_all_employees():
        """
        Retrieves all employees from the database.
        Returns a list of employee records.
        """
        employees = Employee.get_all_employees()
        if employees:
            for emp in employees:
                print(emp)  # Print each employee tuple for visualization
        else:
            print("No employees found.")
        return employees

    @staticmethod
    def update_employee(employee_id, name=None, department=None,
                        salary=None, position=None, hire_date=None):
        """
        Updates an employee's information based on provided fields.
        Only fields that are not None will be updated.
        """
        Employee.update_employee(
            employee_id, name, department, salary, position, hire_date
        )
        print("Employee updated through service.")

    @staticmethod
    def delete_employee(employee_id):
        """
        Deletes an employee from the database based on employee ID.
        """
        Employee.delete_employee(employee_id)
        print("Employee deleted through service.")

    @staticmethod
    def search_employee_by_name(name):
        """
        Search for employees by name.
        """
        result = Employee.search_employee_by_name(name)
        print("Employee searched through service.")
        return result

    @staticmethod
    def calculate_average_salary():
        """
        Calculate and return the average salary of employees.
        """
        result = Employee.calculate_average_salary()
        print("Average salary calculated through service.")
        return result

    @staticmethod
    def count_employees():
        """
        Count and return the total number of employees.
        """
        result = Employee.count_employees()
        print("Employee count calculated through service.")
        return result

    @staticmethod
    def get_employees_sorted_by_salary():
        """
        Retrieve all employees sorted by salary in ascending order.
        """
        result = Employee.get_employees_sorted_by_salary()
        print("Employees sorted by salary through service.")
        return result

    @staticmethod
    def get_recent_employees(limit=5):
        """
        Retrieve the most recently hired employees.
        """
        result = Employee.get_recent_employees(limit)
        print("Recent employees retrieved through service.")
        return result

    @staticmethod
    def increment_salary(employee_id):
        """
        Increment the salary of an employee by a specified amount.
        """
        result = Employee.increment_salary(employee_id)
        print("Employee salary incremented through service.")
        return result

    @staticmethod
    def sort_employees_by_joining_date():
        """
        Fetch and return a list of employees sorted by their joining date.
        """
        result = Employee.sort_employees_by_joining_date()
        print("Employees sorted by joining date through service.")
        return result

    @staticmethod
    def find_employee_by_id(employee_id):
        """
        Find and return an employee's details by their ID.
        """
        result = Employee.find_employee_by_id(employee_id)
        print("Employee found by ID through service.")
        return result

    @staticmethod
    def get_employees_by_title(position):
        """Retrieve and return a list of employees by their position."""
        result = Employee.get_employees_by_title(position)
        print("Employees found by title through service.")
        return result

    @staticmethod
    def get_employees_by_department(department):
        """Retrieve and return a list of employees by their department."""
        result = Employee.get_employees_by_department(department)
        print("Employees found by department through service.")
        return result

    @staticmethod
    def count_employees_per_department(department):
        """Count the number of employees in a specified department."""
        result = Employee.count_employees_per_department(department)
        print("Employee count per department calculated through service.")
        return result

    @staticmethod
    def count_employees_by_name(name):
        """Count the number of employees with a specified name."""
        result = Employee.count_employees_by_name(name)
        print("Employee count by name calculated through service.")
        return result

    @staticmethod
    def get_unique_employee_names():
        """Retrieve unique employee names from the database."""
        result = Employee.get_unique_employee_names()
        print("Unique employee names retrieved through service.")
        return result

    @staticmethod
    def check_employee_exists(employee_id):
        """Check if an employee exists in the database based on employee ID."""
        result = Employee.check_employee_exists(employee_id)
        print("Employee existence checked through service.")
        return result

    @staticmethod
    def get_employees_by_position(position):
        """Retrieve employees by their position."""
        result = Employee.get_employees_by_position(position)
        print("Employees found by position through service.")
        return result

    @staticmethod
    def get_employees_sorted_by_position():
        """Retrieve all employees sorted by their position."""
        result = Employee.get_employees_sorted_by_position()
        print("Employees sorted by position through service.")
        return result
