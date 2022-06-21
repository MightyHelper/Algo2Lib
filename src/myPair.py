class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __str__(self):
		return f"({self.first}|{self.second})"

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, type(self)):
			return False
		return self.first == other.first and self.second == other.second


