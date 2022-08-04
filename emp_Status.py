import random
import logging
logging.basicConfig(filename="emp_Status.log", encoding='utf-8', level=logging.DEBUG, filemode='a')

def wage_computation():
    """
    This function computes wage of an employee
    :return: None
    """

    try:
        is_absent = 0
        # is_full_time = 1
        # is_part_time = 2
        # full_time_hour = 8
        # part_time_hour = 4
        # employee_wage_per_hour = 20
        max_working_days = 20
        max_working_hours = 100
        employee_wage_for_month = 0
        employee_working_days = 0
        employee_working_hours = 0

        while employee_working_days < max_working_days and employee_working_hours <= max_working_hours:
            employee_status = random.randint(0, 2)

            if employee_status == 1:
                employee_wage = 8 * 20
                employee_hours = 8
                print("Employee Worked Full Day: ", employee_wage)

            elif employee_status == 2:
                employee_wage = 4 * 20
                employee_hours = 4
                print("Employee Worked Half Day: ", employee_wage)
            else:
                print("Employee is Absent")
                employee_wage = is_absent * 20
                employee_hours = is_absent

            employee_wage_for_month += employee_wage
            employee_working_hours += employee_hours
            employee_working_days += 1
        print("\nNumber of Days Employee Worked: ", employee_working_days)
        print("Number of Hours Employee Worked: ", employee_working_hours)
        print("Employee wage for a Month: ", employee_wage_for_month)
    except Exception as ex:
        logging.exception(ex)


if __name__ == '__main__':
    wage_computation()