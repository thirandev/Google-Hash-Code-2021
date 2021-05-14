class Inter:
		def __init__(self, index):
			self.index = index
			self.ins = []
			self.outs = []
			self.schedule = []
			
		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index) + str(self.schedule).replace('[', '{').replace(']', '}')
