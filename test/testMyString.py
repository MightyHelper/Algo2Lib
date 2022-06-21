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
		self.assertEqual(str(w[0:2]), "Wo")
		self.assertEqual(str(w[1:]), "orld")
		self.assertEqual(str(w[1::2]), "ol")
		self.assertEqual(str(w[::2]), "Wrd")
		self.assertEqual(str(w[-1]), "d")
		self.assertEqual(str(w[-3:-1]), "rl")
		self.assertEqual(str(w[-3:]), "rld")
		self.assertEqual(str(w[-3::2]), "rd")


if __name__ == '__main__':
	unittest.main()
