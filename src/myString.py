from .myArray import *
from .myCopy import *


class String:
	def __init__(self, str_in):
		self.data = Array.from_iterable(str_in)

	def __getitem__(self, item):
		return self.data[item]

	def __setitem__(self, key, value):
		self.data[key] = value

	def __str__(self):
		return self.data.join("")
