import math;
def getAzimuth(latA, longA, latB, longB):
    azimuth = atan2(sin(longB-longA) * cos(latB), (cos(latA)*sin(latB)) - (sin(latA) * cos(latB) * cos(longB - longA)) );
