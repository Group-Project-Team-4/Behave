# Behave

## 1. Introduction

**1.1. Purpose:** This repository contains an Behavior-Driven Development (BDD) testing application designed to facilitate automated testing with a focus on behavior specifications. BDD allows for collaboration between developers, QA, and non-technical stakeholders by using human-readable descriptions of software behaviors.

**1.2. Definitions and Acronyms:**
+ **BDD**: Behavior Driven Development
+ **Gherkin**: Language used for writing tests in BDD
+ **Behave**: A BDD tool for python

## 2. System Overview

**2.1 Tools & Technologies**
+ Behave
+ Python
+ Selenium (for web application testing in some scenarios)
+ ChromeDriver
+ Supported browsers: Firefox, Chrome, Safari, & Edge

**Python:** Download and install the latest version of Python. Python can not be downloaded through the command prompt itself, yet installation can be verified through the command prompt:  
[https://www.python.org]

**Google Chrome**: Default browser that is being used with Selenium. Make sure the latest version is installed.  
[Download here](https://googlechromelabs.github.io/chrome-for-testing/#stable)

## 3. Install Behave

3. Install Behave in command prompt.  
   `pip install behave`

4. Verify Behave installation and/or version in command prompt.  
   `behave --version`

## 4. Prerequisites
   Before running the Behave tests, make sure to set up a virtual environment and install the required dependencies. You can use the following commands:

   1. Create a virtual environment  
   `python -m venv venv`

   2. Activate the virtual environment (Windows)  
   `venv\Scripts\activate`

   3. Activate the virtual environment (Unix or MacOS)  
   `source venv/bin/activate`

   4. Install dependencies  
   `pip install -r requirements.txt`


## 5. Running Tests with Virtual Enviroment  
   Once virtual environment is set up, you can run Behave tests and have results generated to a json file with the following command:  
   `behave --format json -o test_report.json`

   If you're using the Windows terminal and want to format the generated JSON file for better readability, you can use the following command:  
   `behave --format json -o test_report.json ; (Get-Content test_report.json | ConvertFrom-Json | ConvertTo-Json) | Set-Content -Path test_report.json`  
   This command not only runs the Behave tests and generates the JSON report but also formats the JSON file to be indented, making it easier to read.

      

## 5. Behave Tutorial

   1. After successfully installing behave, there is a directory called "features". In that directory there is a file called "login.feature" containing:

   **Feature**: Login functionality on the clothing store app  

   **Scenario**: User can login  
      **Given**: User is on the shop page  
      **When**: User clicks login  
      **When**: User enters login credentials  
      **When**: User logs in  
      **Then**: the test should pass  

   2. There is a directory called "features.steps" which contains login.py

   ```
   from behave import *

      @when('User clicks login')
   def step_impl(context):
      login_link = context.driver.find_element(By.ID, "base_login_anchor")
      login_link.click()
      time.sleep(0.25)
      assert context.driver.current_url == 'http://localhost:5000/auth/login'
      context.driver.save_screenshot("./login/login_page.png")


   @when('User enters login credentials')
   def step_impl(context):
      username_input = context.driver.find_element(By.ID, "login_username_textinput")
      username_input.send_keys(USERNAME)
      time.sleep(0.25)
      assert username_input.get_attribute('value') == 'nate123'
      password_input = context.driver.find_element(By.ID, "login_password_textinput")
      password_input.send_keys(PASSWORD)
      time.sleep(0.25)
      assert password_input.get_attribute('value') == '12345'
      context.driver.save_screenshot("./login/login_credentials.png")


   @when('User logs in')
   def step_impl(context):
      login_button = context.driver.find_element(By.ID, "login_submit_button")
      login_button.click()
      time.sleep(0.25)
      assert context.driver.current_url == 'http://localhost:5000/'
      context.driver.save_screenshot("./login/login_success.png")
   ```

   3. Run behave  
   ```
   % behave
   Feature: showing off behave 

   Scenario: User can login  # features/login.feature:1
      Given: User is on the shop page # features/login.feature:1
      When: User clicks login   # features/login.feature:1
      When: User enters login credentials  # features/login.feature:1
      When: User logs in  # features/login.feature:1
      Then: the test should pass  # features/login.feature:1
   ```







