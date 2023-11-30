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

   Create a virtual environment  
   `python -m venv venv`

   Activate the virtual environment (Windows)  
   `venv\Scripts\activate`

   Activate the virtual environment (Unix or MacOS)  
   `source venv/bin/activate`

   Install dependencies  
   `pip install -r requirements.txt`


## 5. Running Tests with Virtual Enviroment  
   Once virtual environment is set up, you can run Behave tests and have results generated to a json file with the following command:
   `behave --format json -o test_report.json`

   If you're using the Windows terminal and want to format the generated JSON file for better readability, you can use the following command:
   `behave --format json -o test_report.json ; (Get-Content test_report.json | ConvertFrom-Json | ConvertTo-Json) | Set-Content -Path test_report.json`
   This command not only runs the Behave tests and generates the JSON report but also formats the JSON file to be indented, making it easier to read.

      

## 5. Behave Tutorial
   1. After successfully installing behave, create a directory called "features". In that directory create a file called "tutorial.feature" using Gherkin syntax containing:

    **Feature**: Login Functionality  
        **Scenario**: Successful Login  
        **Given** the user is on the login page  
        **When** they enter valid credentials  
        **Then** they should be redirected to the home page  


