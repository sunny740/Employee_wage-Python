import logging
logging.basicConfig(filename='Emp_DailyWage.log', encoding='utf-8', level=logging.DEBUG, filemode='a')
import random


def emp_wage():
    """
    This function computes wage of an employee
    :return: None
    """
    try:
        # is_full_time = 1
        # emp_rate_per_hour = 20
        # full_time_hour = 8
        
        emp_status = random.randint(0, 1)
        if emp_status == 1:
            print("Employee is Present")
            employee_wage = 8 * 20
            print("Employee Wage for a Day: ", employee_wage)
        else:
            print("Employee is Absent")
    except Exception as Ex:
        logging.exception(Ex)


if __name__ == '__main__':
    emp_wage()