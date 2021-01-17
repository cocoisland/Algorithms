import sys

# def making_change(amount, denominations):
#   if amount == 0:
#     return 1
#   if amount < 0:
#     return 0
#   if len(denominations) <= 0 and amount > 0:
#     return 0
#   else:
#     return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])

'''
Dynamic programming - breaking problem into subsolution and use these subsolutions to solve original problem.
Eg To find out how many coins to change X amount, first find out how many small denominations needed for each
  incremental amount leading to the final amount.
  Amount = 6, denomination=[1,2,5]
  eg Amount[2]xdenomination[2]=2 means 2 ways to change for amount 2 -> 1+1, 2+0
     Amount[4]xdenomination[2]=3 means 3 ways to change for amount 4 -> 1+1+1+1, 2+2, 2+1+1
      - For denomination 2, Amount[4]= Amount[2] + denomination 2 => 2 + 1 = 3
                            Amount[2] = 2 in denomination 2 category/loop
     Amount[6]xdenomination[2]=4 means 4 ways to change for amount 6 -> 1x6, 2x3,2+1+1+1, 2+2+1+1+1+1
    Amount 
 0  1  2  3  4  5  6
  coin 1 denomination
[1, 1, 0, 0, 0, 0, 0]
[1, 1, 1, 0, 0, 0, 0]
[1, 1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 1, 0, 0](6+1)-1 = 6 rows represent number of ways to make changes for that particular column amount.
[1, 1, 1, 1, 1, 1, 0]
[1, 1, 1, 1, 1, 1, 1]
 coin 2 denomination
[1, 1, 2, 1, 1, 1, 1]
[1, 1, 2, 2, 1, 1, 1]
[1, 1, 2, 2, 3, 1, 1] (6+1)-2 = 5 rows
[1, 1, 2, 2, 3, 3, 1]
[1, 1, 2, 2, 3, 3, 4]
 coin 5 denominations
[1, 1, 2, 2, 3, 4, 4] (6+1)-5 = 2 rows
[1, 1, 2, 2, 3, 4, 5] 
ways= 5

  

'''
def making_change(amount, denominations):
  ways = [0] * (amount + 1)
  ways[0] = 1

  for coin in denominations:
    for higher_amount in range(coin, amount + 1):
      remainder = higher_amount - coin
      ways[higher_amount] += ways[remainder]

  return ways[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
