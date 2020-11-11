#!/usr/bin/python3

# ZINSESZINS -> nachschüssige Zinsen
# Endkapital = Anfangskapital * Zinsfaktor( q = 1 + i ) ** n

ANFANGSKAPITAL = 800
ENDKAPITAL = 1000
JAHRE = 5
ZINS = 0.05
ZINSFAKTOR = ZINS + 1

# welches Endkapital?
def zinsesZins(a, z, j):
    return a * z ** j

# wie hoch muss Anfangskapital sein?
def getAnfangskapital(e, z, j):
    return e / ( z ** j )

# mit welchem Zins?
def getZinssatz(e, a, j):
    return ( e / a ) ** (1/j) - 1

# für wie viele Jahre?
# ln wird gebraucht .. lol

print(f'{ANFANGSKAPITAL} Anfangskapital, {ZINS} Zins, {JAHRE} Jahre:')
print( zinsesZins(ANFANGSKAPITAL, ZINSFAKTOR, JAHRE) )

print(f'{ENDKAPITAL} Endkapital, {ZINS} Zins, {JAHRE} Jahre:')
print( getAnfangskapital(ANFANGSKAPITAL, ZINSFAKTOR, JAHRE) )

print(f'{ENDKAPITAL} Endkapital, {ANFANGSKAPITAL} Anfangskapital, {JAHRE} Jahre:')
print( getZinssatz(ENDKAPITAL, ANFANGSKAPITAL, JAHRE) )
