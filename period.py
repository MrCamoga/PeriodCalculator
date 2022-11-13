STATESSIZE = 1000000
MINMATCH = 5000
REPEATPERCENT = 1.3

class PeriodicList:
	def __init__(self,l):
		self.l=l
		self.index=0

	def __iter__(self):
		self.index=0
		return self

	def __next__(self):
		x = self.l[self.index]
		self.index = (self.index+1)%len(self.l)
		return x

def computePeriod(l):
	match=0
	period=0
	states=[-1]*STATESSIZE
	si=0
	for s in l:
		if states[match]!=s:
			m=0
			while match>0:
				for i in range(match):
					if states[m]!=states[m+i]:
						m=0
						break
					else:
						m+=1
				else:
					break
				match-=1
			period=si+1-match
		else:
			match += 1
			if match > MINMATCH and (match == len(states) or match > REPEATPERCENT*period):
				return period,states[0:period]
		if si < len(states):
			states[si] = s
		si+=1
