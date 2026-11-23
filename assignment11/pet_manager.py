from dog import Dog
from cat import Cat
from bird import Bird


def print_menu():
    print("Pet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show All Pets")
    print("5. Exit")


def main():
    pets = []

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter dog's name: ").strip()
            pets.append(Dog(name))
        elif choice == "2":
            name = input("Enter cat's name: ").strip()
            pets.append(Cat(name))
        elif choice == "3":
            name = input("Enter bird's name: ").strip()
            pets.append(Bird(name))
        elif choice == "4":
            print()
            print("Your Pets:")
            # Python calls the correct __str__ for each pet (polymorphism)
            for pet in pets:
                print(pet)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

        print()


if __name__ == "__main__":
    main()