class Employee:
    def __init__(self, name, department, annual_pay):
        self._name = name
        self._department = department
        self._annual_pay = annual_pay

    def get_name(self):
        return self._name

    def get_department(self):
        return self._department

    def get_annual_pay(self):
        return self._annual_pay

    # Subclasses override this to give their own label
    def get_title(self):
        return "Employee"

    def __str__(self):
        return self._name + " (" + self.get_title() + "): $" + format(self.get_annual_pay(), ".2f")