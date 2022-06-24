import os
import sys

from altunityrunner.exceptions import NotFoundException, WaitTimeOutException

sys.path.append(os.path.dirname(__file__))


class BasePage:

    def __init__(self, altdriver):
        self.altdriver = altdriver

    def is_element_present(self, how, what):
        try:
            self.altdriver.find_object(how, what)
        except NotFoundException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            self.altdriver.wait_for_object(how, what, timeout)
        except WaitTimeOutException:
            return True
        return False
