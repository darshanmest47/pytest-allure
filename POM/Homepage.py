from selenium.webdriver.common.by import By

from POM.Basepage import Basepage


class Homepage(Basepage):
    dashes = (By.CSS_SELECTOR, "div.head>h1")

    def verify_dash(self):
        return self.verify_cont(self.dashes)
