from sqlalchemy import create_engine, text
from config import *


class SwaggerDB:
    query = {
        'create_company': text('insert into company(name, description) values (:name, :description)'),
        'last_company_id': text('select MAX(id) from company'),
        'delete_company': text('delete from company where id = :company_id'),
        'employee_list': text('select * from employee where company_id = :company_id'),
        'one_employee': text('select * from employee where company_id = :c_id and id = :e_id'),
        'last_employee_id': text('select MAX(id) from employee where company_id = :c_id'),
        'employee_create': text('insert into employee(company_id, first_name, last_name, phone) values (:c_id, :name, :surname, :number)'),
        'employee_patch': text('update employee set last_name = :new_last_name, phone = :new_phone where id = :e_id'),
        'employee_delete': text('delete from employee where id = :e_id')
    }

    def __init__(self, db_connection_string:str):
        self.db = create_engine(db_connection_string)

    def create_company(self, com_name:str, com_description:str):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["create_company"], parameters=dict(name=com_name, description = com_description))
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('company was successfully created in DB')

    def get_last_company_id(self):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["last_company_id"]).fetchall()[0][0]
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('last created company id was successfully received from DB')

    def delete_company(self, id:int):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["delete_company"], parameters=dict(company_id = id))
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('company was successfully deleted in DB')
    
    def get_all_company_employees(self, id:int):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["employee_list"], parameters=dict(company_id = id)).all()
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('a list of company employees was successfully received from DB')

    def get_employee_by_id(self, company_id:int, employee_id:int):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["one_employee"], parameters=dict(c_id = company_id, e_id = employee_id))
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('employee was successfully received from DB')

    def get_last_employee_id(self, company_id:int):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["last_employee_id"], parameters=dict(c_id = company_id)).fetchall()[0][0]
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('last created employee id was successfully received from DB')

    def create_employee(self, company_id:int, first_name:str, last_name:str, phone:str):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["employee_create"], parameters=dict(c_id = company_id, name = first_name, surname = last_name, number = phone))
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('employee was successfully created in DB')

    def patch_employee(self, last_name:str, phone:str, employee_id:int):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["employee_patch"], parameters=dict(new_last_name = last_name, new_phone = phone, e_id = employee_id))
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('employee was successfully patched in DB')

    def delete_employee(self, employee_id:int):
        try:
            with self.db.connect() as conn:
                response = conn.execute(self.query["employee_delete"], parameters=dict(e_id = employee_id))
                conn.commit()
                return response
        except Exception as ex:
            print('an ERROR occured', ex)
        finally:
            if conn :
                conn.close()
                print('employee was successfully deleted from DB')
