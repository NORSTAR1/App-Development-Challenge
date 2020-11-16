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

csvfile = open('data.csv')
inFile = csv.reader(csvfile, delimiter=',', quotechar='"');
for row in inFile:
    lat = row[0];
    long = row[1];
    height = row[2];
    slope = row[3];
    if ( getAzimuth(lat, long, to earth) == getAzimuth(lat,long, to horizon) ):
        if ( getElevation(to earth) > getElevation(to horizon) ):
            checkpoints.append();
        

        
checkpoints = [[-88, 2, 4, 5], [-89, 3, 2, 5], [-90, 1, 2, 3]];
#sortByHeight = checkpoints.sort(key=lambda x: max(x))[0:10]  #sort checkpoints by height and clip first 10



def sortBy(checkpoints, by=2):
    checkpointsBySort = [];    
    for i in range(len(checkpoints)-1):
        checkpointsBySort.append(checkpoints[i][by]);
    checkpointsBySort.sort();
    while (len(checkpointsBySort) < len(checkpoints)):
        if (checkpointsBySort[i] == checkpoints[i][by]):
            checkpointsBySort[i] = checkpoints[i];
    return(checkpointsByHeight[0:10])

byLat = sortBy(checkpoints, 0);
byLong = sortBy(checkpoints, 1);
byHeight = sortBy(checkpoints, 2);
bySlope = sortBy(checkpoints, 3);

