Feature: Password

  Scenario: Empty string
    Given create class Password and run valid_password method
    When running with empty string
    Then return False

  Scenario: String with capital letter, digit, special char and with right length
    Given create class Password and run valid_password method
    When running with strings with all the requirements
    Then return True

  Scenario: String with invalid length
    Given create class Password and run valid_password method
    When running with string with invalid length
    Then return False

  Scenario: String without capital letter
    Given create class Password and run valid_password method
    When running with string without capital letter
    Then return False

  Scenario: String without digit
    Given create class Password and run valid_password method
    When running with string without digit
    Then return False

  Scenario: String without special char
    Given create class Password and run valid_password method
    When running with string without special char
    Then return False

  Scenario: Input is of type int
    Given create class Password and run valid_password method
    When running with input of type int
    Then get err

  Scenario: Input is of type object
    Given create class Password and run valid_password method
    When running with input of type object
    Then get err
