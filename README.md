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

**Python:** Download and install the latest version of Python. Python can not be downloaded through the command prompt itself, yet installation can be verified through the command prompt:  
[https://www.python.org]

## 3. Install Behave

3. Install Behave in command prompt.  
   `pip install behave`

4. Verify Behave installation and/or version in command prompt.  
   `behave --version`

## 4. Behave Tutorial

1. After successfully installing behave, create a directory called "features". In that directory create a file called "tutorial.feature" containing: 

    **Feature**: Login Functionality  
        **Scenario**: Successful Login  
        **Given** the user is on the login page  
        **When** they enter valid credentials  
        **Then** they should be redirected to the home page  


