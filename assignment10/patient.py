class Patient:
    # --- 1. Initializer ---
    def __init__(self, first_name, middle_name, last_name, address, city,
                 state, zip_code, phone, emergency_contact,
                 emergency_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__emergency_contact = emergency_contact
        self.__emergency_phone = emergency_phone

    # --- 2. Accessor (getter) methods ---
    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone(self):
        return self.__phone

    def get_emergency_contact(self):
        return self.__emergency_contact

    def get_emergency_phone(self):
        return self.__emergency_phone

    # --- 3. Mutator (setter) methods ---
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone(self, phone):
        self.__phone = phone

    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact

    def set_emergency_phone(self, emergency_phone):
        self.__emergency_phone = emergency_phone

    # --- 4. __str__ ---
    def __str__(self):
        return (f"First Name: {self.__first_name}\n"
                f"Middle Name: {self.__middle_name}\n"
                f"Last Name: {self.__last_name}\n"
                f"Address: {self.__address}\n"
                f"City: {self.__city}\n"
                f"State: {self.__state}\n"
                f"ZIP: {self.__zip_code}\n"
                f"Phone: {self.__phone}\n"
                f"Emergency Contact: {self.__emergency_contact}\n"
                f"Emergency Phone: {self.__emergency_phone}")
