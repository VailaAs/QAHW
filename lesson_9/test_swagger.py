from swagger_api import *
from config import *
from swagger_db import *
import pytest

api = SwaggerApi('https://x-clients-be.onrender.com/')
db = SwaggerDB('postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx')

# create company in db
def test_get_all_employees():
    db.create_company('cool_name', 'really cool company')
    company_id = db.get_last_company_id()
    db.create_employee(company_id, 'Vie', 'Tank', 'yes')
    dbe = db.get_all_company_employees(company_id)
    apie = api.get_all_employees(company_id)
    employee_id = db.get_last_employee_id(company_id)
    assert len(dbe) == len(apie)

    db.delete_employee(employee_id)
    db.delete_company(company_id)

def test_create_employee():
    db.create_company('cool_name', 'really cool company')
    company_id = db.get_last_company_id()
    dbe_before = db.get_all_company_employees(company_id)
    db.create_employee(company_id, 'Vie', 'Tank', 'yes')
    dbe_after = db.get_all_company_employees(company_id)
    apie = api.get_all_employees(company_id)
    employee_id = db.get_last_employee_id(company_id)
    assert len(dbe_after) - len(dbe_before) == 1
    assert len(dbe_after) == len(apie)

    db.delete_employee(employee_id)
    db.delete_company(company_id)

def test_get_employee_by_id():
    db.create_company('cool_name', 'really cool company')
    company_id = db.get_last_company_id()
    db.create_employee(company_id, 'Vie', 'Tank', 'yes')
    employee_id = db.get_last_employee_id(company_id)
    dbe = db.get_employee_by_id(company_id, employee_id).all()[0][0]
    apie = api.employee_get_by_id(employee_id).json()['id']
    # check if employee_ids match
    assert dbe == apie

    db.delete_employee(employee_id)
    db.delete_company(company_id)

def test_patch_employee():
    db.create_company('cool_name', 'really cool company')
    company_id = db.get_last_company_id()
    db.create_employee(company_id, 'Vie', 'Tank', 'yes')
    employee_id = db.get_last_employee_id(company_id)
    db.patch_employee('New_Tank', 'yes', employee_id)
    db_new_last_name = db.get_employee_by_id(company_id, employee_id).all()[0][5]
    api_new_last_name = api.employee_get_by_id(employee_id).json()['lastName']
    # check if patch matches
    assert db_new_last_name == api_new_last_name

    db.delete_employee(employee_id)
    db.delete_company(company_id)









# get_employee
# def test_positive_get_emp(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     res = emp.get_all_employees(company_id)
#     assert res.status_code == 200
#     del_com = emp.company_delete(token, company_id)
#     assert del_com == 200

# @pytest.mark.xfail()
# @pytest.mark.parametrize('company_id', 
#     [None, 
#      '', 
#      ' ', 
#      'abc'
#     ])
# def test_negative_get_emp(url, company_id):
#     # no company_id
#     emp = SwaggerApi(url)
#     res = emp.get_all_employees(company_id)
#     assert res.status_code == 200

# # add_employee
# def test_positive_add_employee(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     com_emp_before = emp.get_all_employees(company_id).json()
#     new_employee_body = emp.employee_body(1, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     assert employee_id != None
#     com_emp_after = emp.get_all_employees(company_id).json()
#     assert (len(com_emp_after) - len(com_emp_before)) == 1

# @pytest.mark.xfail()
# def test_negative_add_employee_no_body(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(2, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, None)
#     assert employee_id != None

# @pytest.mark.xfail()
# def test_negative_add_employee_no_token(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(2, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(None, new_employee_body)
#     assert employee_id != None

# @pytest.mark.xfail()
# def test_negative_add_employee_nothing(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(2, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(None, None)
#     assert employee_id != None

# # get_employee_by_id
# def test_positive_get_employee_by_id(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(3, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     get_emp = emp.employee_get_by_id(employee_id)
#     assert get_emp.status_code == 200

# @pytest.mark.xfail()
# def test_negative_get_employee_by_id(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     get_emp = emp.employee_get_by_id(None)
#     assert get_emp.status_code == 200

# # patch_employee
# @pytest.mark.xfail()
# def test_positive_patch_employee(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     patch_body = {"phone": "+123456789"}
#     patched_employee = emp.employee_patch(employee_id, token, patch_body)
#     assert patched_employee.status_code == 201  # получаем код 200 вместо 201, тело неполное

# @pytest.mark.xfail()
# def test_negative_patch_employee_no_emp_id(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     patch_body = {"phone": "+123456789"}
#     patched_employee = emp.employee_patch(None, token, patch_body)
#     assert patched_employee.status_code == 201

# @pytest.mark.xfail()
# def test_negative_patch_employee_token(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     patch_body = {"phone": "+123456789"}
#     patched_employee = emp.employee_patch(employee_id, None, patch_body)
#     assert patched_employee.status_code == 201

# @pytest.mark.xfail()
# def test_negative_patch_employee_no_body(url):
#     emp = SwaggerApi(url)
#     token = emp.company_auth_get_token()
#     company_id = emp.company_create_get_id(token)
#     new_employee_body = emp.employee_body(4, "Anna", "L", "", company_id, "email1@email.com", "", "yes", "2002-06-24")
#     employee_id = emp.employee_create(token, new_employee_body)
#     patched_employee = emp.employee_patch(employee_id, token, None)
#     assert patched_employee.status_code == 201
