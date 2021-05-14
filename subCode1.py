class Street:
		def __init__(self, index, begin, end, name, time):
			self.index = index
			self.begin = begin
			self.end = end
			self.name = name
			self.time = time

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index)
