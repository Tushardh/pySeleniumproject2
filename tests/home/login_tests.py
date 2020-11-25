from selenium import webdriver
from pages.home.login_page import *
from utilities.custom_logger import LogGen
import logging
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class Test_001_Login():

    @pytest.fixture(autouse=True)
    def class_setup(self,oneTimeSetUp):
        self.lp = Login_page(self.driver)
        self.ts = TestStatus(self.driver)


    # @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("admin@yourstore.com", "admin")
        # logger = LogGen.loggen()
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verify_login_successful()
        self.ts.final_mark("test_validLogin", result2, "Login was successful")

        self.lp.logout()

    # @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("admin@yourstore.com", "admin1")
        response = self.lp.verify_login_failed()
        assert response == True