import pytest


from emp_Status import Employee, Company, MultipleCompanies


@pytest.fixture
def emp_parameters():
    return {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}


def test_check_employee_name(emp_parameters):
    # emp_parameters = {}
    test_object = Employee(emp_parameters)
    test_object.calculate_wage()
    assert isinstance(test_object.total_wage, int)

def test_add_employee(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    assert len(company.employee_dict) == 0
    company.add_emp(employee)
    assert len(company.employee_dict) == 1

def test_get_employee(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    company.add_emp(employee)
    com = company.get_emp("sunil")
    assert com == employee

def test_delete_employee(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    company.add_emp(employee)
    assert len(company.employee_dict) == 1
    company.delete_emp("sunil")
    assert len(company.employee_dict) == 0

def test_update_employee(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    company.add_emp(employee)
    update_parameters = {"update_wage": 30,"update_working_hours": 20, "update_working_days": 10}
    company.update_emp(employee, update_parameters)
    assert employee.emp_wage == 30
    assert employee.max_working_hrs == 20
    assert employee.max_working_days == 10

def test_add_company(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    company.add_emp(employee)
    multi = MultipleCompanies()
    multi.add_company(company)
    assert len(multi.company_dict) == 1


def test_get_company(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    multi = MultipleCompanies()
    multi.add_company(company)
    get = multi.get_company_object("TCS")
    assert get == company 

def test_remove_comapny(emp_parameters):
    # emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
    employee = Employee(emp_parameters)
    company = Company("TCS")
    multi = MultipleCompanies()
    multi.add_company(company)
    multi.remove_company("TCS")
    assert not multi.get_company_object("TCS")

    



    # assert employee.emp_name == "sunil"
    # assert employee.emp_name != "mahesh"



    # company = Company("TCS")
    # company.add_emp(employee)
    # assert employee == company.get_emp("sunil")



    # multiplecompanies = MultipleCompanies()
    # multiplecompanies.add_company(company)
    # assert company == multiplecompanies.get_company_object("TCS")



# def test_check_employee_name():
#     emp_parameters = {"employee_name": "sunil", "employee_wage": 20,"maximum_working_hrs": 10, "maximum_working_days": 5}
#     test_object = Employee(emp_parameters)
#     test_object.calculate_wage()
#     assert isinstance(test_object.total_wage, int)

