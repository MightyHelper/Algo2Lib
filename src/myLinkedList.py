from typing import Union, Optional

from .myCopy import copy


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


class LinkedList:
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

	def is_empty(self) -> bool:
		return self.root is None

	def get_node(self, index: int) -> LinkedListNode:
		index = self._parse_index(index)
		c_node = self.root
		for i in range(index):
			c_node = c_node.next
		return c_node

	def _parse_index(self, index, default=None):
		if index is None:
			if default is None:
				raise ValueError("Default value: None")
			else:
				return default
		if index < 0:
			index = self.size + index
		if index >= self.size or index < 0:
			raise IndexError(f"{index=} not available in list of length {self.size}.")
		return index

	def push_front(self, other: any) -> LinkedListNode:
		new_node = LinkedListNode(other, self.root)
		self.root = new_node
		self.size += 1
		return new_node

	def push_back(self, other: any) -> LinkedListNode:
		new_node = self.get_node(-1).push_next(other)
		self.size += 1
		return new_node

	def pop_front(self) -> LinkedListNode:
		out = self.root
		self.root = self.root.next
		self.size -= 1
		return out

	def pop_back(self) -> LinkedListNode:
		popped_node = self.get_node(-2).pop_next()
		self.size -= 1
		return popped_node

	def get_slice(self, key: slice) -> Optional['LinkedList']:
		start, stop, step = self._parse_index(key.start, 0), self._parse_index(key.stop, self.size), self._parse_step(key.step, 1)
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

	@staticmethod
	def _parse_step(step, default=1):
		if step is None:
			step = default
		if step < 1:
			raise IndexError(f"Cannot iterate with step < 1 ... yet.")
		return step

	def __getitem__(self, key: Union[slice, int]) -> any:
		if isinstance(key, slice):
			return self.get_slice(key)
		if isinstance(key, int):
			return self.get_node(key).value
		raise IndexError(f"Unknown index type {type(key)}.")

	def __setitem__(self, index: int, value: any):
		index = self._parse_index(index)
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

	def __str__(self):
		return f"[{self.join()}]"

	def join(self, joiner: str = ', ') -> str:
		out = ""
		for i in self:
			out += str(i) + joiner
		return out[:-2]

	def re_compute_size(self) -> int:
		self.size = 0
		c_node = self.root
		while c_node is not None:
			c_node = c_node.next
			self.size += 1
		return self.size

	def __len__(self) -> int:
		return self.size

	def index_of(self, value):
		for i, val in enumerate(self):
			if val == value:
				return i
		return -1

	def pop_index(self, index: int) -> LinkedListNode:
		index = self._parse_index(index, None)
		if index == 0:
			return self.pop_front()
		return self.get_node(index - 1).pop_next()

	def push_before_index(self, index: int, value: any) -> LinkedListNode:
		index = self._parse_index(index)
		if index == 0:
			return self.push_front(value)
		return self.get_node(index - 1).push_next(value)

	def push_after_index(self, index: int, value: any) -> LinkedListNode:
		index = self._parse_index(index)
		return self.get_node(index).push_next(value)

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

