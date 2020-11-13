import math;
def getAzimuth(latA, longA, latB, longB):
    azimuth = atan2(math.sin(longB-longA) * math.cos(latB), (math.cos(latA)*math.sin(latB)) - (math.sin(latA) * math.cos(latB) * math.cos(longB - longA)) );
    return azimuth;

def getElevation(xa, ya, za, xb, yb, zb):
    Xab = xb - xa;
    Yab = yb - ya;
    Zab = zb - za;
    Range = math.sqrt(Xab**2 + Yab**2 + Zab**2);
    rz = Xab * math.cos(ya) * math.cos(xa) + Yab * math.cos(ya) * math.sin(xa) + Zab * math.sin(ya);
    elevation = math.asin(rz/Range);
    return elevation;

if ( getAzimuth(moon to earth) == getAzimuth(moon to horizon) ):
    if ( getElevation(to earth) > getElevation(to horizon) ):
        ding ding ding
