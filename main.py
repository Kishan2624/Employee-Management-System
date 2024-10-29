# employee_management_system/main.py

from services.employee_service import EmployeeService


def display_menu():
    """
    Displays the main menu for the Employee Management System.
    """
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Search Employee by Name")
    print("6. Calculate Average Salary")
    print("7. Count Employees")
    print("8. View Employees Sorted by Salary")
    print("9. View Recently Joined Employees")
    print("10. Increment Employee Salary")
    print("11. Sort Employees by Joining Date")
    print("12. Find Employee by ID")
    print("13. Get Employees by Title")
    print("14. Get Employees by Department")
    print("15. Count Employees per Department")
    print("16. Count Employees with Name")
    print("17. Get Unique Employee Names")
    print("18. Check Employee Exists")
    print("19. Get Employees by Position")
    print("20. Get Employees Sorted by Position")
    print("21. Exit")
    print("\n")


def add_employee():
    """
    Prompts the user to enter employee details and
    adds the employee to the database.
    """
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    position = input("Enter position: ")
    hire_date = input("Enter hire date (YYYY-MM-DD): ")

    EmployeeService.add_employee(name, department, salary, position, hire_date)


def view_employees():
    """
    Retrieves and displays all employees from the database.
    """
    employees = EmployeeService.get_all_employees()
    if employees:
        print("\nEmployee List:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found.")


def update_employee():
    """
    Prompts the user for employee ID and fields to update.
    """
    employee_id = int(input("Enter employee ID to update: "))
    name = input("Enter new name (leave blank to skip): ")
    department = input("Enter new department (leave blank to skip): ")
    salary_input = input("Enter new salary (leave blank to skip): ")
    salary = float(salary_input) if salary_input else None
    position = input("Enter new position (leave blank to skip): ")
    hire_date = input(
        "Enter new hire date (YYYY-MM-DD, leave blank to skip): "
    )

    EmployeeService.update_employee(
        employee_id,
        name or None,
        department or None,
        salary,
        position or None,
        hire_date or None
    )


def delete_employee():
    """
    Prompts the user for employee ID to delete from the database.
    """
    employee_id = int(input("Enter employee ID to delete: "))
    EmployeeService.delete_employee(employee_id)


def search_employee():
    """
    Prompts the user for a name to search and displays matching employees.
    """
    name = input("Enter employee name to search: ")
    employees = EmployeeService.search_employee_by_name(name)
    print(f"name results - {name}")
    if employees:
        print("\nSearch Results:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found with that name.")


def calculate_average_salary():
    """
    Retrieves and displays the average salary of employees.
    """
    average_salary = EmployeeService.calculate_average_salary()
    print(f"\nAverage Salary of Employees: {average_salary:.2f}")


def count_employees():
    """Retrieves and displays the total number of employees."""
    total_count = EmployeeService.count_employees()
    print(f"\nTotal Number of Employees: {total_count}")


def view_employees_sorted_by_salary():
    """Retrieves and displays all employees sorted by salary."""
    employees = EmployeeService.get_employees_sorted_by_salary()
    if employees:
        print("\nEmployees Sorted by Salary:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found.")


def view_recent_employees():
    """Retrieves and displays the most recently hired employees."""
    recent_employees = EmployeeService.get_recent_employees()
    if recent_employees:
        print("\nRecently Joined Employees:")
        for emp in recent_employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No recently hired employees found.")


def increment_employee_salary():
    """
    Prompts the user for employee ID and
    increment amount, then updates the salary.
    """
    employee_id = int(input("Enter employee ID to increment salary: "))

    EmployeeService.increment_salary(employee_id)


def sort_employees_by_joining_date():
    """
    Retrieves and displays all employees sorted by joining date.
    """
    employees = EmployeeService.sort_employees_by_joining_date()
    if employees:
        print("\nEmployees Sorted by Joining Date:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found.")


def find_employee_by_id():
    """
    Prompts the user for an employee ID and
    retrieves and displays the employee details.
    """
    employee_id = int(input("Enter employee ID to find: "))
    employee = EmployeeService.find_employee_by_id(employee_id)
    if employee:
        print("\nEmployee Found:")
        print(
            f"ID: {employee[0]}, Name: {
                employee[1]}, Department: {employee[2]}, "
            f"Salary: {employee[3]}, Position: {
                employee[4]}, Hire Date: {employee[5]}"
        )
    else:
        print("Employee not found.")


def get_employees_by_title():
    """
    Prompts the user for a position and
    retrieves and displays employees by position.
    """
    position = input("Enter employee Title to find: ")
    employees = EmployeeService.get_employees_by_title(position)
    if employees:
        print("\nEmployees Found by Position:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found with that position.")


def get_employees_by_department():
    """
    Prompts the user for a department and
    retrieves and displays employees by department.
    """
    department = input("Enter employee department to find: ")
    employees = EmployeeService.get_employees_by_department(department)
    if employees:
        print("\nEmployees Found by Department:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found in that department.")


def count_employees_per_department():
    """
    Prompts the user for a department and
    retrieves and displays the count of employees in that department.
    """
    department = input("Enter department to count employees: ")
    count = EmployeeService.count_employees_per_department(department)
    print(f"\nTotal Number of Employees in {department}: {count}")


def count_employees_with_name():
    """
    Prompts the user for a name and
    retrieves and displays the count of employees with that name.
    """
    name = input("Enter employee name to count: ")
    count = EmployeeService.count_employees_by_name(name)
    print(f"\nTotal Number of Employees with Name {name}: {count}")


def get_unique_employee_names():
    """
    Retrieves and displays unique employee names.
    """
    names = EmployeeService.get_unique_employee_names()
    if names:
        print("\nUnique Employee Names:")
        for name in names:
            print(name)
    else:
        print("No unique employee names found.")


def check_employee_exists():
    """
    Prompts the user for an employee ID and
    checks if the employee exists in the database.
    """
    employee_id = int(input("Enter employee ID to check: "))
    exists = EmployeeService.check_employee_exists(employee_id)
    if exists:
        print("Employee exists.")
    else:
        print("Employee does not exist.")


def get_employees_by_position():
    """
    Prompts the user for a position and
    retrieves and displays employees by position.
    """
    position = input("Enter employee position to find: ")
    employees = EmployeeService.get_employees_by_position(position)
    if employees:
        print("\nEmployees Found by Position:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found with that position.")


def get_employees_sorted_by_position():
    """
    Retrieves and displays all employees sorted by position.
    """
    employees = EmployeeService.get_employees_sorted_by_position()
    if employees:
        print("\nEmployees Sorted by Position:")
        for emp in employees:
            print(
                f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, "
                f"Salary: {emp[3]}, Position: {emp[4]}, Hire Date: {emp[5]}"
            )
    else:
        print("No employees found.")


def main():
    """
    Main function to run the Employee Management System.
    """
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            search_employee()
        elif choice == '6':
            calculate_average_salary()
        elif choice == '7':
            count_employees()
        elif choice == '8':
            view_employees_sorted_by_salary()
        elif choice == '9':
            view_recent_employees()
        elif choice == '10':
            increment_employee_salary()
        elif choice == '11':
            sort_employees_by_joining_date()
        elif choice == '12':
            find_employee_by_id()
        elif choice == '13':
            get_employees_by_title()
        elif choice == '14':
            get_employees_by_department()
        elif choice == '15':
            count_employees_per_department()
        elif choice == '16':
            count_employees_with_name()
        elif choice == '17':
            get_unique_employee_names()
        elif choice == '18':
            check_employee_exists()
        elif choice == '19':
            get_employees_by_position()
        elif choice == '20':
            get_employees_sorted_by_position()
        elif choice == '21':
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
