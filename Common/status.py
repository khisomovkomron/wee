from Common.CommonFuncs.webcommon import WebDriverFactory
import logging as logger
from traceback import print_stack


class Status(WebDriverFactory):
    def __init__(self, browser, stand):
        super().__init__(browser, stand)
        self.log = logger
        self.resultList = []

    def set_result(self, result, resultmessage):
        try:
            if result is not None:
                self.resultList.append("PASS")
                self.log.info("$$$ VERiFICATION SUCCESSFUL ::" + resultmessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("$$$ VERiFICATION FAILED :: " + resultmessage)
                self.screenshot(resultmessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("$$$ Exception Occured !!!")
            self.screenshot(resultmessage)
            print_stack()

    def mark(self, result, resultmessage):

        self.set_result(result, resultmessage)

    def mark_final(self, testname, result, resultmessage):

        self.set_result(result, resultmessage)

        if "Fail" in self.resultList:
            self.log.error(testname + " $$$ TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testname + " $$$ TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True