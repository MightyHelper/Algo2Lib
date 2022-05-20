from .myCopy import copy


class Array:
	data = []

	def __init__(self, size: int, init_value: any = 0, pre_fill: bool = False) -> None:
		self.size = size
		if size < 0:
			raise ValueError("Negative size doesn't make sense")
		self.data = [copy(init_value) for _ in range(0, size)] if pre_fill else [None for _ in range(0, size)]
		self.type = type(init_value)

	def __getitem__(self, index: int) -> any:
		if index > self.size:
			raise IndexError(f"Index out of bounds {index} > {self.size}")
		return self.data[index]

	def __setitem__(self, index: int, value: any) -> None:
		if index > self.size:
			raise IndexError(f"Index out of bounds {index} > {self.size}")
		elif type(value) != self.type and value is not None:
			raise ValueError(f"Expected a {self.type} but got a {type(value)}")
		self.data[index] = value

	def __str__(self) -> str:
		return str(self.data)

	def __len__(self) -> int:
		return self.size

	def __iter__(self):
		self.__iter = 0
		return self

	def __next__(self):
		if self.__iter >= self.size:
			raise StopIteration
		val = self[self.__iter]
		self.__iter += 1
		return val

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Array):
			return False
		if other.type != self.type:
			return False
		if other.size != self.size:
			return False
		for i in range(0, self.size):
			if self[i] != other[i]:
				return False
		return True

	@staticmethod
	def from_iterable(iterable) -> 'Array':
		if len(iterable) == 0:
			return Array(0)
		out = Array(len(iterable), iterable[0])
		for idx, x in enumerate(iterable):
			out[idx] = x
		return out
