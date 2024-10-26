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
    print("5. Exit")


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
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
