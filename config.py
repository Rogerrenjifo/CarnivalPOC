"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2024, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: config.py                                                              #
# Project: CarnivalPOC                                                         #
# Last Modified: Sunday, 21st January 2024 3:35:26 am                          #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""

from os import getenv

# You can set EDGE, FIREFOX or CHROME value
BROWSER = getenv("BROWSER", "EDGE")

# timeouts
IMPLICIT_TIMEOUT = int(getenv("IMPLICIT_TIMEOUT", "50"))
WAIT_TIMEOUT = int(getenv("WAIT_TIMEOUT", "10"))

# url
URL = getenv("URL", "https://www.carnival.com/")
