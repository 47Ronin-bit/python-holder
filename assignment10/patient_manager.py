import patient
import procedure


def create_patient():
    """Prompt for the patient's data and return a new Patient."""
    first_name = input("Enter the first name: ")
    middle_name = input("Enter the middle name: ")
    last_name = input("Enter the last name: ")
    address = input("Enter the address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    zip_code = input("Enter the ZIP code: ")
    phone = input("Enter the phone number: ")
    emergency_contact = input("Enter the emergency contact name: ")
    emergency_phone = input("Enter the emergency contact phone: ")

    return patient.Patient(first_name, middle_name, last_name, address, city,
                   state, zip_code, phone, emergency_contact,
                   emergency_phone)


def create_procedure():
    """Prompt for procedure details and return a new Procedure.

    The charge must be validated: keep re-prompting until the user
    enters a number greater than 0.
    """
    description = input("Enter the procedure description: ")
    date = input("Enter the date of the procedure: ")
    practitioner = input("Enter the practitioner's name: ")

    # Keep asking until the charge is a number greater than 0.
    valid = False
    while not valid:
        try:
            charge = float(input("Enter the charge: "))
            if charge > 0:
                valid = True
            else:
                print("The charge must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return procedure.Procedure(description, date, practitioner, charge)


def display_information(patient, procedures):
    """Display the patient, every procedure, and the total charges.

    The patient and each procedure are objects passed in as arguments;
    print() calls their __str__ methods, and get_charge() is called on
    each procedure to total the cost.
    """
    print(patient)

    total = 0.0
    for procedure in procedures:
        print()
        print(procedure)
        total += procedure.get_charge()

    print(f"\nTotal charges: {total:.2f}")


def main():
    patient = create_patient()

    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")
    choice = input("Add a procedure? (y/n): ")
    while choice.lower() != "n":
        procedures.append(create_procedure())
        choice = input("Add another procedure? (y/n): ")

    print("\nPatient and Procedure Information:")
    display_information(patient, procedures)


if __name__ == "__main__":
    main()