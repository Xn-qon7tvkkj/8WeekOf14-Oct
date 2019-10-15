# We are going to look at approximations of Pi
# as well as looking at the math Module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
# 3.0614674589207183
print(archimedes(8))
# 3.121445152258052
print(archimedes(16))
# 3.141592653589793


for sides in range(750, 900, 750):
    print(sides, archimedes(sides))

print(math.pi)
# See the loop above.  in addition to the value of pi, print the difference
#  between the values calculated by the archimedes function and by math.pi.
#  How many sides does it take to make the two close?


# Accumulators

acc = 0
for val in range(1, 6, 1):
    acc = acc + val

print(acc)


# Compute the sum of the first 100 even numbers
acc = 0
for val in range(0, 100, 2):
    acc = acc + val

print(acc)
# Each even numbers accumulate to 100 and added to the val, equalling to 2450.

# Compute the sum of the first 50 odd numbers
acc = 0
for val in range(1, 50, 2):
    acc = acc + val

print(acc)
# Each odd numbers accumulate to 50 and added to the val, equalling to 625.

# Compute the average of the first 100 odd numbers
acc = 0
for val in range(1, 100, 2):
    acc = acc + val
    acc = (acc + val / 100)
print(acc)
# Each odd numbers accumulate up to 100 and added to the val, equalling to 46.

# Write a function that returns the average of the first N numbers, where
#   N is a parameter

# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter


# Each number in the Fibonacci sequence is the sum of previous two number
#   The first two numbers in the sequence are 1 and 1. Compute the 10th
#    Fibonacci number
acc = 1
for val in range(1, 10):
    acc = acc + val

print(acc)
# The 10th Fibonacci number is 46 because the first two numbers are a sum, which the sum is added with the val.

# Write a function to compute the Nth Fibonacci number, where N is a parameter
#   You may assume that N will be greater than or equal to 3.
