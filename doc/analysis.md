# Analysis

The major value of FinClerk is helping users analyze earnings.

Buying or selling shares do not have effect on earning, price fluctuation does. Given a period, the earning should be the difference between the total value (including that has been sold) at period end and the total value at period beginning with buying total in this period excluded: ```E = Vend - Vstart - B```, where *E* stands for earning, *V* stands for total value, *B* stands for buying total.

Buying total in a period is the sum of every buying: ```Btotal = ∑(Pi * Qi)```, where *P* stands for price, *Q* stands for quantity.

For a given time, the total value should be the product of current price and share adding previous selling total, since selling could be regarded as locking the price of some share: ```V = Pcurrent * (∑Qbuy - ∑Qsell) + ∑(Pi * Qi)```, where *Pi* and *Qi* are prices and quantities of selling.
