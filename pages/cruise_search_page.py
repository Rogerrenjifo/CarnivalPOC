"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: cruise_search_page.py                                                  #
# Project: CarnivalPOC                                                         #
# Last Modified: Sunday, 21st January 2024 4:02:08 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class CruiseSearchPage(BasePage):
    """ Page class representing the Cruise Search page on the Carnival website.
    """
    def __init__(self) -> None:
        super().__init__()
        self._vacation_budget_button = [By.CSS_SELECTOR, "[data-testid='pricingFilterButton']"]
        self._itinerary_link = [By.CSS_SELECTOR, "[data-testid*='cg-itinerary']"]

    def click_on_itinerary_link(self):
        """Click on the itinerary link.
        """
        self._driver.find_element(*self._itinerary_link).click()
