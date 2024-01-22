# CarnivalPOC
This repository contains a UI testing framework built with Python, ScreenPy, Selenium, and Pytest for automating tests on a Carnival web page. The framework is designed to provide a scalable and maintainable solution for testing the user interface of the Carnival website.


Python 3.11.5

### Install virtualenv
```sh
> pip install virtualenv
```

### Create a virtual environment 
```sh
> virtualenv venv -p 3.11.5
```

### Activate Virtual environment
```sh
> source venv/Scripts/activate    (Git Bash on windows)
> venv\Scripts\activate           (Windows)
> source venv/bin/activate        (macOS, Linux)
``` 

### Install requirements
```sh
> pip install -r requirements.txt
```

### set config variables.

you can change the browser, url, and timeout in the config.py file or set it as environment variables
```
BROWSER=
IMPLICIT_TIMEOUT=
WAIT_TIMEOUT=
URL= 
```

### run the test cases 
```sh
> pytest testcases/smoke_test.py 
```

### Generate The report (allure must be installed)
```sh
> allure serve allure-results
```


# Documentation
[pytest](https://docs.pytest.org/en/7.1.x/contents.html) - To create and execute the test cases.
[Allure](https://allurereport.org/docs/pytest/) - To generate reports
[Selenium](https://www.selenium.dev/documentation/) - To interact with the UI
[xray](https://www.getxray.app/blog/xray-test-management-for-jira) - To generate reports on jira
[Jira](https://rrrenjifo.atlassian.net/jira/software/c/projects/FR/boards/7) - to manage tkts.
