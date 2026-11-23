class Procedure:
    # --- 1. Initializer ---
    def __init__(self, description, date, practitioner, charge):
        self.__description = description
        self.__date = date
        self.__practitioner = practitioner
        self.__charge = charge

    # --- 2. Accessor (getter) methods ---
    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charge(self):
        return self.__charge

    # --- 3. Mutator (setter) methods ---
    def set_description(self, description):
        self.__description = description

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charge(self, charge):
        if charge <= 0:
            raise ValueError("charge must be greater than 0")
        self.__charge = charge

    # --- 4. __str__ ---
    def __str__(self):
        return (f"Procedure: {self.__description}\n"
                f"Date: {self.__date}\n"
                f"Practitioner: {self.__practitioner}\n"
                f"Charge: {self.__charge:.2f}")


if __name__ == "__main__":
    # Quick demo of the class in action.
    procedure = Procedure("Physical Exam", "8-24-2019", "Dr. Irvine",
                          250.0)
    print(procedure)