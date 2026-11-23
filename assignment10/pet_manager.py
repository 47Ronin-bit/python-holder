import pet


def main():
    # Get the pet's data from the user.
    name = input("Enter the name of the pet: ")
    animal_type = input("Enter the type of animal: ")
    age = int(input("Enter the age of the pet: "))

    # Create a Pet object.
    my_pet = pet.Pet(name, animal_type, age)

    # Display the data that was entered.
    print("Here is the data that you entered:")
    print(my_pet)


# Call the main function.
main()