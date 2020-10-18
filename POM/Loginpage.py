from selenium.webdriver.common.by import By

from POM.Basepage import Basepage
from POM.Homepage import Homepage
from utilities.Common import Common


class Loginpage(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
        # driver.get(Common().url)

    name_fld = (By.XPATH, "//input[@name='txtUsername']")
    pass_fld = (By.XPATH, "//input[@name='txtPassword']")
    submit_fld = (By.XPATH, "//input[@name='Submit']")
    for_pass = (By.LINK_TEXT, "Forgot your password?")
    inv_msg = (By.XPATH, "//div[@id='divLoginButton']/span")

    def entervalsintoname(self,val1):
        self.enter_vals(self.name_fld, val1)

    def entervalsintopass(self,val2):
        self.enter_vals(self.pass_fld, val2)

    def checkelementpresence(self):
        return self.check_element_present(self.for_pass)

    def perform_click(self):
        self.click_btn(self.submit_fld)
        hp = Homepage(self.driver)
        return hp

    def verify_pg_title(self):
        return self.get_pgtitle()


