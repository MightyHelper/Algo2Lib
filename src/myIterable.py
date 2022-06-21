from abc import ABC, abstractmethod
from typing import Optional, Tuple

from .myCopy import copy


class Iterable(ABC):
	size: int = 0

	@staticmethod
	@abstractmethod
	def from_iterable(iterable) -> 'Iterable':
		pass

	def index_of(self, value: any, start: int = 0) -> int:
		start = self.parse_index(start, None)
		iterator = enumerate(self)
		for o in range(start):
			next(iterator)
		for i, val in iterator:
			if val == value:
				return i
		return -1

	def naive_str_index_of(self, other: 'Iterable', start: int = 0):
		if len(other) > len(self):
			return -1
		if len(other) == 0:
			return 0
		i = start
		while i < len(self):
			if i == -1:
				return -1
			if i + len(other) <= len(self) and other == self[i:i + len(other)]:
				return i
			i = self.index_of(other[0], i + 1)
		return -1

	def is_empty(self) -> bool:
		return len(self) == 0

	def parse_index(self, index: int, default: int = None) -> int:
		if index is None:
			if default is None:
				raise ValueError("Default value: None")
			else:
				return default
		if index < 0:
			index = len(self) + index
		if default == len(self) and index == default:
			return default
		if (index >= len(self) or index < 0):
			raise IndexError(f"{index=} not available in list of length {len(self)}.")
		return index

	def __len__(self) -> int:
		return self.size

	@abstractmethod
	def pop_index(self, index: int) -> Tuple[any, 'Iterable']:
		pass

	@abstractmethod
	def push_before_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		pass

	@abstractmethod
	def push_after_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		pass

	@abstractmethod
	def __eq__(self, other) -> bool:
		pass

	@abstractmethod
	def __iter__(self) -> any:
		pass

	@abstractmethod
	def __getitem__(self, item) -> any:
		pass

	@abstractmethod
	def __setitem__(self, key, value) -> None:
		pass

	@abstractmethod
	def push_front(self, value) -> Tuple[any, 'Iterable']:
		pass

	@abstractmethod
	def push_back(self, value) -> Tuple[any, 'Iterable']:
		pass

	@abstractmethod
	def pop_front(self) -> Tuple[any, 'Iterable']:
		pass

	@abstractmethod
	def pop_back(self) -> Tuple[any, 'Iterable']:
		pass

	@staticmethod
	def parse_step(step, default=1):
		if step is None:
			step = default
		if step < 1:
			raise IndexError(f"Cannot iterate with step < 1 ... yet.")
		return step

	def join(self, joiner: str = ', ') -> str:
		out = ""
		for i in self:
			out += str(i) + joiner
		return out[:len(out) - len(joiner)]

	def __str__(self):
		return f"[{self.join()}]"

	@abstractmethod
	def get_slice(self, key: slice) -> Optional['Iterable']:
		pass

	@abstractmethod
	def concat(self, other: 'Iterable') -> 'Iterable':
		pass

	def __add__(self, other):
		if not isinstance(other, Iterable):
			_, other = copy(self).push_back(other)
			return other
		return self.concat(other)

	def __repr__(self):
		return f"[{type(self).__name__}:{self}]"

	@staticmethod
	def split(self, value: any) -> 'Iterable':
		pass
