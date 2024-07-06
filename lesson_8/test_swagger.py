from swagger_api import *
import pytest

# get_employee
def test_positive_get_emp(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    res = emp.get_all_employees(company_id)
    assert res.status_code == 200
    del_com = emp.company_delete(token, company_id)
    assert del_com == 200

@pytest.mark.xfail()
@pytest.mark.parametrize('company_id', 
    [None, 
     '', 
     ' ', 
     'abc'
    ])
def test_negative_get_emp(url, company_id):
    # no company_id
    emp = SwaggerApi(url)
    res = emp.get_all_employees(company_id)
    assert res.status_code == 200

# add_employee
def test_positive_add_employee(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    com_emp_before = emp.get_all_employees(company_id).json()
    new_employee_body = emp.employee_body(1, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    assert employee_id != None
    com_emp_after = emp.get_all_employees(company_id).json()
    assert (len(com_emp_after) - len(com_emp_before)) == 1

@pytest.mark.xfail()
def test_negative_add_employee_no_body(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(2, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, None)
    assert employee_id != None

@pytest.mark.xfail()
def test_negative_add_employee_no_token(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(2, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(None, new_employee_body)
    assert employee_id != None

@pytest.mark.xfail()
def test_negative_add_employee_nothing(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(2, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(None, None)
    assert employee_id != None

# get_employee_by_id
def test_positive_get_employee_by_id(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(3, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    get_emp = emp.employee_get_by_id(employee_id)
    assert get_emp.status_code == 200

@pytest.mark.xfail()
def test_negative_get_employee_by_id(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    get_emp = emp.employee_get_by_id(None)
    assert get_emp.status_code == 200

# patch_employee
@pytest.mark.xfail()
def test_positive_patch_employee(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    patch_body = {"phone": "+123456789"}
    patched_employee = emp.employee_patch(employee_id, token, patch_body)
    assert patched_employee.status_code == 201  # получаем код 200 вместо 201, тело неполное

@pytest.mark.xfail()
def test_negative_patch_employee_no_emp_id(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    patch_body = {"phone": "+123456789"}
    patched_employee = emp.employee_patch(None, token, patch_body)
    assert patched_employee.status_code == 201

@pytest.mark.xfail()
def test_negative_patch_employee_token(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    patch_body = {"phone": "+123456789"}
    patched_employee = emp.employee_patch(employee_id, None, patch_body)
    assert patched_employee.status_code == 201

@pytest.mark.xfail()
def test_negative_patch_employee_no_body(url):
    emp = SwaggerApi(url)
    token = emp.company_auth_get_token()
    company_id = emp.company_create_get_id(token)
    new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
    employee_id = emp.employee_create(token, new_employee_body)
    patched_employee = emp.employee_patch(employee_id, token, None)
    assert patched_employee.status_code == 201
