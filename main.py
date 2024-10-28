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
    print("11. Get Employee by ID")
    print("12. Get Employees by Position")
    print("13. Get Employees by Department")
    print("14. Count Employees per Department")
    print("15. Count Employees with a Specific Name")
    print("16. Get Unique Employee Names")
    print("17. Check if Employee ID Exists")
    print("18. Get Employees Sorted by Position")
    print("19. Get Employees by Job Title")
    print("20. Count Employees with a Specific Position")
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

        elif choice == '21':
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
