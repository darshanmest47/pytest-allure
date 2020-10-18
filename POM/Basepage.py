from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    def __init__(self, driver):
        self.driver = driver

    def enter_vals(self, locator, value):
        wait = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(value)

    def click_btn(self, locator):
        wait = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def check_element_present(self, locator):
        wait = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()

    def get_pgtitle(self):
        return self.driver.title

    def verify_cont(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator).text
