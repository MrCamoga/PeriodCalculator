from period import *
from random import randint

sequences = [[0,1,2,3,4,5,0,1,2,3],[3,5,7],[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9],[0, 0, 0, 1, 1],[2,5,1,2,5,1,2,3],[1,2],[3],[1,2,1]]
for s in sequences:
	print(computePeriod(PeriodicList(s)))

for _ in range(10):
	length = randint(10,100000)
	s = [randint(0,255) for _ in range(length)]
	p,l=computePeriod(PeriodicList(s))
	if p!=length:
		print(p)
