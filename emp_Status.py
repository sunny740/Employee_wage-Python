import logging
logging.basicConfig(filename="Empwage_month.log", encoding='utf-8', level=logging.DEBUG, filemode='a')

import random

def employee_wage():
    """
    Emp_Wage function Implemented
    :return:
    """
    try:
        empwage_working_days = 15
        empwage_per_hour = 20
        # IS_FULL_TIME = 1
        # IS_PART_TIME = 2
        # FULL_TIME_HOUR = 8
        # PART_TIME_HOUR = 4
        not_present = 0
        emp_month = 0
        emp_days = 0

        while emp_days < empwage_working_days:
            emp_status = random.randint(0, 2)

            if emp_status == 1:
                # print("Employee is Present Full Day")
                emp_wage = 8 * empwage_per_hour
                print("Employee worked ", emp_wage)

            elif emp_status == 2:
                # print("Employee is Present Only Half Day")
                emp_wage = 4 * empwage_per_hour
                print("Employee not worked: ", emp_wage)

            else:
                print("Employee is not present")
                emp_wage = not_present * empwage_per_hour

                emp_month += emp_wage
                emp_days += 1

        logging.info("EmpWage_Month" + str(emp_month))


    except Exception as Ex:
        logging.exception(Ex)

if __name__ == "__main__":
    employee_wage()