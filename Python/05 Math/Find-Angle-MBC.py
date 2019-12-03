import math

ab = int(input())
bc = int(input())

print( str( round( math.degrees( math.atan2(ab,bc) ) ) ) + '°' )