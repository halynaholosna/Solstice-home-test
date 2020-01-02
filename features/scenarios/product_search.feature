# Created by golos at 1/1/2020
Feature: Test for Amazon Search functionality

  Scenario: User can search and add to card items
    Given Open Amazon page
    When Search for Alexa
    And Navigate to the second page
    And Click on the third item
    Then Verify Add to card button is clickable