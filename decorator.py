import functools

def log (text):
	if isinstance(text, str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper (*args,**kw):
				print ("begin call")
				print ("%s:" % text)
				res=func(*args,**kw)
				print ("end call")
				return res
			return wrapper
		return decorator
	else:
		@functools.wraps(text)
		def  wrapper(*args, **kw):
			print ("begin call")
			print('calling %s():' % text.__name__)
			res=text(*args,**kw)
			print ("end call")
			return res
		return wrapper


@log
def now():
	print ("I love you")

now()

@log("Say")
def now2():
	print ("I love you")

now2()

