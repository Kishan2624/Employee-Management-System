# employee_management_system/models/employee.py

from utils.db_connection import create_connection, close_connection


class Employee:
    def __init__(self, name, department, salary, position, hire_date):
        self.name = name
        self.department = department
        self.salary = salary
        self.position = position
        self.hire_date = hire_date

    @staticmethod
    def add_employee(employee):
        """
        Adds a new employee to the database.
        """
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                sql = """
                    INSERT INTO employees 
                    (name, department, salary, position, hire_date)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values = (
                    employee.name,
                    employee.department,
                    employee.salary,
                    employee.position,
                    employee.hire_date
                )
                cursor.execute(sql, values)
                connection.commit()
                print("Employee added successfully.")
            except Exception as e:
                print(f"Error adding employee: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def get_all_employees():
        """
        Retrieves all employees from the database.
        """
        connection = create_connection()
        employees = []
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM employees")
                employees = cursor.fetchall()
            except Exception as e:
                print(f"Error fetching employees: {e}")
            finally:
                close_connection(connection)
        return employees

    @staticmethod
    def update_employee(
        employee_id,
        name=None,
        department=None,
        salary=None,
        position=None,
        hire_date=None
    ):
        """
        Updates an existing employee's details in the database.
        """
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "UPDATE employees SET"
                updates = []
                values = []

                if name:
                    updates.append("name = %s")
                    values.append(name)
                if department:
                    updates.append("department = %s")
                    values.append(department)
                if salary:
                    updates.append("salary = %s")
                    values.append(salary)
                if position:
                    updates.append("position = %s")
                    values.append(position)
                if hire_date:
                    updates.append("hire_date = %s")
                    values.append(hire_date)

                if updates:
                    sql += " " + ", ".join(updates) + " WHERE id = %s"
                    values.append(employee_id)
                    cursor.execute(sql, values)
                    connection.commit()
                    print("Employee updated successfully.")
                else:
                    print("No changes provided for update.")
            except Exception as e:
                print(f"Error updating employee: {e}")
            finally:
                close_connection(connection)

    @staticmethod
    def delete_employee(employee_id):
        """
        Deletes an employee from the database based on employee ID.
        """
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                sql = "DELETE FROM employees WHERE id = %s"
                cursor.execute(sql, (employee_id,))
                connection.commit()
                print("Employee deleted successfully.")
            except Exception as e:
                print(f"Error deleting employee: {e}")
            finally:
                close_connection(connection)
