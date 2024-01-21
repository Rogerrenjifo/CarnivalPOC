"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: singleton.py                                                           #
# Project: CarnivalPOC                                                         #
# Last Modified: Saturday, 20th January 2024 7:17:44 pm                        #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


class Singleton(type):
    """
    This is the singleton class to created only one instance of the
    classes that need to guarantee that exists only one instance of
    itself
    Returns:
        Instance: object of instanced class
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Method to create and return the instance class if it has not been
        created, create the instance
        Returns:
            Instance: object of instanced class
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
