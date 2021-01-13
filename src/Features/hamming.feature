Feature: Hamming

  Scenario: Empty strands
    Given create class Hamming and run distance method
    When running with two empty strands
    Then return 0 distance value

  Scenario: Strands with identical single letter
    Given create class Hamming and run distance method
    When running with strands with identical single letter
    Then return 0 distance value

  Scenario: Strands with different single letter
    Given create class Hamming and run distance method
    When running with strands with different single letter
    Then return 1 distance value

  Scenario: Long identical strands
    Given create class Hamming and run distance method
    When running with two long identical strands where distance is 0
    Then return 0 distance value

  Scenario: Long different strands
    Given create class Hamming and run distance method
    When running with two long different strands where distance is 9
    Then return 9 distance value

  Scenario: First strand is longer than the second
    Given create class Hamming and run distance method
    When running with first strand longer than the second
    Then get error

  Scenario: Second strand is longer than the first
    Given create class Hamming and run distance method
    When running with second strand longer than the first
    Then get error

  Scenario: First strand is empty
    Given create class Hamming and run distance method
    When running with empty first strand
    Then get error

  Scenario: Second strand is empty
    Given create class Hamming and run distance method
    When running with empty second strand
    Then get error