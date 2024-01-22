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
from selenium.webdriver.support import expected_conditions as EC
from utils.base_page import BasePage


class HomePage(BasePage):
    """Represents the home page of the cruise website.
    """

    def __init__(self) -> None:
        super().__init__()
        self._sail_to_button = [By.CSS_SELECTOR, "#cdc-destinations"]
        self._sail_from_button = [By.CSS_SELECTOR, "#cdc-ports"]
        self._dates_button = [By.CSS_SELECTOR, "#cdc-dates"]
        self._duration_button = [By.CSS_SELECTOR, "#cdc-durations"]
        self._search_cruises_button = [By.CSS_SELECTOR, ".cdc-filters-tab--searchcta"]
        self._filter_options = [By.XPATH, "//button[contains(text(), '{}')]"]
        self._cookie_policy_close_button = [By.CSS_SELECTOR, "#cookie-consent-btn"]

    def select_sail_to_option(self, option):
        """
        Initializes a new instance of the HomePage class.

        Args:
            option (string): The Sail to option to select
        """
        self._driver.find_element(*self._sail_to_button).click()
        filter_option = (
            self._filter_options[0],
            self._filter_options[1].format(option),
        )
        self._driver.find_element(*filter_option).click()
        self._wait.until(
            EC.text_to_be_present_in_element_attribute(
                filter_option, "aria-label", "selected"
            )
        )

    def select_duration_option(self, option):
        """
        Selects the 'Duration' option from the dropdown.

        Args:
            option (str): The duration option to select.
        """
        self._driver.find_element(*self._duration_button).click()
        filter_option = (
            self._filter_options[0],
            self._filter_options[1].format(option),
        )
        self._driver.find_element(*filter_option).click()
        self._wait.until(
            EC.text_to_be_present_in_element_attribute(
                filter_option, "aria-label", "selected"
            )
        )

    def click_on_search_button(self):
        """Clicks on the 'Search Cruises' button.
        """
        self._driver.find_element(*self._search_cruises_button).click()

    def close_cookie_policy(self):
        """Close the cookie policy popup
        """
        self._driver.find_element(*self._cookie_policy_close_button).click()
