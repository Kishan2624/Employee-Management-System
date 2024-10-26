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
