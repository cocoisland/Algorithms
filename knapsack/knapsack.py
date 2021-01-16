import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

"""
Brute-force knapsack checks every possible combination of items we could 
be taking and outputs the combination with the best value. 
1. Use recursion to exhaustively check every single combination of items
2. Base case 1: we have no items left in the pile to take
3. Base case 2: we have one item left in the pile. Check to see if it fits. If it does, take it, otherwise discard it.
4. On each recursive call we pick up the next item from the pile
5. Calculate the overall value we have in our knapsack if we don't take the item
6. Calculate the overall value we have in our knapsack if we do take the item
7. Compare the two calculated values; take the option that yields the greater value
"""

# def knapsack_solver(items, capacity):
#   # Recursively check all combinations of items with inner helper method
#   def knapsack_rec(items, capacity, value=0, bag=set()):
#     # No remaining items that fit
#     if not items:
#       return value, bag
#     elif items[0].size > capacity:
#         return knapsack_rec(items[1:], capacity, value, bag)
#     else:
#       # Recurse cases of taking item/not taking item, return max
#       bag_copy = bag.copy() # Copy to avoid marking everything taken
#       bag_copy.add(items[0].index)
#       # Calculate the value of taking this item
#       r1 = knapsack_rec(items[1:], capacity - items[0].size,
#                         value + items[0].value, bag_copy)
#       # Calculate the value of not taking this item
#       r2 = knapsack_rec(items[1:], capacity, value, bag)
#       # Choose the option with the larger value
#       return max(r1, r2, key=lambda tup: tup[0])
#   # Initial call with our bag represented as a Set data structure
#   answer = knapsack_rec(items, capacity)
#   return {'Value': answer[0], 'Chosen': sorted(list(answer[1]))}

"""
-----------------------------------------------------------------------------------------
knapsack_solver answer is wrong. Try the following data for max value return
val = [4,7,10] 
wt = [3,3,5] 
W =7
n = len(val) 
print(knapSack(W, wt, val, n)) 
  -> correct answer->val(4+7=11) for wt(3+3<7) 
  -> not correct answer -> val=10 for wt=5
-------------------------------------
This following program works.
# A naive recursive implementation of 0-1 Knapsack Problem 
  
# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(W, wt, val, n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
        else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1)) 
  
# end of function knapSack 
  
# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print knapSack(W, wt, val, n) 

------------------------------------------------------------------------------------
"""


# Memoized version of our brute-force solution
def knapsack_solver(items, capacity):
  cache = [[0] * (capacity + 1) for _ in range(len(items) + 1)]

  def knapsack_memoized_helper(index, capacity, value=0, bag=set()):
    answer = cache[index][capacity]
    if answer == 0:
      answer = knapsack_bf_helper(index, capacity, value, bag)
      cache[index][capacity] = answer
    return answer

  def knapsack_bf_helper(index, capacity, value=0, bag=set()):
    # No remaining items that fit
    if index == -1:
      return value, bag
    elif items[index].size > capacity:
        return knapsack_memoized_helper(index - 1, capacity, value, bag)
    else:
      # Recurse cases of taking item/not taking item, return max
      bag_copy = bag.copy() # Copy to avoid marking everything taken
      bag_copy.add(index)
      # Calculate the value of taking this item
      r1 = knapsack_memoized_helper(index - 1, capacity - items[index].size, value + items[index].value, bag_copy)
      # Calculate the value of not taking this item
      r2 = knapsack_memoized_helper(index - 1, capacity, value, bag)
      # Choose the option with the larger value
      return max(r1, r2, key=lambda tup: tup[0])
    
  answer = knapsack_bf_helper(len(items) - 1, capacity)
  return {'Value': answer[0], 'Chosen': sorted(list(answer[1]))}


"""
Incorrect but feasible and efficient solution for the knapsack problem. due to sorting weight by value
"""
# def knapsack_solver(items, capacity):
#   value = 0
#   weight = 0
#   bag = set() 
#   # Relax the problem by considering items in increasing order of weight by value
#   #norm_items = [Item(item.index, float(item.size) / item.value, item.value) for item in items]
#   sorted_items = sorted(items, key=lambda item: item.value)

#   # Greedy loop, if the item fits in the knapsack, take it
#   for item in sorted_items:
#     if weight + (item.size * item.value) <= capacity:
#       bag.add(item.index)
#       value += item.value
#       weight += (item.size * item.value)

#   return {'Value': value, 'Chosen': sorted(list(bag))}

"""
Correct if first sort by value, then fit as much as size as possible within weight capacity.
def knapsack_solver(items, capacity):
  rvalue = 0
  rweight = 0
  bag = set()
  sorted_value = sorted(items, key=lambda item: item.value)
  
  for item in sorted_value:
    if (weight + item.size) <= capacity :
      bag.add(item.index)
      value += item.value
      weight += item.size
      
   return{'Value': value, 'Chosen': sorted(list(bag)))}

"""

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
