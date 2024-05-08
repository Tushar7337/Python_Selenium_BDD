Feature: Search Functionality

  @search
  Scenario: Search For Valid Product
    Given I Launch the URL and navigated to Home Page
    When I entered valid product say "HP" in search box field
    And I clicked on search Button
    Then Valid Product should get displayed in search result

  @search
  Scenario: Search for Invalid Product
    Given I Launch the URL and navigated to Home Page
    When I entered invalid product say "Honda" in search box field
    And I clicked on search Button
    Then Proper message should be display in search result

  @search
  Scenario: Search for Invalid Product
    Given I Launch the URL and navigated to Home Page
    When I not entered anything in search box field
    And I clicked on search Button
    Then Proper message should be display in search result
