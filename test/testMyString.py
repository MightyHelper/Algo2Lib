import unittest

from src.myString import String


class TestMyString(unittest.TestCase):
	def test_create(self):
		self.assertEqual(str(String("Hello")), "Hello")
		self.assertEqual(str(String("")), "")
		h = String("Hello")
		w = String("World")
		self.assertEqual(str(h + String(" ") + w), "Hello World")
		h[0] = 'T'
		self.assertEqual(str(h), "Tello")
		self.assertEqual(str(w*3), "WorldWorldWorld")


if __name__ == '__main__':
	unittest.main()
