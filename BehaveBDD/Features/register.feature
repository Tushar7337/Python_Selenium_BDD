Feature: Register Account Functionality

  @register @time
  Scenario: Register with mandatory fields
    Given I launch the URL and navigate to Register Page
    When I enter below details mandatory field
         |first_name|last_name|password |
         |Raw       |BDD      |Pass@1234|
    And I click on Continue Button
    Then Account Should get created

  @register @time
  Scenario: Register with all fields
    Given I launch the URL and navigate to Register Page
    When I enter all the below field
         |first_name|last_name|password |
         |raw       |BDD      |Pass@1234|
    And I click on Continue Button
    Then Account Should get created

  @register
  Scenario: Register with duplicate email address
    Given I launch the URL and navigate to Register Page
    When I enter existing email in email textfield
        |first_name|last_name|password |
        |Raw       |BDD      |Pass@1234|
    And I click on Continue Button
    Then Proper error message about duplicate email should be display

  @register
  Scenario: Register without entered any details
    Given I launch the URL and navigate to Register Page
    When I dont enter any details
    And I click on Continue Button
    Then Proper error message about mandatory fields should be display