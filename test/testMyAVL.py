import unittest
import traceback

import src.myAVL as mAVL


class TestMyAVL(unittest.TestCase):
	def test_rotates_right(self):
		avl = mAVL.AVL()
		avl[235] = 235
		avl[234] = 234
		avl[123] = 123
		self.assertEqual(avl.root.value, 234)

	def test_rotates_left(self):
		avl = mAVL.AVL()
		avl[123] = 123
		avl[234] = 234
		avl[235] = 235
		self.assertEqual(avl.root.value, 234)

	def test_rotates_right_with_root(self):
		avl = mAVL.AVL()
		avl[239] = 239
		avl[235] = 235
		avl[234] = 234
		avl[123] = 123
		self.assertEqual(avl.root.value, 235)

	def test_rotates_left_with_root(self):
		avl = mAVL.AVL()
		avl[123] = 123
		avl[234] = 234
		avl[235] = 235
		avl[239] = 239
		self.assertEqual(avl.root.value, 234)

	def test_sorts(self):
		from random import randint as r
		clash_count = 0
		try:
			avl = mAVL.AVL()
			for i in range(0, 500):
				rand = 5
				clash_count -= 1
				while avl[rand] is not None:
					rand = r(-5000000, 5000000)
					clash_count += 1
				avl[rand] = rand
			values = [node.value for node in avl.root.in_order()]
			self.assertEqual(values, sorted(values))
		except BaseException as e:
			traceback.print_tb(e.__traceback__)
			raise e
		print(f"{clash_count=}")


if __name__ == '__main__':
	unittest.main()
