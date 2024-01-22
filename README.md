# CarnivalPOC
This repository contains a UI testing framework built with Python, ScreenPy, Selenium, and Pytest for automating tests on a Carnival web page. The framework is designed to provide a scalable and maintainable solution for testing the user interface of the Carnival website.


Python 3.11.5

# Install virtualenv

> pip install virtualenv

# Create a virtual environment 

> virtualenv venv -p 3.11.5

# Activate Virtual environment
> source venv/Scripts/activate    (Git Bash on windows)
> venv\Scripts\activate           (Windows)
> source venv/bin/activate        (macOS, Linux)

# Install requirements

> pip install -r requirements.txt

# set config variables.

you can change the browser, url, and timeout in the config.py file or set it as environment variables
```
BROWSER=
IMPLICIT_TIMEOUT=
WAIT_TIMEOUT=
URL= 
```

# run the test cases 

> pytest testcases/smoke_test.py 

# Generate The report (allure must be installed)
> allure serve allure-results
