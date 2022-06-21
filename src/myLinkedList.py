from typing import Union, Optional, Tuple

from .myCopy import copy
from .myIterable import Iterable


class LinkedListNode:
	def __init__(self, value: any = None, next_node: 'LinkedListNode' = None):
		self.value = value
		self.next: Optional[LinkedListNode] = next_node

	def __next__(self):
		return self.next

	def __copy__(self):
		return LinkedListNode(copy(self.value), copy(self.next))

	def push_next(self, other: any) -> 'LinkedListNode':
		new_node = LinkedListNode(other, self.next)
		self.next = new_node
		return new_node

	def pop_next(self) -> 'LinkedListNode':
		popped_node = self.next
		if self.next is not None:
			self.next = self.next.next
		return popped_node

	def __str__(self):
		return str(self.value)

	def __eq__(self, other):
		if not isinstance(other, LinkedListNode):
			return False
		return self.value == other.value


class LinkedList(Iterable):
	def __init__(self, head: LinkedListNode = None, expected_size: int = 0):
		self.root = head
		self.size = expected_size

	def __deepcopy__(self):
		return LinkedList(copy(self.root), self.size)

	@staticmethod
	def from_iterable(iterable) -> 'LinkedList':
		out_head = LinkedListNode()
		out_tail = out_head
		expected_length = 0
		for x in iterable:
			out_tail = out_tail.push_next(x)
			expected_length += 1
		return LinkedList(out_head.next, expected_length)

	def get_node(self, index: int) -> LinkedListNode:
		index = self.parse_index(index)
		c_node = self.root
		for i in range(index):
			c_node = c_node.next
		return c_node

	def push_front_(self, other: any) -> LinkedListNode:
		new_node = LinkedListNode(other, self.root)
		self.root = new_node
		self.size += 1
		return new_node

	def push_front(self, other: any) -> Tuple[any, 'Iterable']:
		return self.push_front_(other).value, self

	def push_back(self, other: any) -> LinkedListNode:
		new_node = self.get_node(-1).push_next(other)
		self.size += 1
		return new_node

	def pop_front_(self) -> LinkedListNode:
		out = self.root
		self.root = self.root.next
		self.size -= 1
		return out

	def pop_front(self) -> Tuple[any, 'Iterable']:
		return self.pop_front_().value, self

	def pop_back_(self) -> LinkedListNode:
		popped_node = self.get_node(-2).pop_next()
		self.size -= 1
		return popped_node

	def pop_back(self) -> Tuple[any, 'Iterable']:
		return self.pop_back_().value, self

	def get_slice(self, key: slice) -> Optional['LinkedList']:
		start, stop, step = self.parse_index(key.start, 0), self.parse_index(key.stop, self.size), self.parse_step(key.step, 1)
		if start > stop:
			raise IndexError(f"Cannot iterate from {start} to {stop}.")
		out_list_head = LinkedListNode()
		out_list_tail = out_list_head
		c_node = self.get_node(start)
		expected_size = 0
		for i in range(int(((stop - start) / step) + 0.99999)):
			out_list_tail = out_list_tail.push_next(c_node.value)
			expected_size += 1
			for k in range(step):
				c_node = c_node.next
		return LinkedList(out_list_head.next, expected_size)

	def __getitem__(self, key: Union[slice, int]) -> any:
		if isinstance(key, slice):
			return self.get_slice(key)
		if isinstance(key, int):
			return self.get_node(key).value
		raise IndexError(f"Unknown index type {type(key)}.")

	def __setitem__(self, index: int, value: any):
		index = self.parse_index(index)
		self.get_node(index).value = value

	def __iter__(self):
		self.__iter = self.root
		return self

	def __next__(self):
		if self.__iter is None:
			raise StopIteration
		out = self.__iter
		self.__iter = self.__iter.next
		return out.value

	def re_compute_size(self) -> int:
		self.size = 0
		c_node = self.root
		while c_node is not None:
			c_node = c_node.next
			self.size += 1
		return self.size

	def pop_index_(self, index: int) -> LinkedListNode:
		index = self.parse_index(index, None)
		if index == 0:
			return self.pop_front_()
		return self.get_node(index - 1).pop_next()

	def push_before_index_(self, index: int, value: any) -> LinkedListNode:
		index = self.parse_index(index)
		if index == 0:
			return self.push_front_(value)
		return self.get_node(index - 1).push_next(value)

	def push_after_index_(self, index: int, value: any) -> LinkedListNode:
		index = self.parse_index(index)
		return self.get_node(index).push_next(value)

	def pop_index(self, index: int) -> Tuple[any, 'Iterable']:
		return self.pop_index_(index).value, self

	def push_before_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		return self.push_before_index_(index, value).value, self

	def push_after_index(self, index: int, value: any) -> Tuple[any, 'Iterable']:
		return self.push_after_index_(index, value).value, self

	def __eq__(self, other):
		if not isinstance(other, LinkedList):
			return False
		if len(other) != len(self):
			return False
		if len(other) == 0:
			return True
		s_node = self.root
		o_node = other.root
		for i in range(len(other)):
			if s_node != o_node:
				return False
			s_node = next(s_node)
			o_node = next(o_node)
		return True

