from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, department, salary)

    # Overrides Employee.get_title
    def get_title(self):
        return "Salaried Employee"