#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  for i in recipe:
    for j in ingredients:
      if i == j:
        amount = math.floor(j.value / i.value)
        if amount < 1:
          return 0
        return amount
  return min(amount)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))