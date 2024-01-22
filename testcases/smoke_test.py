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
from pages.carnival import Carnival
from test_data import itinerary_data

@pytest.fixture(scope="class")
def navigate_to_itinerary_page(request):
    carnival = Carnival()
    carnival.home.close_cookie_policy()
    carnival.home.click_on_search_button()
    carnival.cruise_search.click_on_itinerary_link()

    request.addfinalizer(carnival.close_page)
    return carnival


class TestSmokeUserStory02:
    """This class contain the test cases for the user story 02
    """

    def test_validate_itinerary_page_is_displayed(self, navigate_to_itinerary_page):
        carnival: Carnival = navigate_to_itinerary_page
        assert '/itinerary/' in carnival.get_current_url(), "The /itinerary/ does not load"

    def test_validate_the_information_of_activities_is_displayed_by_day(self, navigate_to_itinerary_page):
        """
        This test case extract the number of days from the title and get the title 
        of the itineraty, use that information to verify if the itinerary has information
        for all the days.
        """
        # Get the trip and itinerary information titles.
        carnival: Carnival = navigate_to_itinerary_page
        trip_title = carnival.itinerary.get_trip_title()
        titles = carnival.itinerary.get_itinerary_titles()
        # extract the days of the trip from the title
        trip_days = int(''.join(filter(str.isdigit, trip_title)))
        # verify if it is a itinerary information for every day
        for day in range(1, trip_days + 1):
            assert str(day) in " ".join(titles)

    def test_validate_itinerary_page_has_a_button_called_book_now(self, navigate_to_itinerary_page):
        carnival: Carnival = navigate_to_itinerary_page
        button_name = carnival.itinerary.get_booking_button_name()
        assert itinerary_data.BOOKING_BUTTON_NAME in button_name

    def test_validate_itinerary_page_has_button_to_start_booking(self, navigate_to_itinerary_page):
        carnival: Carnival = navigate_to_itinerary_page
        carnival.itinerary.click_start_booking_button()
        assert "/booking/" in carnival.get_current_url(), "The /booking/ does not load"
