MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
DATE_PARTS = 3      # month, day, year
YEAR_DIGITS = 4
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31
 
 
def get_date_text():
    """Prompt for a date and return it with extra whitespace removed."""
    return input("Enter a date (mm/dd/yyyy): ").strip()
 
 
def parse_date(text):
    """Split the text into (month, day, year) integers.
 
    Raises ValueError with a clear message if the text is not a valid date.
    """
    parts = text.split("/")
    if len(parts) != DATE_PARTS:
        raise ValueError("The date must have three parts separated by "
                         "slashes, like 01/05/2024.")
 
    # Every part must be made up only of digits
    for part in parts:
        if not part.isdigit():
            raise ValueError("The month, day, and year must contain "
                             "only digits.")
 
    month = int(parts[0])
    day = int(parts[1])
    year_text = parts[2]
 
    if month < MIN_MONTH or month > MAX_MONTH:
        raise ValueError(f"The month must be between {MIN_MONTH} and "
                         f"{MAX_MONTH}.")
    if day < MIN_DAY or day > MAX_DAY:
        raise ValueError(f"The day must be between {MIN_DAY} and "
                         f"{MAX_DAY}.")
    if len(year_text) != YEAR_DIGITS:
        raise ValueError(f"The year must have {YEAR_DIGITS} digits.")
 
    return month, day, int(year_text)
 
 
def format_date(month, day, year):
    """Return the date as text using the full English month name."""
    month_name = MONTH_NAMES[month - 1]    # list index starts at 0
    return f"{month_name} {day}, {year}"
 
 
def main():
    """Get a date from the user and print it with the month spelled out."""
    try:
        text = get_date_text()
        month, day, year = parse_date(text)
        print(format_date(month, day, year))
    except ValueError as error:
        print(f"Invalid date: {error}")
    except (EOFError, KeyboardInterrupt):
        print("\nNo date was entered. Exiting.")
 
 
main()
