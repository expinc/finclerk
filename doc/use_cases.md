# Use cases

This document illustrates the use cases of FinClerk. Only normal use cases are illustrated here. No abnormal use case. Since there is only one kind of actor possible: users (account owners), the actors of the use cases are eliminated.

- [Authentication](#authentication)
- [Journal](#journal)
- [Analysis](#analysis)

## Authentication

Use case: Register account
- Context: User has not logged in with existing account yet.
- Actions:
    1. User submits *account name*, *password*, *confirmed password*.
- Expected result:
    1. The account is created.
    1. User is logged in with the created account.

Use case: Login
- Context: User has not logged in with existing account yet.
- Actions:
    1. User submits *account name*, *password*.
- Expected result:
    1. User is logged in.
    1. Products added in the account are listed.

Use case: Logout
- Context: User has logged in with existing account.
- Actions:
    1. User choose to logout.
- Expected result:
    1. User is logged out.
    1. Goes to login page.

## Journal

Use case: Add a product
- Context:
    1. User has logged in with existing account.
    1. The product has not been added yet.
- Actions:
    1. User submits *product code*, *product name*, *product type*.
- Expected result:
    1. The product is added.

Use case: Record a trade
- Context:
    1. User has logged in with existing account.
    1. The product has been added.
- Actions:
    1. User chooses a product to record a trade.
    1. User submits *trade type* (buy or sell), *price*, *quantity*.
- Expected result:
    1. A trade is recorded.

Use case: View trades of a product
- Context:
    1. User has logged in with existing account.
    1. The product has been added.
- Actions:
    1. User chooses a *product* to view trades.
- Expected result:
    1. All trades of the product are listed.

Use case: Amend a trade
- Context:
    1. User has logged in with existing account.
    1. The product has been added.
    1. User has gone to the list of product trades.
    1. There are some trades in the list.
- Actions:
    1. User chooses a *trade* to amend.
    1. User submits new *trade type* (buy or sell), *price*, *quantity*.
- Expected result:
    1. The trade is amended.
    1. The amended trade is displayed in the trade list.

Use case: Delete a trade
- Context:
    1. User has logged in with existing account.
    1. The product has been added.
    1. User has gone to the list of product trades.
    1. There are some trades in the list.
- Actions:
    1. User chooses a *trade* to delete.
    1. User confirms to delete the trade.
- Expected result:
    1. The trade is deleted.
    1. The amended trade disappears in the trade list.

## Analysis

Use case: Analyze earning of a product
- Context:
    1. User has logged in with existing account.
    1. The product has been added.
- Actions:
    1. User chooses a *product* to analyze earning.
    1. User submits the *time period* for analysis.
- Expected result:
    1. The earning quantity in the time period is displayed.
