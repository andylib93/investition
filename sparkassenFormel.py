#!/usr/bin/python3

# setze die Variablen
ZINS = 0.08
RATE = 6000
JAHRE = 35

# nachschüssig
def sparkassenFormelN(r, z, j):
    return r * ( ((z + 1)**j - 1) / z )

# vorschüssig
def sparkassenFormelV(r, z, j):
    return r * (z + 1) * ( ((z + 1)**j - 1) / z )

print(f'Rate: {RATE}, Zins: {ZINS}, Jahre: {JAHRE}, nachschüssig:')
print(sparkassenFormelN(RATE, ZINS, JAHRE))

print(f'Rate: {RATE}, Zins: {ZINS}, Jahre: {JAHRE}, vorschüssig:')
print(sparkassenFormelV(RATE, ZINS, JAHRE))
