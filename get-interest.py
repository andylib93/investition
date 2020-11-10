#!/usr/bin/python3

# RENTEN-RECHNUNG

'''
Ausgangssituation:
> Heute 10.000 oder in 10 Jahren 15.000?

15.000 = 10.000 * ( 1 + i ) ** 10

i = ( 15.000 / 10.000 ) ** ( 1/10 ) - 1

'''

BARWERT = 20000
ENDWERT = 15000
JAHRE = 50
ZINS = 0.02

def getInterest(e, b, j):
	return ( e / b ) ** ( 1 / j ) - 1

print( getInterest(ENDWERT, BARWERT, JAHRE) )

def getAccumulatedValue(b, z, j):
	q = 1 + z
	return b * ( ( z * ( q ** j )) / (( q ** j ) - 1) )

print( getAccumulatedValue(BARWERT, ZINS, JAHRE) )
