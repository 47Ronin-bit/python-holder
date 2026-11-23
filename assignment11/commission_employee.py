from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, department, base_pay, commission):
        super().__init__(name, department, 0)
        self._base_pay = base_pay
        self._commission = commission

    # Overrides Employee.get_annual_pay
    def get_annual_pay(self):
        return self._base_pay + self._commission

    # Overrides Employee.get_title
    def get_title(self):
        return "Commission Employee"

    # Only commission employees have this method
    def get_breakdown(self):
        percent = self._commission / self.get_annual_pay() * 100
        return ("Base $" + format(self._base_pay, ".2f") +
                " + Commission $" + format(self._commission, ".2f") +
                " (" + format(percent, ".1f") + "% of earnings)")