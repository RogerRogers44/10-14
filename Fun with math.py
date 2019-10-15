# Approximations of pi
print(22/7)
print(455/113)

import math
print(9801/ (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))
#for sides in range(800, 1000000000, 800):
    #print(sides, archimedes(sides))
print(math.pi)
#  I made 1 billion sides and it's pretty close
# print(math.pi - archimedes(1000000000))

#  Accumulators

acc = 0
# adds 1 to val every time it runs so it'll be 1, 2, 3...
# it keeps doing that until it has done it 6 times
# whatever you get for acc last time, you plug that in for acc the next time
for val in range(1, 100):
    acc = acc + val

print(acc)


