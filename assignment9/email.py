import os
import pickle
 
# Menu choice constants
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
 
# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')
 
 
def main():
    """Load the emails, run the menu loop, and save after each change."""
    emails = load_emails()
    choice = 0
 
    while choice != QUIT:
        choice = get_user_choice()
 
        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
            save_emails(emails)
        elif choice == CHANGE:
            change(emails)
            save_emails(emails)
        elif choice == DELETE:
            delete(emails)
            save_emails(emails)
 
 
def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    # If the file does not exist, start with an empty dictionary
    try:
        input_file = open(FILENAME, 'rb')
    except IOError:
        return {}
 
    # If the file exists but is empty, unpickling raises EOFError
    try:
        emails = pickle.load(input_file)
    except EOFError:
        emails = {}
 
    input_file.close()
    return emails
 
 
def get_user_choice():
    """Display the menu and return a validated choice."""
    print('\nEmail Address Menu')
    print('------------------')
    print('1. Look up an email address')
    print('2. Add a new email address')
    print('3. Change an email address')
    print('4. Delete an email address')
    print('5. Quit the program')
 
    choice = 0
    while choice < LOOK_UP or choice > QUIT:
        try:
            choice = int(input('Enter your choice: '))
            if choice < LOOK_UP or choice > QUIT:
                print('Error: enter a number from 1 to 5.')
        except ValueError:
            print('Error: enter a number from 1 to 5.')
            choice = 0
 
    return choice
 
 
def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input('Enter a name: ')
    print(emails.get(name, 'That name was not found.'))
 
 
def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input('Enter a name: ')
 
    if name not in emails:
        address = input('Enter the email address: ')
        emails[name] = address
        print('The email address was added.')
    else:
        print('That name already exists.')
 
 
def change(emails):
    """Update the address for an existing name."""
    name = input('Enter a name: ')
 
    if name in emails:
        address = input('Enter the new email address: ')
        emails[name] = address
        print('The email address was changed.')
    else:
        print('That name was not found.')
 
 
def delete(emails):
    """Remove a name/address pair."""
    name = input('Enter a name: ')
 
    if name in emails:
        del emails[name]
        print('The entry was deleted.')
    else:
        print('That name was not found.')
 
 
def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    output_file = open(FILENAME, 'wb')
    pickle.dump(emails, output_file)
    output_file.close()
 
 
if __name__ == '__main__':
    main()