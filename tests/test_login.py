import time

import pytest
import allure
from allure_commons.types import AttachmentType

from POM.Loginpage import Loginpage
from tests.Basetest import Basetest
from utilities.Common import Common


class Testlogin(Basetest):

    @allure.severity(allure.severity_level.BLOCKER)
    def test_one(self, valset):
        lp = Loginpage(self.driver)

        lp.entervalsintoname(valset['username'])
        time.sleep(2)
        lp.entervalsintopass(valset['password'])
        time.sleep(2)
        print(lp.checkelementpresence())
        time.sleep(2)

        txt = lp.verify_pg_title()

        assert txt == 'OrangeHRM'
        hp = lp.perform_click()
        print(lp.verify_pg_title())
        text_title = lp.verify_pg_title()
        assert text_title == Common().title
        
        txt = hp.verify_dash()
        
        if txt == Common().dash:
            assert True
        
        else:
            assert False


@pytest.fixture(params=Common().return_excelvals())
def valset(request):
    return request.param
