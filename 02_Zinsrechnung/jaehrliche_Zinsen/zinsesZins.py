#!/usr/bin/python3

# ZINSESZINS -> nachschüssige Zinsen
# Endkapital = Anfangskapital * Zinsfaktor( q = 1 + i ) ** n

ANFANGSKAPITAL = 10000
ENDKAPITAL = 10000
JAHRE = 5
ZINS = 0.04
ZINSFAKTOR = ZINS + 1

# welches Endkapital?
def zinsesZins(a, z, j):
    return a * z ** j

print(f'{ANFANGSKAPITAL} Anfangskapital, {JAHRE} Jahre, {ZINS} Zins:')
print( zinsesZins(ANFANGSKAPITAL, ZINSFAKTOR, JAHRE) )
