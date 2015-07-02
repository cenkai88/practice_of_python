from functools import reduce

def  str2float(s):
	def str2int(a):return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[a]
	def list2int(x,y):return x*10+y
	if (s.find(".")==-1): return reduce(list2int, map(str2int,s))
	else: 
		length=len(s)-1
		digit=s.index('.')
		s=s.replace(".", "")
		return reduce(list2int, map(str2int,s))/float(math.pow(10,length-digit))

str2float('123.45678')