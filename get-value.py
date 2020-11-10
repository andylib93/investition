#!/usr/bin/python3

# setze die Variablen
VALUE = 100000
GIVEN = 200000
INTEREST = 0.07
YEARS = 10

# gewünschter wert / jahreszins hoch anzahl jahre = zu zahlender wert
def getDesiredValue(v, i, y):
	return v / (1 + i) ** y

# kapitalwert * (1 + (zins mal jahre)) = endkapital
def withGivenValue(g, i, y):
	return g * (1 + (i * y))

print('Zu zahlender Wert:')
print(getDesiredValue(VALUE, INTEREST, YEARS))
print('Endkapital:')
print(withGivenValue(GIVEN, INTEREST, YEARS))
