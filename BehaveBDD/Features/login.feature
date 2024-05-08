Feature: Login Functionality

  @login
  Scenario Outline: Login with valid Creds
    Given I Launch the Browser and Navigate to Login Page
    When I enter valid email as "<email>" and valid password as "<password>"
    And I click Login Button
    Then I should get Logged In
    Examples:
      |email                |password          |
      |cucu@gmail.com       |Pass@1234         |

  @login
  Scenario: Login with invalid email and valid password
    Given I Launch the Browser and Navigate to Login Page
    When I enter invalid email and valid password as "Pass@1234"
    And I click Login Button
    Then I should get proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I Launch the Browser and Navigate to Login Page
    When I enter valid email as "cucu@gmail.com" and invalid as "Pass@1234567"
    And I click Login Button
    Then I should get proper warning message

  @login
  Scenario: Login with invalid email and invalid password
    Given I Launch the Browser and Navigate to Login Page
    When I enter invalid email and invalid password
    And I click Login Button
    Then I should get proper warning message

  @login
  Scenario: Login without email and password
    Given I Launch the Browser and Navigate to Login Page
    When I dont enter any email and password
    And I click Login Button
    Then I should get proper warning message
