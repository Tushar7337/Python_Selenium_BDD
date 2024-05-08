Feature: Login TRST admin application

  @trst
  Scenario: Login into the TRST-admin with valid username and password
    Given Launch the web URL and navigate to Login screen
    When Enter username as "super_admin" and password as "Super1@trst"
    And Click Sign In Button
    Then Dashboard should display