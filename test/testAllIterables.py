import unittest
from typing import Type

import src.myLinkedList as mLinkedList
import src.myArray as mArray

from src.myIterable import Iterable


def test_iterable(iterable_clz: Type[Iterable]):
	class TestMyIterables(unittest.TestCase):
		def test_from_iterable(self):
			iterable = [1, 2, 4, 8, 2, 1, 78]
			self.assertEqual([*iterable_clz.from_iterable(iterable)], iterable)

		def test_slices(self):
			iterable = [*range(100)]
			arr = iterable_clz.from_iterable(iterable)
			for i in range(50, 80, 3):
				self.assertEqual([*arr[i:90]], iterable[i:90])
			for i in range(50, 80, 3):
				self.assertEqual([*arr[i:90:3]], iterable[i:90:3])
			for i in range(50, 80, 3):
				self.assertEqual([*arr[i:]], iterable[i:])
				self.assertEqual([*arr[:i]], iterable[:i])

		def test_set_item(self):
			arr = iterable_clz.from_iterable([*range(10)])
			for i in range(10):
				arr[i] = 10 - i
			for i in range(10):
				self.assertEqual(arr[i], 10 - i)

		def test_indices(self):
			arr = iterable_clz.from_iterable([1, 2, 3, 10, 11, 112, 1431])
			self.assertEqual(arr.index_of(2), 1)
			self.assertEqual(arr.index_of(1), 0)
			self.assertEqual(arr.index_of(4), -1)
			v, arr = arr.pop_index(1)
			self.assertEqual(v, 2)
			v, arr = arr.pop_index(1)
			self.assertEqual(v, 3)
			self.assertEqual(arr.index_of(2), -1)
			v, arr = arr.push_after_index(2, 12345)
			self.assertEqual(v, 12345)
			self.assertEqual(arr[3], 12345)
			v, arr = arr.push_before_index(2, 121212)
			self.assertEqual(v, 121212)
			self.assertEqual(arr[2], 121212)
			v, arr = arr.pop_index(0)
			self.assertEqual(v, 1)
			v, arr = arr.push_before_index(0, 1)
			self.assertEqual(v, 1)
			self.assertEqual(arr[0], 1)
	return TestMyIterables


TestLinkedList = test_iterable(mLinkedList.LinkedList)
TestArray = test_iterable(mArray.Array)

if __name__ == '__main__':
	unittest.main()
