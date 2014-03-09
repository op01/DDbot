
def n():
	print "OK"

class diamond(object):
	"""docstring for diamond"""
	def __init__(self,l):
		super(diamond, self).__init__()
		self.n = -1
		self.l = l
		self.s = 0
	def set(self,n,l):
		self.l = l
		self.n = n

class counter(object):
	"""docstring for counter"""
	def __init__(self,l):
		super(counter, self).__init__()
		self.n = 0
		self.l = l