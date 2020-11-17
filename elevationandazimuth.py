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

for row in inFile:
    if ()


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



def sortBy(by=2):
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

