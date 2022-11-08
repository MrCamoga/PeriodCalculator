from period import *

sequences = [[0,1,2,3,4,5,0,1,2,3],[3,5,7],[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9],[0, 0, 0, 1, 1],[2,5,1,2,5,1,2,3],[1,2],[3],[1,2,1]]
for s in sequences:
        print(computePeriod(PeriodicList(s)))
