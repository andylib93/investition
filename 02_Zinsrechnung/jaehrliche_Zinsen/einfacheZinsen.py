#!/usr/bin/python3

# EINFACHE JÄHRLICHE VERZINSUNG -> nachschüssige Zinsen
# Endkapital = Anfangskapital * ( 1 + n * i )

ANFANGSKAPITAL = 8000
ENDKAPITAL = 10000
JAHRE = 5
ZINS = 0.04

# welches Endkapital?
def einfacheVerzinsung(a, j, z):
    return a * ( 1 + j * z )

# wie hoch muss Anfangskapital sein?
def getAngangskapital(e, j, z):
    return e / ( 1 + j * z )

# mit welchem Zins?
def getZinssatz(e, a, j):
    return (1 / j) / ( ( e / a ) - 1 )

# für wie viele Jahre?
def getJahre(z, e, a):
    return (1 / z) * ( ( e / a ) - 1 )

print(f'{ANFANGSKAPITAL} Anfangskapital, {JAHRE} Jahre, {ZINS} Zins:')
print( einfacheVerzinsung(ANFANGSKAPITAL, JAHRE, ZINS) )

print(f'{ENDKAPITAL} Endkapital, {JAHRE} Jahre, {ZINS} Zins:')
print( getAngangskapital(ENDKAPITAL, JAHRE, ZINS) )

print(f'{ENDKAPITAL} Endkapital, {ANFANGSKAPITAL} Anfangskapital, {JAHRE} Jahre:')
print( getZinssatz(ENDKAPITAL, ANFANGSKAPITAL, JAHRE) )

print(f'{ZINS} Zins, {ENDKAPITAL} Endkapital, {ANFANGSKAPITAL} Anfangskapital:')
print( getJahre(ZINS, ENDKAPITAL, ANFANGSKAPITAL) )
