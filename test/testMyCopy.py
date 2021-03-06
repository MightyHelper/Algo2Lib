import unittest
import src.myCopy as mCopy


class TestMyCopy(unittest.TestCase):
	def assertWorks(self, value):
		self.assertEqual(value, mCopy.copy(value))

	def assertFull(self, value):
		dup = mCopy.copy(value)
		self.assertEqual(value, dup)
		self.assertFalse(value is dup, value)

	def test_literals(self):
		for x in (True, 1, 0, "hg", "hello", "", None, 1.0, 2 + 3j):
			self.assertWorks(x)

	def test_lists(self):
		for x in ([1, 2, 3], [], [1424124124124121, 14242, 14, 24, 14, 12, 4], [1, 2, 3, [2, 3, 4]]):
			self.assertFull(x)

	def test_dicts(self):
		for x in ({"a": "b", 1: "ccc", (1, 2, 3): 12, "aa": [123], ("a", "z"): "k"}, {"a": {"a": {"a": 1}}}):
			self.assertFull(x)

	def test_manual_copy(self):
		class J:
			val = 123
			mm = "XXX"

			def __str__(self):
				return f"J-{self.val}{self.mm}"

		class T:
			v = J()
			k = 2

			def __str__(self):
				return f"T-{self.v}{self.k}"

		t = T()
		t.k = 123
		self.assertEqual(str(t), str(mCopy.copy(t)))
		self.assertFalse(t is mCopy.copy(t))


if __name__ == '__main__':
	unittest.main()
