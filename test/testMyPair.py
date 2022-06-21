import unittest
import src.myPair as mPair


class TestMyPair(unittest.TestCase):
	def test(self):
		pair1 = mPair.Pair(123, "abc")
		self.assertEqual(pair1.first, 123)
		self.assertEqual(pair1.second, "abc")
		pair2 = mPair.Pair(123, "abc")
		self.assertEqual(pair1, pair2)
		pair3 = mPair.Pair(125, "abc")
		pair1.first += 2
		self.assertEqual(pair1, pair3)


if __name__ == '__main__':
	unittest.main()
