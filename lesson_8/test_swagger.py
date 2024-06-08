from swagger_api import *

def test_swag(url):
    com = CompanyApi(url)
    res = com.company_auth()
    assert res.status_code == 201