import random

print("<------------Calculating EmployeeDailyWage Based on Working Hours------------>\n")
print("<-------Switch Case------->")


class DailyWage:
    def __init__(self, wage_per_hour, emp_work_hour, emp_daily_wage):
        self.wage_per_hour = wage_per_hour
        self.emp_daily_wage = emp_daily_wage
        self.emp_work_hour = emp_work_hour

    """
       Defining a function name calculate Wage and declaring variables
    """

    # Now checking the employee is present or not
    def present_for_full_time(self):
        """
        this function is set to employee working hours as 8 hrs
        :return: emp_work_hour
        """
        self.emp_work_hour = 8
        return self.emp_work_hour

    def present_for_part_time(self):
        """
        this function is set to employee working hours as 4 hrs
        :return: emp_work_hour
        """
        self.emp_work_hour = 4
        return self.emp_work_hour

    def employee_absent(self):
        """
        this function is set to employee as absent
        :return: emp_work_hour
        """
        self.emp_work_hour = 0
        return self.emp_work_hour

    def switch_case(self):
        """
        implementing switch case in this function
        :return: emp_status
        """
        switch = {
            1: self.present_for_full_time(),
            0: self.present_for_part_time()
        }
        return switch.get(self, "")()

    def get_status(self):
        self.emp_work_hour
        check = random.randint(0, 1)
        if not check:
            return self.employee_absent()
        else:
            check = random.randint(0, 1)
            result = self.switch_case(0)

    def employee_daily_wage(self):
        print(self.emp_work_hour * self.wage_per_hour)
        return self


if __name__ == '__main__':
    calculate_wage = DailyWage(20, 0, 0)
    calculate_wage.employee_daily_wage()
    # Calculate the employee daily wage using random result