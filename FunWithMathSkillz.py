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


for sides in range(350, 900, 350):
    print(sides, archimedes(sides))

print(math.pi)
# See the loop above.  in addition to the value of pi, print the difference
#  between the values calculated by the archimedes function and by math.pi.
#  How many sides does it take to make the two close?
