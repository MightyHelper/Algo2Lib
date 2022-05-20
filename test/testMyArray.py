import unittest
import src.myArray as mArray


class TestMyArray(unittest.TestCase):
	def test_constructor(self):
		self.assertTrue(mArray.Array(1, 1).type is int)
		self.assertTrue(mArray.Array(1, 0.1).type is float)
		self.assertTrue(len(mArray.Array(2, 0.1)) == 2)
		self.assertTrue(len(mArray.Array(7, 0.1)) == 7)
		self.assertTrue(mArray.Array(3, 0.1).data == [None, None, None])
		self.assertTrue(mArray.Array(3, 0.1, False).data == [None, None, None])
		self.assertTrue(mArray.Array(3, 0.1, True).data == [0.1, 0.1, 0.1])

	def test_get(self):
		arr = mArray.Array(5, 0.5, True)
		arr.data[2] = 0.1
		for i in range(5):
			self.assertEqual(arr[i], 0.1 if i == 2 else 0.5)

	def test_set(self):
		arr = mArray.Array(5, 0.5, True)
		arr[2] = 0.1
		for i in range(5):
			self.assertEqual(arr.data[i], 0.1 if i == 2 else 0.5)

	def test_iter(self):
		arr = mArray.Array(5, 0)
		arr.data = [*range(5)]
		for i, val in enumerate(arr):
			self.assertEqual(i, val)
		self.assertEqual(len(mArray.Array.from_iterable([])), 0)

	def test_exceptions(self):
		with self.assertRaises(ValueError):
			mArray.Array(-1, 123, False)
		with self.assertRaises(IndexError):
			a = mArray.Array(2, 123, False)[123]
		with self.assertRaises(IndexError):
			mArray.Array(2, 123, False)[123] = 5
		with self.assertRaises(ValueError):
			mArray.Array(2, 123, False)[1] = 5.2

	def test_eq(self):
		arr1 = mArray.Array.from_iterable([1, 2, 3])
		arr2 = mArray.Array.from_iterable([1, 2, 3])
		self.assertEqual(arr1, arr2)
		arr1[0] = 123
		self.assertNotEqual(arr1, arr2)
		arr2[0] = 123
		self.assertEqual(arr1, arr2)
		self.assertEqual(str(arr1), str(arr2))
		self.assertNotEqual(arr1, "")
		self.assertNotEqual(arr1, str(arr1))
		self.assertNotEqual(arr1, mArray.Array.from_iterable([1, 2, 3, 4]))
		self.assertNotEqual(arr1, mArray.Array.from_iterable([1.0, 1.5, 1.2]))


if __name__ == '__main__':
	unittest.main()
