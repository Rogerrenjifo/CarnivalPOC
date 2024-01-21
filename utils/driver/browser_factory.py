"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: browser_factory.py                                                     #
# Project: CarnivalPOC                                                         #
# Last Modified: Sunday, 21st January 2024 3:46:09 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from selenium.webdriver import (
    FirefoxOptions,
    ChromeOptions,
    EdgeOptions,
    Chrome,
    Edge,
    Firefox,
)
from utils.singleton import Singleton
from config import BROWSER, IMPLICIT_TIMEOUT


class BrowserFactory(metaclass=Singleton):
    """Singleton factory class for creating and managing WebDriver instances.

    Usage:
        factory = BrowserFactory()
        driver = factory.get_driver()
    """

    def __init__(self):
        self._browser = BROWSER
        self._implicit_timeout = IMPLICIT_TIMEOUT
        self._driver = None

    def get_driver(self):
        """Returns the WebDriver instance, creating it if necessary.

        If the WebDriver instance is not yet created, it initializes it based
        on the specified browser type.
        The WebDriver is configured with the default implicit wait timeout and maximizes the window.

        Raises:
            ValueError: invalid BROWSER value.

        Returns:
            (WebDriver): The configured WebDriver instance.
        """
        if self._driver is None:
            if self._browser == "CHROME":
                options = ChromeOptions()
                self._driver = Chrome(options=options)
            elif self._browser == "EDGE":
                options = EdgeOptions()
                self._driver = Edge(options=options)
            elif self._browser == "FIREFOX":
                options = FirefoxOptions()
                self._driver = Firefox(options=options)
            else:
                invalid_browser_message = (
                    "Supported browsers are 'CHROME', 'FIREFOX', and 'EDGE'."
                )
                raise ValueError(
                    f"Invalid browser: {self._browser}. {invalid_browser_message}"
                )
            self._driver.implicitly_wait(self._implicit_timeout)
            self._driver.maximize_window()

        return self._driver
