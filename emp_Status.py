import logging
logging.basicConfig(filename='Emp_Status.log', encoding='utf-8', level=logging.DEBUG, filemode='a')

import random

def emp_wage_comp():
    """
    This function used to find employee status that Employee present or not
    :return: None
    """
    try:
        emp_status = random.randint(0, 1)

        if emp_status == 1:
            # logging.info("Employee is Present")
            print("Employee is Present:")

        else:
            # logging.info("Employee is not present")
            print("Employee is Absent:")

    except Exception as EX:
        logging.exception(EX)


if __name__ == '__main__':
    emp_wage_comp()