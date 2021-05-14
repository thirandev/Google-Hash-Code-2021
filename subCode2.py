class Car:
		def __init__(self, index, path, timeRemaining):
			self.index = index
			self.path = path
			self.timeRemaining = timeRemaining

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index) + ':' + str(self.timeRemaining) + ':' + str(self.path).replace('[', '{').replace(']', '}')
