from typing import Optional, Tuple

from src.myArray import Array
from src.myIterable import Iterable


class ArrayWrapper(Iterable):
	@staticmethod
	def from_iterable(iterable) -> 'Iterable':
		pass

	def pop_index(self, index: int) -> Tuple[any, 'Iterable']:
		pass

	def push_before_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		pass

	def push_after_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		pass

	def __eq__(self, other) -> bool:
		pass

	def __iter__(self) -> any:
		pass

	def __next__(self) -> any:
		pass

	def __getitem__(self, item) -> any:
		pass

	def __setitem__(self, key, value) -> None:
		pass

	def push_front(self, value) -> Tuple[any, 'Iterable']:
		pass

	def push_back(self, value) -> Tuple[any, 'Iterable']:
		pass

	def pop_front(self) -> Tuple[any, 'Iterable']:
		pass

	def pop_back(self) -> Tuple[any, 'Iterable']:
		pass

	def get_slice(self, key: slice) -> Optional['Iterable']:
		pass

	def concat(self, other: 'Iterable') -> 'Iterable':
		pass

	def __init__(self, sz, tp, init):
		arr = Array(sz, tp, init)
