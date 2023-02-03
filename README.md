# UI Homework Assignment Project

An Automation Web Framework based on Python, Behave, Selenium and Allure Report.

## Getting Started

### Prerequisites

> #### Python
> - Install last version of Python and Pip.
> - Check successfully installation whit ``python --version`` command.

> #### Python Virtual Env
> - Create a new python venv with ``python -m venv .venv``.
> - After that, you will have a new folder ``.venv`` in the root project.
> - Activate venv with `` $ source .venv/bin/activate `` command.
> - You can check in your console if it was activated successfully.

> #### Allure
> - Install Allure following the next steps https://docs.qameta.io/allure/#_get_started
> - Check the installation with ``allure --version``.

### Installing

> #### Python Libs
> - You need install project module/libs from *requirements.txt* file.
> - `pip install -r requirements.txt`.

## Running tests
> You can run your test with the following command:
> - `behave` to execute all tests cases folder.
> - `behave  -f allure_behave.formatter:AllureFormatter -o ./allure-report` to execute tests and generate Allure report.
> - `behave features/users.feature:3 -f allure_behave.formatter:AllureFormatter -o ./allure-report` to execute a specific scenario/example.

## Report
> You can get the Allure report with these commands:  
> `allure serve ./report_folder/` to see the current report.
