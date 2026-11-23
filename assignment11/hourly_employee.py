from employee import Employee


class HourlyEmployee(Employee):
    WEEKS_PER_YEAR = 52

    def __init__(self, name, department, hourly_rate, hours_per_week):
        super().__init__(name, department, 0)
        self._hourly_rate = hourly_rate
        self._hours_per_week = hours_per_week

    # Overrides Employee.get_annual_pay
    def get_annual_pay(self):
        return self._hourly_rate * self._hours_per_week * HourlyEmployee.WEEKS_PER_YEAR

    # Overrides Employee.get_title
    def get_title(self):
        return "Hourly Employee"
    