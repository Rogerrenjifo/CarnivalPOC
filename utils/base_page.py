"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: base_page.py                                                           #
# Project: CarnivalPOC                                                         #
# Last Modified: Sunday, 21st January 2024 3:39:07 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from selenium.webdriver.support.ui import WebDriverWait
from utils.driver.browser_factory import BrowserFactory
from config import WAIT_TIMEOUT


class BasePage:
    """Base class representing a generic web page.
    """
    def __init__(self) -> None:
        self._driver = BrowserFactory().get_driver()
        self._wait = WebDriverWait(self._driver, WAIT_TIMEOUT)
        