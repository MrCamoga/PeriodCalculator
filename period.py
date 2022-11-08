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
	match=1
	period=0
	states=[0]*STATESSIZE
	buffer=[]
	si=0
	for s in l:
		if si < len(states):
			states[si] = s
		si += 1
		if states[match]!=s:
			match=0
			period+=1
			while len(buffer)>0:
				for i in range(len(buffer)):
					if states[match]!=buffer[i]:
						match=0
						break
					else:
						match+=1
				else:
					break # ESTO FALTA EN EL DE JAVA
				buffer.remove(0)
				period+=1
		else:
			match += 1
			buffer.append(s)
			if match > MINMATCH and (match == len(states) or match > REPEATPERCENT*period):
				return period,states[0:period]
