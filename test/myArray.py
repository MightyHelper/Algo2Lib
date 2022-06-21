import unittest
import src.myArray as mArray


class TestMyArray(unittest.TestCase):
	def test_constructor(self):
		self.assertTrue(mArray.Array(1, 1).type is int)
		self.assertTrue(mArray.Array(1, 0.1).type is float)
		self.assertTrue(mArray.Array(2, 0.1).size == 2)
		self.assertTrue(mArray.Array(7, 0.1).size == 7)
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


if __name__ == '__main__':
	unittest.main()
