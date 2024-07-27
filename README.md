
# ParaBank Automated Test Project

This project contains automated tests for the ParaBank website. The tests are implemented using Python, Selenium, and PyTest. Dependency management is handled with Poetry.

## Project Structure

- `tests/`: Directory containing test cases.
- `pages/`: Directory containing page object models.
- `utils/`: Directory containing utility functions.
- `pytest.ini`: Configuration file for PyTest.
- `pyproject.toml`: Configuration file for Poetry.

## Prerequisites

- Python 3.8+
- Poetry for dependency management
- Google Chrome and ChromeDriver

## Setup Instructions

1. **Clone the repository:**
   bash
   
   git clone https://github.com/foramnayak92/parabank-tests.git
   cd parabank-tests
   
Install dependencies:

Ensure you have Poetry installed. If not, you can install it using the following command:

bash
curl -sSL https://install.python-poetry.org | python3 -

bash
poetry install
Activate the virtual environment:

bash

poetry shell
Run the tests:

bash

pytest --browser chrome --headless

Test Scenarios
The project includes the following test scenarios:

User Registration: Verifies that a user can successfully register on the ParaBank website.
User Login: Verifies that a registered user can log in.
Account Overview: Verifies that the user can view the account overview after logging in.
Fund Transfer: Verifies that the user can transfer funds between accounts.
Bill Payment: Verifies that the user can pay bills using the available funds.
Project Implementation

1. Project Proposal
The project proposal includes the selection of test scenarios and the design of test cases for the ParaBank website.

2. Automated Test Cases
The test cases were automated using Selenium for browser interactions and PyTest for test execution and reporting.

3. XML Report
An XML report is generated for the test execution, which provides a detailed summary of the test results.

Difficulties Faced
During the automation of test cases, several challenges were encountered, including:

Element Identification: Locating dynamic elements on the web pages.
Synchronization Issues: Handling loading times and ensuring elements are available for interaction.
Test Data Management: Managing test data for various test scenarios.
Conclusion
This project demonstrates the process of automating web application tests using Selenium and PyTest, with a focus on robust test design and effective error handling.

Future Work
Potential future enhancements for this project include:

Adding more test scenarios to cover additional functionalities of the ParaBank website.
Implementing parallel test execution to reduce test execution time.
Integrating the test suite with CI/CD pipelines for automated test execution.

Author
Foram Nayak

License
This project is licensed under the MIT License - see the LICENSE file for details.






