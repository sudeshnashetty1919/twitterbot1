Feature: Testing tagging and posting post
  Background:
    Given user is on login page
    When user enters sudeshnashetty2211@gmail.com and clicks on next
    When user enter @SSudesshna66398 and clicks on next
    When user puts 987654Suddu@
    When user clicks on login


  Scenario Outline: Check login with valid credentials
    When user types note <account> to tag
    When user clicks on post to tag
    Then user should get a toast <message> after tagging
    Then user clicks on logout after tagging

    Examples:
       | account   |message            |
       | @gari_setti61193 |Your post was sent.|
