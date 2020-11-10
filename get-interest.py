#!/usr/bin/python3

# RENTEN-RECHNUNG

'''
Ausgangssituation:
> Heute 10.000 oder in 10 Jahren 15.000?

15.000 = 10.000 * ( 1 + i ) ** 10

i = ( 15.000 / 10.000 ) ** ( 1/10 ) - 1

'''

BARWERT = 10.000
ENDWERT = 15.000
JAHRE = 10

def getInterest(e, b, j):
	return ( e / b ) ** ( 1 / j ) - 1

print( getInterest(ENDWERT, BARWERT, JAHRE) )
