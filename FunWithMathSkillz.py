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
for val in range(1, 201, 2):
    acc = acc + val

print(acc / 100)
# Each odd numbers accumulate up to 100 and added to the val, equalling to 100.

# Write a function that returns the average of the first N numbers, where
#   N is a parameter
n = input("Type Number ")
n = int(n)
average = 0
acc = 0
for n in range(0, n+1, 1):
    acc = acc + n;
average = acc / n
print("Average of first", n, "number is: ", average)

# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
n = input("Type Number ")
n = int(n)
factorial = 0
acc = 0
for n in range(0, n+1, 1):
    acc = acc + n;
factorial = acc * n
print("Product of first N", n, "number is: ", factorial)

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

def Fibonacci(n):
    if n>=3:
        print("Incorrect input")
    # First Fibonacci number is 3
    elif n==3:
        return 3
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


# A Monte Carlo Simulation

# random numbers

import random

print(random.random())

# Boolean Expressions
# <, <=, >, >=, ==, !=
# Compound Boolean expressions
# and, or, not

dogWeight = 25
print(dogWeight < 25)   # ==, <=, >= is True. !=, <, > is false
catWeight = 12
print(dogWeight > 25 or catWeight <= 10)
print(not catWeight <= 10)

# Decision making skills

alice = 20
bob = 15
carol = 25
ans = 0
if alice > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if carol > 500:
        ans = 200
    else:
        ans = 75
print(ans)

value = 75
if value > 100:
    print("bigger than 100")
elif  value > 80:
    print("bigger than 80")
elif value > 45:
    print("bigger than 45")
else:
    print("not bigger than much")