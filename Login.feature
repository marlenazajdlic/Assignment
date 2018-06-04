
Feature: Login feature
  As a user I would like to check login functionality into mailbox with valid and invalid credentials

  Scenario: Login with valid credentials
    Given the homepage is loaded
    When I hover the mouse over widget in the top-right corner
    Then login form is visible
    When I fill username with 'testautomation2018'
    And I fill password with 'testautomation2018'
    And I click Zaloguj się button
    Then I am redirected to my mailbox

  Scenario: Login with invalid credentials
    Given the homepage is loaded
    When I hover the mouse over widget in the top-right corner
    Then login form is visible
    When I fill username with 'testautomation2018v'
    And I fill password with 'testautomation2018'
    And I click Zaloguj się button
    Then I am redirected to the login page with message about wrong credentials

  Scenario: Login without credentials
    Given the homepage is loaded
    When I hover the mouse over widget in the top-right corner
    Then login form is visible
    When I click Zaloguj się button
    Then I am redirected to the login page with message about wrong credentials