import random
import logging
logging.basicConfig(filename="Emp_wage_parttime.log", encoding='utf-8', level=logging.DEBUG, filemode='a')


def emp_wage_parttime():
    """
     This is Emp Wage function
    :return:
    """

    try:
        # empwage_per_hour = 20
        # is_full_time = 1
        # is_part_time = 2
        # full_time_hour = 8
        # part_time_hour = 4
        emp_status = random.randint(0, 2)

        if emp_status == 1:
            print("Employee is Present Full Day")
            emp_wage = 8 * 20
            print("Employee Wage", emp_wage)

        elif emp_status == 2:
            print("Employee is Present Only Half Day")
            emp_wage = 4 * 20
            print("Employee Wage for a Day: ", emp_wage)

        else:
            print("Employee is not present")

    except Exception as Ex:
        logging.exception(Ex)

if __name__ == '__main__':
    emp_wage_parttime()