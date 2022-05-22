import unittest
import src.myLinkedList as mLinkedList
import src.myCopy as mCopy


class TestMyLinkedList(unittest.TestCase):

	def test_from_iterable(self):
		iterable = [1, 2, 4, 8, 2, 1, 78]
		self.assertEqual([*mLinkedList.LinkedList.from_iterable(iterable)], iterable)

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
