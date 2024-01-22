"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: smoke_test.py                                                          #
# Project: CarnivalPOC                                                         #
# Last Modified: Monday, 22nd January 2024 2:27:14 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


import pytest
from test_data import search_data
from pages.carnival import Carnival


@pytest.fixture(scope="class")
def navigate_to_seachpage(request):
    carnival = Carnival()
    carnival.home.close_cookie_policy()
    carnival.home.select_sail_to_option(search_data.SAIL_TO)
    carnival.home.select_duration_option(search_data.DURATION)
    carnival.home.click_on_search_button()

    request.addfinalizer(carnival.close_page)
    return carnival


class TestSmoke:
    """_summary_
    """

    def test_validate_the_cruise_Search_page_is_displayed(self, navigate_to_seachpage):
        """FR-6 Validate the cruise-search page is displayed.
        """
        carnival: Carnival = navigate_to_seachpage
        assert '/cruise-search' in carnival.get_current_url(), "The /cruise-search does not load"

    def test_validate_search_for_Cruises_to_The_Bahamas_with_Duration_6_9_days(self, navigate_to_seachpage):
        """ FR-5 Validate Search for Cruises to The Bahamas with Duration 6-9 days.
        """
        carnival: Carnival = navigate_to_seachpage
        assert "The Bahamas" in carnival.cruise_search.get_selected_filters()
        assert "6 Days" in carnival.cruise_search.get_selected_filters()
        assert "7 Days" in carnival.cruise_search.get_selected_filters()
        assert "8 Days" in carnival.cruise_search.get_selected_filters()
        assert "9 Days" in carnival.cruise_search.get_selected_filters()

    def test_validate_search_result_is_displayed_as_grid_by_default(self, navigate_to_seachpage):
        """Fr-19 Validate search results are displayed as grid by default."""
        carnival: Carnival = navigate_to_seachpage
        assert "grid" == carnival.cruise_search.get_display_attribute_of_trip_options()

    def test_validate_filter_trips_by_price_using_the_slider_bar(self, navigate_to_seachpage):
        """FR-8 Validate Filter Bahamas cruises by price range using slider bar.
        """
        carnival: Carnival = navigate_to_seachpage
        carnival.reload_page()
        carnival.cruise_search.click_vacation_budget_button()
        carnival.cruise_search.move_left_slider_thumb_to(search_data.SLIDER_THUMB_POSITION)
        min_value , max_value = carnival.cruise_search.get_min_and_max_filter_price()
        prices = carnival.cruise_search.get_prices()
        assert all(min_value <= x <= max_value for x in prices)

    def test_validate_search_result_is_sortable_by_price(self, navigate_to_seachpage):
        """ FR-9 Validate Sort Bahamas cruises by price.
        """
        carnival: Carnival = navigate_to_seachpage
        carnival.reload_page()
        carnival.cruise_search.select_sort_by_option(search_data.HIGH_TO_LOW)
        prices = carnival.cruise_search.get_prices()
        assert prices == sorted(prices, reverse=True)
