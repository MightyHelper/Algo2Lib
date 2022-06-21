class Pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __str__(self):
		s1, s2 = str(self.first), str(self.second)
		if s1 == s2:
			return f"({s1}|)"
		return f"({s1}|{s2})"

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, type(self)):
			return False
		return self.first == other.first and self.second == other.second


