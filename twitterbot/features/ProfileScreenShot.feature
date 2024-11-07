Feature: Test login functionality
Background:
    Given user is on login page
    When user enters sudeshna1995shetty@gmail.com and clicks on next
    When user enter @gari_setti61193 and clicks on next
    When user puts 987654Suddu@
    When user clicks on login

  Scenario Outline: Check login with valid credentials
    When user clicks on notifications and opens the account
    When user takes a screenshot
    When click back
    When clicks on reply
    When posts the screenshot
    Then user should get a toast <message>
    Then close the popup if opened
    Then user clicks on logout

  Examples:
    | message             |
    | Your post was sent. |
