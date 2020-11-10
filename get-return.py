#!/usr/bin/python3

# VERZINSUNG

WERT = 10000
ZINS = 0.4
JAHRE = 20
result = 0

for year in range (1, (JAHRE + 1)):
	calculation = WERT / (1 + ZINS ** year)
	result += calculation
	print(result)
