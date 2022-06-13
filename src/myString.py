from myPair import Pair
from mySort import main_sort
from .myArray import *
from .myLinkedList import LinkedList


class String(Array):
	def __init__(self, str_in: Union['String', str, Array, int]):
		if isinstance(str_in, str) or isinstance(str_in, String) or isinstance(str_in, Array):
			super().__init__(len(str_in), '')
			for idx, x in enumerate(str_in):
				self[idx] = x
		else:
			super().__init__(str_in, '')

	def new_array_of_same_type(self, length: int) -> 'String':
		return String(length)

	def __str__(self) -> str:
		return self.join("")

	def __add__(self, other: 'String') -> 'String':
		# noinspection PyTypeChecker
		return self.concat(other)

	def __mul__(self, other: int) -> 'String':
		out = String(self)
		for i in range(other - 1):
			out = out + self
		return out

	def _ansi_apply(self, *token_parameters: 'String') -> 'String':
		parameter_sum = String("")
		for i in token_parameters:
			parameter_sum = parameter_sum + i + String(";")
		parameter_sum = parameter_sum[:-1]
		return parameter_sum + self + ANSI_NORMAL

	def visible_length(self) -> int:
		in_escape_code = False
		out_len = 0
		for c in self:
			if not in_escape_code:
				if c == ANSI_ESCAPE:
					in_escape_code = True
				else:
					out_len += 1
			else:
				if 'A' < c < 'z':
					in_escape_code = False
		return out_len

	def to_normal(self):
		return self._ansi_apply(ANSI_NORMAL)

	def to_bold(self):
		return self._ansi_apply(ANSI_BOLD)

	def to_faint(self):
		return self._ansi_apply(ANSI_FAINT)

	def to_italic(self):
		return self._ansi_apply(ANSI_ITALIC)

	def to_underline(self):
		return self._ansi_apply(ANSI_UNDERLINE)

	def to_crossed(self):
		return self._ansi_apply(ANSI_CROSSED)

	def to_overline(self):
		return self._ansi_apply(ANSI_OVERLINE)

	def to_fg_rgb(self, r, g, b):
		return self._ansi_apply(ANSI_FG_RGB, r, g, b)

	def to_bg_rgb(self, r, g, b):
		return self._ansi_apply(ANSI_BG_RGB, r, g, b)

	def __contains__(self, char: 'String') -> bool:
		return self.index_of(self) != -1

	def is_palindrome(self) -> bool:
		for i in range(len(self)>>1):
			if self[i] != self[-i-1]:
				return False
		return True

	def most_repeated_char(self) -> 'String':
		arr = Array(256, 0, True)
		for i in self:
			arr[ord(i)]+=1
		max_i = 0
		for i in range(1, len(arr)):
			if arr[i] > arr[max_i]:
				max_i = i
		return chr(max_i)

	def longest_island(self) -> int:
		max_l = 0
		l = 0
		cc = String('')
		for i in self:
			if i == cc:
				l += 1
				continue
			if max_l < l:
				max_l = l
			l = 1
			cc = i
		return max_l

	def is_anagram(self, other: 'String') -> bool:
		return main_sort(self) == main_sort(other)

	def balanced(self, open: 'String', close: 'String') -> bool:
		level = 0
		for i in self:
			if i == open: level += 1
			elif i == close:
				level -= 1
				if level < 0: return False
		return True

	def reduce_length_adjacent(self) -> 'String':
		l=0
		u=1
		le=len(self)
		skips = LinkedList()
		while u < le:
			while self[l] == self[u]:
				if l == 0:
					skips += Pair(l, u)
					break
				if u == le:
					skips += Pair(l, u)
					break
				l -= 1
				u += 1
			l = u
			u += 1

		i = 0
		out = String('')
		for j in skips:
			for k in range(i, j.first):
				out += self[k]
			i = j.second
		for k in range(i, le):
			out += self[k]
		return out



	def contains_in_order(self, other: 'String') -> bool:
		idx = 0
		i = 0
		l = len(other)
		while idx < l:
			i = self.index_of(other[idx], i)
			if i == -1: return False
			idx += 1
		return True



ANSI_ESC = String("\033")
ANSI_ESCAPE = ANSI_ESC + String("[")
ANSI_NORMAL = ANSI_ESCAPE + String("0m")
ANSI_BOLD = ANSI_ESCAPE + String("1m")
ANSI_FAINT = ANSI_ESCAPE + String("2m")
ANSI_ITALIC = ANSI_ESCAPE + String("3m")
ANSI_UNDERLINE = ANSI_ESCAPE + String("4m")
ANSI_CROSSED = ANSI_ESCAPE + String("9m")
ANSI_OVERLINE = ANSI_ESCAPE + String("53m")
ANSI_FG_RGB = ANSI_ESCAPE + String("38;2;")
ANSI_BG_RGB = ANSI_ESCAPE + String("48;2;")
