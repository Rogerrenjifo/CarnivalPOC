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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utils.base_page import BasePage


class CruiseSearchPage(BasePage):
    """ Page class representing the Cruise Search page on the Carnival website.
    """
    def __init__(self) -> None:
        super().__init__()
        self._vacation_budget_button = [By.CSS_SELECTOR, "[data-testid='pricingFilterButton']"]
        self._sort_by_options = [By.CSS_SELECTOR, "[data-testid='sortBySelect']"]
        self._results_options = [By.CSS_SELECTOR, "[data-testid='tripTile']"]
        self._result_option_price = [By.CSS_SELECTOR, "[data-testid='priceAmount']"]
        self._itinerary_link = [By.CSS_SELECTOR, "[data-testid*='cg-itinerary']"]
        self._load_more_results_button = [By.CSS_SELECTOR, "[data-testid='loadMoreResults']"]
        self._selected_filters = [By.CSS_SELECTOR, "div[data-testid*='selected-Filter']"]
        self._left_slider_thumb = [By.CSS_SELECTOR, "span[data-index='0'].MuiSlider-thumb"]
        self._right_slider_thumb = [By.CSS_SELECTOR, "span[data-index='1'].MuiSlider-thumb"]
        self._slider_bar = [By.CSS_SELECTOR, ".MuiSlider-track"]
        self._min_price = [By.CSS_SELECTOR, "[data-testid='minPriceInput']"]
        self._max_price = [By.CSS_SELECTOR, "[data-testid='maxPriceInput']"]

    def click_load_more_results_button(self):
        """Clicks the Load More Results button on the Cruise Search page.
        """
        self._driver.find_element(*self._load_more_results_button).click()

    def click_vacation_budget_button(self):
        """Clicks the Vacation Budget button on the Cruise Search page.
        """
        self._driver.find_element(*self._vacation_budget_button).click()

    def select_sort_by_option(self, option):
        """Selects a sorting option from the Sort By dropdown on the Cruise Search page.

        Args:
            option (str): The value of the sorting option to select.
        """
        select_element = self._driver.find_element(*self._sort_by_options)
        select = Select(select_element)
        select.select_by_value(option)

    def get_selected_filters(self):
        """Get the text of all selected filters.

        Returns:
            list: A list of strings representing the text of selected filters.
        """
        selected_filters = self._driver.find_elements(*self._selected_filters)
        return [filter.text for filter in selected_filters]

    def get_display_attribute_of_trip_options(self):
        """
        Get the CSS 'display' property value of the first trip option.

        Returns:
            str: The value of the 'display' property.
        """
        trips = self._driver.find_elements(*self._results_options)
        self._wait.until(
            EC.visibility_of(trips[0])
        )
        return trips[0].value_of_css_property("display")

    def move_left_slider_thumb_to(self, position):
        """
        Move the left slider thumb to the specified position.

        Args:
            position (int): The position to move the left slider thumb to.
        """
        source = self._driver.find_element(*self._left_slider_thumb)
        target = self._driver.find_element(*self._slider_bar)
        self.action_chains.click_and_hold(source).move_to_element(target)
        self.action_chains.move_by_offset(position, 0).release().perform()

    def move_right_slider_thumb_to(self, position):
        """
        Move the right slider thumb to the specified position.

        Args:
            position (int): The position to move the right slider thumb to.
        """
        source = self._driver.find_element(*self._right_slider_thumb)
        target = self._driver.find_element(*self._slider_bar)
        self.action_chains.click_and_hold(source).move_to_element(target)
        self.action_chains.move_by_offset(position, 0).release().perform()

    def get_prices(self):
        """
        Get the prices of all result options.

        Returns:
            list: A list of integers representing the prices.
        """
        option_prices = self._driver.find_elements(*self._result_option_price)
        return [int(''.join(filter(str.isdigit, price.text))) for price in option_prices]

    def get_min_and_max_filter_price(self):
        """
        Get the minimum and maximum filter prices.

        Returns:
            tuple: A tuple containing two integers - the minimum and maximum filter prices.
        """
        min_value = self._driver.find_element(*self._min_price).get_attribute("value")
        max_value = self._driver.find_element(*self._max_price).get_attribute("value")
        min_price = ''.join(filter(str.isdigit, min_value))
        max_price = ''.join(filter(str.isdigit, max_value))
        return int(min_price), int(max_price)

    def click_on_itinerary_link(self):
        """Click on the itinerary link.
        """
        self._driver.find_element(*self._itinerary_link).click()
