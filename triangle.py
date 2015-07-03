#杨辉三角
def triangles():
	row=[1]
	while True:
		yield row
		row=[sum(i) for i in zip([0]+row,row+[0])]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break