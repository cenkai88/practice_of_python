#
def _int_iter():
	n=1
	while  True:
		n=n+1
		yield n
		pass

def indivisible(n):
	return lambda x: x%n > 0

def primes():
	it=_int_iter()
	yield 2
	while True:
		it=filter(indivisible(n), it)
		n=next(it)
		yield n


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
