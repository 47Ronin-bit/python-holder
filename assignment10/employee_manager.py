import pickle
from employee import Employee

# Global constants for the menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constants for the file name and the not-found message
FILENAME = "employees.dat"
NOT_FOUND = "The specified ID number was not found"


def load_employees():
    """Unpickle the dictionary from the file, or return an empty one."""
    try:
        input_file = open(FILENAME, "rb")
        employees = pickle.load(input_file)
        input_file.close()
    except IOError:
        # The file does not exist yet, so start with an empty dictionary.
        employees = {}

    return employees


def save_employees(employees):
    """Pickle the dictionary to the file."""
    output_file = open(FILENAME, "wb")
    pickle.dump(employees, output_file)
    output_file.close()


def get_menu_choice():
    """Display the menu and return a valid choice."""
    print("\nMenu")
    print("----------------------------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")
    print()

    choice = 0
    while choice < LOOK_UP or choice > QUIT:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            choice = 0
        if choice < LOOK_UP or choice > QUIT:
            print("Invalid choice. Enter a number from 1 to 5.")

    return choice


def look_up(employees):
    """Display the employee with the ID number entered by the user."""
    id_number = input("Enter an employee ID number: ")

    # The Employee object's __str__ method formats the output.
    print(employees.get(id_number, NOT_FOUND))


def add(employees):
    """Add a new employee to the dictionary."""
    name = input("Enter employee name: ")
    id_number = input("Enter employee ID number: ")
    department = input("Enter employee department: ")
    job_title = input("Enter employee title: ")

    if id_number not in employees:
        employees[id_number] = Employee(name, id_number, department,
                                        job_title)
        print("The new employee has been added.")
    else:
        print("An entry with that ID number already exists.")


def change(employees):
    """Change the data of an existing employee."""
    id_number = input("Enter employee ID number: ")

    if id_number in employees:
        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        job_title = input("Enter the new title: ")

        # Call the mutator methods of the Employee object.
        employee = employees[id_number]
        employee.set_name(name)
        employee.set_department(department)
        employee.set_job_title(job_title)
        print("Employee information updated.")
    else:
        print(NOT_FOUND)


def delete(employees):
    """Delete an employee from the dictionary."""
    id_number = input("Enter employee ID number: ")

    if id_number in employees:
        del employees[id_number]
        print("Employee information deleted.")
    else:
        print(NOT_FOUND)


def main():
    employees = load_employees()

    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

    # Save the dictionary before the program ends.
    save_employees(employees)


if __name__ == "__main__":
    main()