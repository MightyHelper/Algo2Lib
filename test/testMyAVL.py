import time
import unittest
import traceback

import src.myAVL as mAVL


class TestMyAVL(unittest.TestCase):

	def test_str(self):
		try:
			avl = mAVL.AVL()
			for x in (0, 5, -5, -2, 7, -7):
				avl[x] = x
				print(str(avl))
		except BaseException as e:
			print(traceback.print_tb(e.__traceback__))
			print(e)

	def test_rotates_right(self):
		avl = mAVL.AVL()
		avl[3] = 3
		avl[2] = 2
		avl[1] = 1
		self.assertEqual(avl.root.value, 2)

	def test_rotates_left(self):
		avl = mAVL.AVL()
		avl[1] = 1
		avl[2] = 2
		avl[3] = 3
		self.assertEqual(avl.root.value, 2)

	def test_rotates_right_with_root(self):
		avl = mAVL.AVL()
		print(avl.root.treed())
		avl[4] = 4
		avl[3] = 3
		avl[2] = 2
		avl[1] = 1
		self.assertEqual(avl.root.value, 3)
		self.assertEqual(avl.root[mAVL.LEFT].value, 2)
		self.assertEqual(avl.root[mAVL.RIGHT].value, 4)
		self.assertEqual(avl.root[mAVL.LEFT][mAVL.LEFT].value, 1)

	def test_rotates_video(self):
		try:

			avl = mAVL.AVL()
			for x in (60, 20, 100, 80, 120):
				avl[x] = x
			print(avl)
			avl[70] = 70
			print(avl)
		except BaseException as e:
			traceback.print_tb(e.__traceback__)
			raise e

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

		print(f"{clash_count=}")

if __name__ == '__main__':
	unittest.main()
