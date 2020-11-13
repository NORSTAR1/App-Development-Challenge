import math;
def getAzimuth(latA, longA, latB, longB):
    azimuth = math.atan2(math.sin(longB-longA) * math.cos(latB), (math.cos(latA)*math.sin(latB)) - (math.sin(latA) * math.cos(latB) * math.cos(longB - longA)) );
    return azimuth;

def getElevation(xa, ya, za, xb, yb, zb):
    Xab = xb - xa;
    Yab = yb - ya;
    Zab = zb - za;
    if (Xab < 0 || Yab < 0 || Zab < 0):
        print("Input error!");              #The square root of a negative number doesn't exist.
        return -1;
    Range = math.sqrt(Xab**2 + Yab**2 + Zab**2);
    rz = Xab * math.cos(ya) * math.cos(xa) + Yab * math.cos(ya) * math.sin(xa) + Zab * math.sin(ya);
    elevation = math.asin(rz/Range);
    return elevation;

checkpoints = [];
if ( getAzimuth(moon to earth) == getAzimuth(moon to horizon) ):
    if ( getElevation(to earth) > getElevation(to horizon) ):
        checkpoints.append();
        
sortByHeight = checkpoints.sort(key=lambda x: x.max())[0:10];  #sort checkpoints by height and clip first 10
