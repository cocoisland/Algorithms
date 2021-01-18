#!/usr/bin/python
'''
Plan:
find the smallest number of recipe that can fit in available ingredients.
return 0 if no ingredients.
'''
import math

def recipe_batches(recipe, ingredients):
  maxBatch = 0
  batchCount = 0

  for k in recipe.keys():
    if k in ingredients:
      batchCount = recipe[k] // ingredients[k]
      
      if batchCount > maxBatch:
        maxBatch = batchCount
    else:
      return 0
  

  return maxBatch

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  ingredients = { 'milk': 100, 'butter': 50, 'flour': 5 }
  recipe = { 'milk': 132, 'butter': 48, 'flour': 51 }
  maxBatch=recipe_batches(recipe, ingredients)
  print(f'{maxBatch} batches can be made from the available ingredients: {ingredients}')
