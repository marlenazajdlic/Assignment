Feature: Quiz feature
  As O2 user I would like to open quiz
  Scenario: Access to the quiz
    Given the homepage is loaded
    When I hover the mouse over widget in the bottom-right corner
    Then button "Graj teraz!" is visible
    When I click Graj teraz! button
    Then Quiz page available
