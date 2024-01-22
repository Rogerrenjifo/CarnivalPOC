"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: home_page.py                                                           #
# Project: CarnivalPOC                                                         #
# Last Modified: Saturday, 20th January 2024 11:55:02 pm                       #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class HomePage(BasePage):
    """Represents the home page of the cruise website.
    """

    def __init__(self) -> None:
        super().__init__()
        self._sail_to_button = [By.CSS_SELECTOR, "#cdc-destinations"]
        self._search_cruises_button = [By.CSS_SELECTOR, ".cdc-filters-tab--searchcta"]
        self._cookie_policy_close_button = [By.CSS_SELECTOR, "#cookie-consent-btn"]

    def click_on_search_button(self):
        """Clicks on the 'Search Cruises' button.
        """
        self._driver.find_element(*self._search_cruises_button).click()

    def close_cookie_policy(self):
        """Close the cookie policy popup
        """
        self._driver.find_element(*self._cookie_policy_close_button).click()
