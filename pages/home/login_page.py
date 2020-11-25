from selenium.webdriver.common.by import By
from utilities.custom_logger import LogGen
from base.basepage import BasePage
import logging

class Login_page(BasePage):
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"
    text_invalidlogin_xpath ="//div[contains(text(),'Login was unsuccessful. Please correct the errors and try again.')]"
    text_usernametext_xpath = "//li[contains(text(),'John Smith')]"

    logger = LogGen.loggen()

    def clear_username(self):
        self.driver.find_element_by_id(self.textbox_username_id).clear()

    def clear_password(self):
        self.driver.find_element_by_id(self.textbox_password_id).clear()

    def enterEmail(self, username):
        self.sendKeys(username, self.textbox_username_id)

    def enterPassword(self, password):
        self.sendKeys(password, self.textbox_password_id)

    def clickLoginButton(self):
        self.elementClick(self.button_login_xpath, locatorType="xpath")

    def clickLogoutLink(self):
        self.elementClick(self.link_logout_linktext, locatorType="link")

    def login(self, username="", password=""):
        self.clear_username()
        self.clear_password()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def logout(self):
        self.clickLogoutLink()

    def verify_login_failed(self):
        resp = self.isElementPresent(self.text_invalidlogin_xpath,locatorType="xpath")
        return resp

    def verify_login_successful(self):
        result = self.isElementPresent(self.text_usernametext_xpath, locatorType="xpath")
        return  result

    def verifyTitle(self):
        return self.verifyPageTitle("Dashboard / nopCommerce administration")





