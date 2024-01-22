"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: carnival.py                                                            #
# Project: CarnivalPOC                                                         #
# Last Modified: Sunday, 21st January 2024 3:54:54 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from pages.home_page import HomePage
from pages.cruise_search_page import CruiseSearchPage
from utils.driver.browser_factory import BrowserFactory
from config import URL


class Carnival:
    """ Class representing the Carnival website automation.
    
    Usage:
        carnival_instance = Carnival()
        carnival_instance.navigate_to("https://www.carnival.com/")
        carnival_instance.close_page()
    """
    def __init__(self) -> None:
        self._driver = BrowserFactory().get_driver()
        self.home = HomePage()
        self.cruise_search = CruiseSearchPage()
        self._driver.get(URL)

    def navigate_to(self, url):
        """Navigates to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        if self._driver:
            self._driver.get(url)

    def close_page(self):
        """Closes the WebDriver instance.
        """
        if self._driver:
            self._driver.quit()

    def get_current_url(self):
        """
        Get the current URL of the web page.

        Returns:
            str: The current URL as a string.
        """
        return self._driver.current_url

    def reload_page(self):
        """This method refreshes the page by reloading it.
        """
        self._driver.refresh()
