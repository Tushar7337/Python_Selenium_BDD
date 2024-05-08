Feature: Dashboard of the application

  Scenario: After login verify dashboard of the application
    Given Launch Chrome Browser
    When Open Login Screen
    And Enter username "admin@blueskytelepsychiatry.com" and password "Bluesky@123"
    And Click on Login Button
    Then Verify Dashboard of the application

  @blue
  Scenario Outline: After login verify dashboard of the application
    Given Launch Chrome Browser
    When Open Login Screen
    And Enter username "<username>" and password "<password>"
    And Click on Login Button
    Then Verify Dashboard of the application

    Examples:
      | username                                | password |
      | admin@blueskytelepsychiatry.com         | Bluesky@123 |
      | tushar.bhadane+frontdesk@thinkitive.com | Bluesky@123 |
      | billergates@mailinator.com              | Bluesky@123 |