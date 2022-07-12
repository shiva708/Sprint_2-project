Feature: searching the hotel

  Scenario: search a hotel by user inputs
    Given user launch the trivago broswer
    And user should select on hotels
    When User click on search location bar and enter the location as "hyderabad"
    And give the checkin and checkout dates
    And select the No of adults and childs and apply
    Then user search the hotels and it will display




