import unittest
import src.myLinkedList as mLinkedList
import src.myCopy as mCopy


class TestMyLinkedList(unittest.TestCase):
	def test_inserts_iter(self):
		arr = mLinkedList.LinkedList()
		arr.push_front(4)
		arr.push_back(5)
		arr.push_front(3)
		arr.push_back(6)
		arr.push_front(2)
		arr.push_front(1)
		arr.push_back(7)
		self.assertEqual([*arr], [*range(1, 8)])
		self.assertEqual(arr.pop_front().value, 1)
		self.assertEqual(arr.pop_front().value, 2)
		self.assertEqual(arr.pop_back().value, 7)
		self.assertEqual(arr.pop_back().value, 6)
		self.assertEqual(len(arr), 3)
		self.assertEqual(str(arr), str([*range(3, 6)]))

	def test_from_iterable(self):
		iterable = [1, 2, 4, 8, 2, 1, 78]
		self.assertEqual([*mLinkedList.LinkedList.from_iterable(iterable)], iterable)

	def test_slices(self):
		iterable = [*range(100)]
		arr = mLinkedList.LinkedList.from_iterable(iterable)
		for i in range(50, 80, 3):
			self.assertEqual([*arr[i:90]], iterable[i:90])
		for i in range(50, 80, 3):
			self.assertEqual([*arr[i:90:3]], iterable[i:90:3])
		for i in range(50, 80, 3):
			self.assertEqual([*arr[i:]], iterable[i:])
			self.assertEqual([*arr[:i]], iterable[:i])

	def test_set_item(self):
		arr = mLinkedList.LinkedList.from_iterable([*range(10)])
		for i in range(10):
			arr[i] = 10 - i
		for i in range(10):
			self.assertEqual(arr[i], 10 - i)

	def test_recompute_size(self):
		a = mLinkedList.LinkedListNode()
		a.push_next(1).push_next(1).push_next(1).push_next(1)
		ll = mLinkedList.LinkedList(a)
		self.assertEqual(5, ll.re_compute_size())
		self.assertFalse(ll.is_empty())
		ll.root = None
		self.assertEqual(0, ll.re_compute_size())
		self.assertTrue(ll.is_empty())

	def test_exceptions(self):
		with self.assertRaises(IndexError):
			a = mLinkedList.LinkedList()
			a.push_front(123)
			# noinspection PyTypeChecker
			b = a["Hello?"]
		with self.assertRaises(IndexError):
			a = mLinkedList.LinkedList()
			a.push_front(123)
			b = a[0:0:-1]
		with self.assertRaises(IndexError):
			a = mLinkedList.LinkedList()
			a.push_front(123)
			b = a[999]
		with self.assertRaises(IndexError):
			a = mLinkedList.LinkedList.from_iterable([*range(10)])
			b = a[5:2]
		with self.assertRaises(ValueError):
			# noinspection PyTypeChecker
			mLinkedList.LinkedList.from_iterable([1, 2, 3]).pop_index(None)

	def test_indices(self):
		arr = mLinkedList.LinkedList.from_iterable([1, 2, 3, 10, 11, 112, 1431])
		self.assertEqual(arr.index_of(2), 1)
		self.assertEqual(arr.index_of(1), 0)
		self.assertEqual(arr.index_of(4), -1)
		self.assertEqual(arr.pop_index(1).value, 2)
		self.assertEqual(arr.pop_index(1).value, 3)
		self.assertEqual(arr.index_of(2), -1)
		self.assertEqual(arr.push_after_index(2, 12345).value, 12345)
		self.assertEqual(arr[3], 12345)
		self.assertEqual(arr.push_before_index(2, 121212).value, 121212)
		self.assertEqual(arr[2], 121212)
		self.assertEqual(arr.pop_index(0).value, 1)
		self.assertEqual(arr.push_before_index(0, 1).value, 1)
		self.assertEqual(arr[0], 1)

	def test_copy(self):
		arr = mLinkedList.LinkedList.from_iterable([1, 2, 3, 4, 5, 65])
		arr2 = mCopy.copy(arr)
		self.assertEqual(arr, arr2)

	def test_node(self):
		for x in (123, "123", 0.5, 1 + 1j):
			self.assertEqual(str(mLinkedList.LinkedListNode(x)), str(x))
		self.assertNotEqual(mLinkedList.LinkedListNode(123), 123)

	def test_eq(self):
		self.assertEqual(mLinkedList.LinkedList.from_iterable([1,2,3]),mLinkedList.LinkedList.from_iterable([1,2,3]))
		self.assertNotEqual(mLinkedList.LinkedList.from_iterable([1,2,3]),[1,2,3])
		self.assertNotEqual(mLinkedList.LinkedList.from_iterable([1,2,3]),mLinkedList.LinkedList.from_iterable([1,2,3,4]))
		self.assertEqual(mLinkedList.LinkedList.from_iterable([]),mLinkedList.LinkedList.from_iterable([]))
		self.assertNotEqual(mLinkedList.LinkedList.from_iterable([1,2,3]),mLinkedList.LinkedList.from_iterable([1,4,3]))


if __name__ == '__main__':
	unittest.main()
