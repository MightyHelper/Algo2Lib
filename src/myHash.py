from abc import ABC, abstractmethod

from src.myIterable import Iterable
from src.myLinkedList import LinkedList


class Hash(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def hash(self, key: any) -> int:
		pass

	def compose(self, other: 'Hash') -> 'Hash':
		return HashCompose(self, other)


class HashCompose(Hash):
	def __init__(self, first: Hash, second: Hash):
		super().__init__()
		self.first = first
		self.second = second

	def hash(self, key: any) -> int:
		return self.first.hash(self.second.hash(key))


class ModHash(Hash):
	def __init__(self, mod: int):
		super().__init__()
		self.mod = mod

	def hash(self, key: any) -> int:
		return key % self.mod


class AsciiHash(Hash):
	def hash(self, key: str) -> int:
		return ord(key)


class MultiHash(Hash):
	def hash(self, key: Iterable) -> int:
		return sum(key)


class MultiCompose(Hash):
	def __init__(self, hasher: Hash):
		super().__init__()
		self.hasher = hasher

	def hash(self, key: Iterable) -> Iterable:
		out = LinkedList()
		for x in key:
			out.push_back_(self.hasher.hash(x))
		return out


class MultHash(Hash):
	def __init__(self, buckets, a=(5 ** 0.5 - 1) / 2):
		super().__init__()
		self.buckets = buckets
		self.a = a

	def hash(self, key: int) -> int:
		return int(((self.a * key) % 1) * self.buckets)


class SlidingHash:
	def __init__(self, width: int, buckets: int, iterable: 'Iterable'):
		super().__init__()
		self.buckets = buckets
		self.iterable = iterable
		self.width = width
		self.__iter_front = None
		self.__iter_back = None
		self.__slide = 0
		self.__head = None
		self.done = False

	def __iter__(self):
		self.__iter_front = self.iterable.__iter__()
		self.__iter_back = self.iterable.__iter__()
		assert self.__iter_front is not self.__iter_back, "Iterable does not support parallel iteration"
		for i in range(self.width):
			self.__slide *= self.buckets
			self.__slide += self.__iter_front.__next__()
		return self

	def __next__(self):
		if self.done:
			raise StopIteration
		old_slide = self.__slide
		self.__slide -= self.__iter_back.__next__() * (self.buckets ** (self.width - 1))
		self.__slide *= self.buckets
		try:
			self.__slide += self.__iter_front.__next__()
		except StopIteration:
			self.done = True
		return old_slide
