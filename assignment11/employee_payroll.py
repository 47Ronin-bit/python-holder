from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee


def load_employees():
    # Hard-coded mix of different pay types
    employees = [
        HourlyEmployee("Nick DeFalco", "Sales", 25, 40),
        SalaryEmployee("Applejack Johnson", "Sales", 44000),
        SalaryEmployee("Mario Dubois", "Sales", 77200),
        SalaryEmployee("Anthony Jo", "Engineering", 98000),
        Employee("Stephanie Johnson", "Engineering", 31200),
        CommissionEmployee("Dominic Togo", "Maintenance", 20000, 45000),
        HourlyEmployee("Christina Gonzalez", "Maintenance", 19.8, 40),
        HourlyEmployee("Geoffrey Dav", "HR", 65, 40)
    ]
    return employees


def main():
    employees = load_employees()

    # Group the employees into a dictionary keyed by department
    employee_dict = {}
    for emp in employees:
        department = emp.get_department()
        if department not in employee_dict:
            employee_dict[department] = []
        employee_dict[department].append(emp)

    first = True
    for department, emp_list in employee_dict.items():
        # Blank line between departments
        if not first:
            print()
        first = False

        print(f"Department: {department}")
        total = 0

        for emp in emp_list:
            # Polymorphism: each employee's own get_annual_pay is used
            print(f"    {emp}")
            total += emp.get_annual_pay()

            # Only commission employees have a breakdown
            if isinstance(emp, CommissionEmployee):
                print(f"        {emp.get_breakdown()}")

        print(f"Total Payroll: ${total:.2f}")


if __name__ == "__main__":
    main()