#汉诺塔，递归实现，注意从后往前考虑
def hanoi(n,a,b,c):
	if n==1:
		print ('%s-->%s'%(a,c))
	else:
		hanoi(n-1, a,c,b) #将a上n-1个看成整体，移到b
		hanoi(1,a,b,c) #将a上最底下1个移到c
		hanoi(n-1,b,a,c) #将b上的n-1个移到c

print(hanoi(3,'A','B','C'))