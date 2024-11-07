Feature: Test Login
  @skip
  Scenario Outline: Verify the login of the user
    Given user is on login page
    When user enters <user name> and clicks on next
    When user enter <phone NO or User Name> and clicks on next
    When user puts <password>
    When user clicks on login


  Examples:
    | user name                    | phone NO or User Name | password     |
    | sudeshna1995shetty@gmail.com | @gari_setti61193      | 987654Suddu@ |