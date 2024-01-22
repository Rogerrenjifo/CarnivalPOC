"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: itinerary_page.py                                                      #
# Project: CarnivalPOC                                                         #
# Last Modified: Monday, 22nd January 2024 3:05:51 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from selenium.webdriver.common.by import By
from utils.base_page import BasePage


class ItineraryPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
        self._day_information = [By.CSS_SELECTOR, "[data-testid='dayTileContent']"]
        self._day_information_title = [By.CSS_SELECTOR, "[data-testid='dayTileContent'] h3"]
        self._trip_title = [By.CSS_SELECTOR, "[data-testid='cg-region']"]
        self._start_booking_button = [By.CSS_SELECTOR, "[data-testid='startBooking'] > a"]

    def get_trip_title(self):
        title = self._driver.find_element(*self._trip_title)
        return title.get_attribute('innerText')

    def get_itinerary_titles(self):
        titles = self._driver.find_elements(*self._day_information_title)
        return [title.text for title in titles]

    def get_booking_button_name(self):
        button = self._driver.find_element(*self._start_booking_button)
        return button.text

    def click_start_booking_button(self):
        self._driver.find_element(*self._start_booking_button).click()
