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
for val in range(1, 6):
    acc = acc + val

print(acc)

acc2 = 0
for val2 in range(0, 100, 2):
    acc2 = acc2 + val2
print(val2)


# A Monto Carlo Simulation

# random numbers

import random

print(random.random())

# Boolean Expressions
# <, <+, >, >=, ==, !=
# Compound Boolean Expressions
# and, or, not

dogweight = 25
print(dogweight == 25)
catweight = 12
print(dogweight >= 25 or catweight == 10)
print(not catweight >= 10)

# decision making skills

alice = 20
bob = 15
carol = 25
ans = 0
if alice == 20:
    ans = 300
    if bob < 50:
        ans = 150
    else:
        ans = 999
else:
    ans = 200
print(ans)

value = 75
if value > 10:
    print("bigger than 10")
elif value > 20:
    print("bigger than 20")
elif value > 45:
    print("bigger than 45")
else:
    print("not bigger than much")


def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        if distance <= 1:
            inCircle = inCircle + 1
    pi = inCircle / numDarts * 4
    return pi


print(montePi(10000))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)
    t.penup()

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)
        if distance <= 1:
            inCircle = inCircle + 1
            t.color("green")
        else:
            t.color("red")

        t.dot()
    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi
