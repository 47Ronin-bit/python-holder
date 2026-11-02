MIN_LENGTH = 8

 
def get_password():
    """Prompt for a password and return it exactly as typed.
 
    The password is not stripped, so a leading or trailing space is
    caught by the "letters and digits only" rule instead of being hidden.
    """
    return input("Enter a password: ")
 
 
def check_password(password):
    """Return a list of messages describing each policy rule that failed."""
    problems = []
 
    if len(password) < MIN_LENGTH:
        problems.append(f"It must be at least {MIN_LENGTH} characters long "
                        f"(yours has {len(password)}).")
 
    has_upper = False
    has_lower = False
    has_digit = False
    has_invalid = False
 
    # Examine the password one character at a time
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
 
        if not char.isalnum():
            has_invalid = True
 
    if not has_upper or not has_lower or not has_digit:
        problems.append("It must contain at least one uppercase letter, one lowercase letter, and one digit.")
        if has_invalid:
            problems.append("It may only contain letters and digits (no spaces or symbols).")
 
    return problems
 
 
def display_result(problems):
    """Print whether the password is valid, and why not if it isn't."""
    if not problems:
        print("Password accepted. It meets all requirements.")
    else:
        print("Password rejected for the following reason(s):")
        for problem in problems:
            print(f"  - {problem}")
 
 
def main():
    """Get a password, check it against the policy, and show the result."""
    try:
        password = get_password()
    except (EOFError, KeyboardInterrupt):
        print("\nNo password was entered. Exiting.")
        return
 
    problems = check_password(password)
    display_result(problems)
 
 
main()
 
 
