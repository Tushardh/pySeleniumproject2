"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from utilities.custom_logger import LogGen
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    logger = LogGen.loggen()

    def __init__(self, driver):
        super().__init__(driver)
        self.resultlist =[]

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.logger.info("### Verification Successful ::"+ result_message)
                else:
                    self.resultlist.append("FAIL")
                    self.logger.info("### Verification Failed ::" + result_message)
                    self.screenShot(result_message)
            else:
                self.resultlist.append("FAIL")
                self.logger.error("### Verification Failed ::" + result_message)
                self.screenShot(result_message)
        except:
            self.resultlist.append("FAIL")
            self.logger.error("### Exception Occurred !!!")
            self.screenShot(result_message)

    def mark(self,result, result_message):
        """ Mark the result of the verification point in a test case    """
        self.set_result(result, result_message)

    def final_mark(self,testname, result, result_message):
        """
                Mark the final result of the verification point in a test case
                This needs to be called at least once in a test case
                This should be final test status of the test case
         """
        self.set_result(result, result_message)

        if "FAIL" in self.resultlist:
            self.logger.error(testname + " ### TEST FAILED")
            self.resultlist.clear()
            assert True == False
        else:
            self.logger.error(testname + " ### TEST PASSED")
            self.resultlist.clear()
            assert True == True







