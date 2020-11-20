#!/usr/bin/python3

# setze die Variablen
ZINS = 0.08
RATE = 6000
JAHRE = 35

def sparkassenFormel(r, z, j):
    return r * ( ((z + 1)**j - 1) / z )

print(f'Rate: {RATE}, Zins: {ZINS}, Jahre: {JAHRE}:')
print(sparkassenFormel(RATE, ZINS, JAHRE))
