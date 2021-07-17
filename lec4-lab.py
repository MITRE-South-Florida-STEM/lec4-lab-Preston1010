def dice_probability(die_1, die_2):
    '''
    die_1 and die_2 are both assumed to be non-negative integers
    '''
    if die_2 > 6 or die_2 < 1 or die_1 > 6 or die_1 < 1:
        print("Both dice need to be between 1 and 6!")
        return None

    s = die_1 + die_2

    if die_1 == 1 and die_2 == 1:
      print("Snake eyes!")
      print(round(1/36, 3))
      return round(1/36, 3)
    elif s <= 7:
      print(round((s - 1)/36, 3))
      return round((s - 1)/36, 3)
    else:
      print(round((12 - s + 1)/36, 3))
      return round((12 - s + 1)/36, 3)
    ...

#dice_probability(0, 2)
# Expected output:
# "Both dice need to be between 1 and 6!"

dice_probability(3, 4)
# Expected output:
# 0.194

#dice_probability (1, 1)
# Expected output:
# 0.028
# "Snake eyes!"

# Write a function that takes two functions, a low float and a high float. Print out which function is larger each time
#  you increase the input value by 1 starting at the low float and ending before you exceed the high float.

import math

def larger_function(f1, f2, low, high):
    '''
    f1 and f2 are functions that return floats
    low and high are floats that represent the range of input values into f1 and f2
    '''
    x = low
    while x < high:
      if f1(x) == f(x):
        print("Equal")
      elif f1(x) > f2(x):
        print("f1 is greater")
      else:
        print("f2 is greater")
      x += 1

# define f1 as the sine function with amplitude 2
def f1(x):
  return (math.sine(x) * 2)

# define f2 as the cosine function with shift 3
def f2(x):
  return (math.cos(x - 3)) # negate because the shift is positive

# call your function with low = 0 and high = 4pi
larger_function(f1, f2, 0, 4*math.pi())