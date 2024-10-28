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

    @staticmethod
    def search_employee_by_name(name):
        """Search for employees by name."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Use parameterized queries to prevent SQL injection
            query = "SELECT * FROM employees WHERE name LIKE %s"
            cursor.execute(query, (f"%{name}%",))
            employees = cursor.fetchall()

            return employees
        except Exception as err:
            print(f"Error: {err}")
            return []
        finally:
            close_connection(connection)

    @staticmethod
    def calculate_average_salary():
        """Calculate and return the average salary of employees."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            query = "SELECT AVG(salary) FROM employees"
            cursor.execute(query)
            average_salary = cursor.fetchone()[0]

            return average_salary if average_salary is not None else 0.0
        except Exception as err:
            print(f"Error: {err}")
            return 0.0
        finally:
            close_connection(connection)

    @staticmethod
    def count_employees():
        """Count and return the total number of employees."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            query = "SELECT COUNT(*) FROM employees"
            cursor.execute(query)
            employee_count = cursor.fetchone()[0]

            return employee_count
        except Exception as err:
            print(f"Error: {err}")
            return 0
        finally:
            close_connection(connection)

    @staticmethod
    def get_employees_sorted_by_salary():
        """Retrieve all employees sorted by salary in ascending order."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            query = "SELECT * FROM employees ORDER BY salary ASC"
            cursor.execute(query)
            employees = cursor.fetchall()

            return employees
        except Exception as err:
            print(f"Error: {err}")
            return []
        finally:
            close_connection(connection)

    @staticmethod
    def get_recent_employees(limit=5):
        """Retrieve the most recently hired employees."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            query = "SELECT * FROM employees ORDER BY hire_date DESC LIMIT %s"
            cursor.execute(query, (limit,))
            recent_employees = cursor.fetchall()

            return recent_employees
        except Exception as err:
            print(f"Error: {err}")
            return []
        finally:
            close_connection(connection)

    @staticmethod
    def increment_salary(employee_id):
        """
        Increment the salary of an employee by a specified amount.
        """
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Check if the employee ID exists
            check_query = "SELECT COUNT(*) FROM employees WHERE id = %s"
            cursor.execute(check_query, (employee_id,))
            exists = cursor.fetchone()[0]

            if exists == 0:
                print(
                    f"Error: No employee found with ID: {employee_id}"
                )
                return

            increment_amount = float(input("Enter increment amount: "))
            # Update the salary for the specified employee ID
            query = "UPDATE employees SET salary = salary + %s WHERE id = %s"
            cursor.execute(query, (increment_amount, employee_id))
            connection.commit()

            print(
                f"Salary updated for employee ID: {
                    employee_id}. Increment amount: {increment_amount}"
            )

        except Exception as err:
            print(f"Error: {err}")

        finally:
            close_connection(connection)

    @staticmethod
    def sort_employees_by_joining_date():
        """
        Fetch and return a list of employees sorted by their joining date.
        """
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to fetch employees sorted by joining date
            # Assuming the column name is 'joining_date'
            query = "SELECT * FROM employees ORDER BY joining_date ASC"
            cursor.execute(query)

            # Fetch all employees sorted by joining date
            employees = cursor.fetchall()

            # Return the list of employees
            return employees

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def find_employee_by_id(employee_id):
        """
        Find and return an employee's details by their ID.
        """
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to find an employee by ID
            query = "SELECT * FROM employees WHERE id = %s"
            cursor.execute(query, (employee_id,))

            # Fetch the result
            employee = cursor.fetchone()

            if employee is None:
                raise ValueError(
                    f"Error: No employee found with ID: {employee_id}")

            return employee  # Return employee details as a tuple

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def get_employees_by_title(position):
        """Retrieve and return a list of employees by their position."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to find employees by position
            query = "SELECT * FROM employees WHERE position = %s"
            cursor.execute(query, (position,))

            # Fetch all matching employees
            employees = cursor.fetchall()

            if not employees:
                raise ValueError(
                    f"Error: No employees found with position: {position}")

            return employees  # Return a list of employees as tuples

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def get_employees_by_department(department):
        """Retrieve and return a list of employees by their department."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to find employees by department
            query = "SELECT * FROM employees WHERE department = %s"
            cursor.execute(query, (department,))

            # Fetch all matching employees
            employees = cursor.fetchall()

            if not employees:
                raise ValueError(
                    f"Error: No employees found in department: {department}")

            return employees  # Return a list of employees as tuples

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def count_employees_per_department(department):
        """Count the number of employees in a specified department."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to count employees by department
            query = "SELECT COUNT(*) FROM employees WHERE department = %s"
            cursor.execute(query, (department,))

            # Fetch the count result
            count = cursor.fetchone()[0]

            return count  # Return the count of employees in the department

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def count_employees_by_name(name):
        """Count the number of employees with a specified name."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to count employees by name
            query = "SELECT COUNT(*) FROM employees WHERE name = %s"
            cursor.execute(query, (name,))

            # Fetch the count result
            count = cursor.fetchone()[0]

            # Return the count of employees with the specified name
            return count

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def get_unique_employee_names():
        """Retrieve unique employee names from the database."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to get unique employee names
            query = "SELECT DISTINCT name FROM employees"
            cursor.execute(query)

            # Fetch all unique names
            unique_names = cursor.fetchall()

            # Extract names from the result tuples
            unique_names_list = [name[0] for name in unique_names]

            return unique_names_list  # Return a list of unique employee names

        except Exception as err:
            return f"Error: {err}"

        finally:
            close_connection(connection)

    @staticmethod
    def check_employee_exists(employee_id):
        """Check if an employee exists in the database based on employee ID."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to check if the employee ID exists
            query = "SELECT COUNT(*) FROM employees WHERE id = %s"
            cursor.execute(query, (employee_id,))
            exists = cursor.fetchone()[0]

            return exists > 0  # Return True if exists, False otherwise

        except Exception as err:
            print(f"Error: {err}")
            return False  # Return False if there's an error

        finally:
            close_connection(connection)

    @staticmethod
    def get_employees_by_position(position):
        """Retrieve employees by their position."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Use parameterized queries to prevent SQL injection
            query = "SELECT * FROM employees WHERE position = %s"
            cursor.execute(query, (position,))

            employees = cursor.fetchall()  # Fetch all the records
            return employees

        except Exception as err:
            print(f"Error: {err}")
            return []  # Return an empty list if there's an error

        finally:
            close_connection(connection)

    @staticmethod
    def get_employees_sorted_by_position():
        """Retrieve all employees sorted by their position."""
        try:
            connection = create_connection()
            cursor = connection.cursor()

            # SQL query to select all employees sorted by position
            query = "SELECT * FROM employees ORDER BY position"
            cursor.execute(query)

            employees = cursor.fetchall()  # Fetch all the records
            return employees

        except Exception as err:
            print(f"Error: {err}")
            return []  # Return an empty list if there's an error

        finally:
            close_connection(connection)
