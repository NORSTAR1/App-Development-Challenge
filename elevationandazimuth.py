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

179.4
l = sqrt(2*moonradius*height+height**2);
checkpoints = [];
earth = [361000, 0, -42100];
horizon = [0,0,0];
csvfile = open('data.csv')

inFile = csv.reader(csvfile, delimiter=',', quotechar='"');
for row in inFile:
    if (getElevation(row[0], row[1], row[2], earth[0], earth[1], earth[2]) == 0):
        horizon = row;
        print("Horizon : ", horizon);
inFile = csv.reader(csvfile, delimiter=',', quotechar='"');
for row in inFile:
    lat = row[0];
    long = row[1];
    height = row[2];
    slope = row[3];
    if ( getAzimuth(lat, long, earth[0], earth[1]) == getAzimuth(lat, long, horizon[0], horizon[1]) ):
        if ( getElevation(lat, long, height, earth[0], earth[1], earth[2]) > getElevation(lat, long, height, horizon[0], horizon[1], horizon[2]) ):
            checkpoints.append();
        

def sortBy(by=2): #sort checkpoints by 'by' and clip the first 10
    global checkpoints;
    checkpointsBySort = [];    
    for i in range(len(checkpoints)):
        checkpointsBySort.append(checkpoints[i][by]);
    checkpointsBySort.sort(reverse=True);
    for i in range(len(checkpoints)):
        for g in range(0, len(checkpoints)):
            if (checkpointsBySort[g] == checkpoints[i][by]):
                checkpointsBySort[g] = checkpoints[i];
    return(checkpointsBySort[:10]);

byLat = sortBy(0); #sort by highest longitude
byLong = sortBy(1); #sort by highest latitude
byHeight = sortBy(2); #sort by the heighest point
bySlope = sortBy(3); #sort by the highest slope

