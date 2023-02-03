Feature: Users

  Scenario Outline: Create new user
     Given a users table
      When we create a new user <first_name>, <last_name>, <user_name>, <password>, <customer>, <role>, <email>, <phone>
      Then user <user_name> was created successfully

    Examples:
      | first_name | last_name | user_name  | password | customer    | role  | email   | phone |
      | lucas      | monsierra | lmonsierra | lucas    | Company AAA | Admin | l@m.com | 12345 |

    Scenario Outline: Delete user
     Given a users table
      When we delete user <user_name>
      Then user <user_name> was deleted successfully

    Examples:
      | user_name |
      | novak     |