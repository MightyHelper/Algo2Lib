from typing import Optional, Union, Tuple, Type

from .myCopy import copy
from .myIterable import Iterable


class Array(Iterable):
	def concat(self, other: 'Iterable') -> 'Iterable':
		out = self.new_array_of_same_type(len(self) + len(other))
		i = 0
		for x in self:
			out[i] = x
			i += 1
		for x in other:
			if not isinstance(x, self.type):
				raise ValueError(f"Cannot concatenate iterable into the array because of type mismatch ({self.type} vs {type(x)}).")
			out[i] = x
			i += 1
		return out

	data = []

	def pop_index(self, index: int) -> Tuple[any, 'Iterable']:
		new_array = self.new_array_of_same_type(len(self) - 1)
		for i in range(len(self) - 1):
			new_array[i] = self[i if i < index else i + 1]
		return self[index], new_array

	def new_array_of_same_type(self, length: int) -> 'Array':
		return Array.of_type(length, self.type)

	def __copy__(self):
		out = self.new_array_of_same_type(len(self))
		for i, v in enumerate(self):
			out[i] = v
		return out

	@staticmethod
	def of_type(size: int, t: Type) -> 'Array':
		out = Array(size)
		out.type = t
		return out

	def push_before_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		new_array = self.new_array_of_same_type(len(self) + 1)
		new_array[index] = value
		for i in range(len(self)):
			new_array[i if i < index else i + 1] = self[i]
		return value, new_array

	def push_after_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		return self.push_before_index(index + 1, value)

	def push_front(self, value) -> Tuple[any, 'Iterable']:
		new_array = self.new_array_of_same_type(len(self) + 1)
		new_array[0] = value
		for i in range(len(self)):
			new_array[i + 1] = self[i]
		return value, new_array

	def push_back(self, value) -> Tuple[any, 'Iterable']:
		new_array = self.new_array_of_same_type(len(self) + 1)
		new_array[-1] = value
		for i in range(len(self)):
			new_array[i] = self[i]
		return value, new_array

	def pop_front(self) -> Tuple[any, 'Iterable']:
		new_array = self.new_array_of_same_type(len(self) - 1)
		for i in range(len(self) - 1):
			new_array[i] = self[i + 1]
		return self[0], new_array

	def pop_back(self) -> Tuple[any, 'Iterable']:
		new_array = self.new_array_of_same_type(len(self) - 1)
		for i in range(len(self) - 1):
			new_array[i] = self[i]
		return self[-1], new_array

	def __init__(self, size: int, init_value: any = None, pre_fill: bool = False) -> None:
		self.size = size
		if size < 0:
			raise ValueError("Negative size doesn't make sense")
		self.data = [copy(init_value) for _ in range(0, size)] if pre_fill else [None for _ in range(0, size)]
		self.type = type(init_value)

	def get_slice(self, key: slice) -> Optional['Array']:
		start, stop = self.parse_index(key.start, 0), self.parse_index(key.stop, self.size)
		step = self.parse_step(key.step, 1)
		if start > stop:
			raise IndexError(f"Cannot iterate from {start} to {stop}.")
		out_array = self.new_array_of_same_type(int(((stop - start) / step) + 0.99999))
		for i in range(len(out_array)):
			out_array[i] = self[i * step + start]
		return out_array

	def __getitem__(self, key: Union[slice, int]) -> any:
		if isinstance(key, slice):
			return self.get_slice(key)
		if isinstance(key, int):
			if key > self.size:
				raise IndexError(f"Index out of bounds {key} > {self.size}")
			return self.data[key]
		raise IndexError(f"Unknown index type {type(key)}.")

	def __setitem__(self, index: int, value: any) -> None:
		if index > self.size:
			raise IndexError(f"Index out of bounds {index} > {self.size}")
		elif not isinstance(value, self.type) and value is not None:
			raise ValueError(f"Expected a {self.type} but got a {type(value)}")
		self.data[index] = value

	def __str__(self) -> str:
		return str(self.data)

	def __len__(self) -> int:
		return self.size

	def __iter__(self):
		return ArrayIterator(self)

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, type(self)):
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

	def split(self, value: any) -> 'Array':
		out = self.of_type(0, Array)
		accumulator = self.new_array_of_same_type(0)
		for i in self:
			if i == value:
				_, out = out.push_back(accumulator)
				accumulator = self.new_array_of_same_type(0)
			else:
				_, accumulator = accumulator.push_back(i)
		if not accumulator.is_empty():
			_, out = out.push_back(accumulator)
		return out


class ArrayIterator:
	def __init__(self, array: Array):
		self.array = array
		self.index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= self.array.size:
			raise StopIteration
		self.index += 1
		return self.array[self.index - 1]
