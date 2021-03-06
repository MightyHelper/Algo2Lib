from .myArray import *
from .myHash import AsciiHash, SlidingHash, MultiCompose
from .myLinkedList import LinkedList
from .mySort import main_sort


class String(Array):
	def __init__(self, str_in: Union['String', str, Array, int] = ""):
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

	def __contains__(self, char: str) -> bool:
		return self.index_of(char) != -1

	def is_palindrome(self) -> bool:
		for i in range(len(self) >> 1):
			if self[i] != self[-i - 1]:
				return False
		return True

	def most_repeated_char(self) -> 'String':
		arr = Array(256, 0, True)
		for i in self:
			arr[ord(i)] += 1
		max_i = 0
		for i in range(1, len(arr)):
			if arr[i] > arr[max_i]:
				max_i = i
		if arr[max_i] == 0:
			return String('')
		return String(chr(max_i))

	def longest_island(self) -> int:
		max_length = 0
		island_length = 0
		current_char = String('')
		for i in self:
			if i == current_char:
				island_length += 1
				continue
			if max_length < island_length:
				max_length = island_length
			island_length = 1
			current_char = i
		return island_length if max_length < island_length else max_length

	def is_anagram(self, other: 'String') -> bool:
		return main_sort(self, ord) == main_sort(other, ord)

	def balanced(self, start_block: str, end_block: str) -> bool:
		level = 0
		for i in self:
			if i == start_block:
				level += 1
			elif i == end_block:
				level -= 1
				if level < 0: return False
		return level == 0

	def reduce_length_adjacent(self) -> 'String':
		i = 0
		stack = LinkedList()
		while i < len(self):
			if not stack.is_empty() and stack[0] == self[i]:
				stack.pop_front_()
			else:
				stack.push_front_(self[i])
			i += 1
		out_len = len(stack)
		out = Array.of_type(out_len, str)
		for o in range(out_len):
			out[out_len - o - 1] = stack[o]
		return String(out)

	def contains_in_order(self, other: 'String', start_idx: int = 0) -> bool:
		idx = 0
		i = start_idx
		other_len = len(other)
		while idx < other_len:
			i = self.index_of(other[idx], i + 1)
			if i == -1: return False
			idx += 1
		return True

	def match_with_wildcard(self, other: 'String', wildcard: str) -> bool:
		sections = other.split(wildcard)
		section_index = 0
		string_index = 0
		while section_index < len(sections):
			string_index = self.naive_str_index_of(sections[section_index], string_index)
			if string_index == -1:
				return False
			section_index += 1
		return True

	def naive_longest_prefix(self, other: 'String') -> 'String':
		if len(other) == 0:
			return String("")
		if len(self) == 0:
			return String("")
		for i in range(0, len(other)):
			res = self.naive_str_index_of(other[:len(other) - i])
			if res != -1:
				return other[:len(other) - i]
		return String("")

	def compile_kmp(self) -> Array:
		out = Array.of_type(len(self), int)
		out[0] = 0
		for i in range(1, len(self)):
			if self[i] == self[out[i - 1]]:
				out[i] = out[i - 1] + 1
			elif self[i] == self[0]:
				out[i] = 1
			else:
				out[i] = 0
		return out

	def kmp_search(self, other: 'String') -> int:
		pattern = other.compile_kmp()
		matched = 0
		for i in range(len(self)):
			if self[i] == other[matched]:
				matched += 1
				if matched == len(other):
					return i - matched + 1
			else:
				matched = pattern[matched]
		return -1

	def starts_with(self, other: 'String') -> bool:
		if len(other) > len(self):
			return False
		return self[:len(other)] == other

	def ends_with(self, other: 'String') -> bool:
		if len(other) > len(self):
			return False
		return self[len(self) - len(other):] == other

	def compile_automata(self, vocabulary: 'String') -> Array:
		out = Array(len(self), Array(len(vocabulary), 0, True), True)
		for j in range(len(self)):
			for i in range(len(vocabulary)):
				for k in range(j, -1, -1):
					if self[j - k:j] + vocabulary[i] == self[:k + 1]:
						out[j][i] = k + 1
						break
		return out

	def compile_automata2(self, vocabulary: 'String') -> Array:
		out = Array(len(self), Array(len(vocabulary), 0), True)
		for j in range(len(self)):
			for i in range(len(vocabulary)):
				k = min(len(self) + 1, j + 2) - 1
				while (self[:j] + vocabulary[i]).starts_with(self[:k]) and k > 0:
					k -= 1
				out[j][i] = k
		print()
		for x in out:
			print(x)
		return out

	def longest_prefix(self, other: 'String') -> 'String':
		print(self, other)
		if len(other) == 0:
			return String("")
		prefix_len = 0
		max_prefix = -1
		other_p = other.compile_kmp()
		for i in self:
			if prefix_len == len(other):
				return other
			if i != other[prefix_len]:
				if prefix_len > max_prefix:
					max_prefix = prefix_len
				prefix_len = other_p[prefix_len]
			if i == other[prefix_len]:
				prefix_len += 1
		if prefix_len > max_prefix:
			max_prefix = prefix_len
		return other[:max_prefix]

	def count_automata(self, automata: Array, vocabulary: 'String') -> int:
		if len(automata) == 0: return 0
		if len(self) == 0: return 0
		if len(self) < len(automata): return 0
		state = 0
		count = 0
		for i in automata:
			print(i)
		print()
		print(self)
		for i in self:
			print(state, self)
			state = automata[state][vocabulary.index_of(i)]
			if state == len(automata):
				count += 1
				state = 0
		return count

	def rabin_karp_compile(self) -> int:
		slide = SlidingHash(len(self), 256, MultiCompose(AsciiHash()).hash(self))
		return next(iter(slide))

	def rabin_karp_search(self, other: 'String') -> int:
		"""For O(1) we can use python's hash function"""
		compiled = other.rabin_karp_compile()
		slide = SlidingHash(len(other), 256, MultiCompose(AsciiHash()).hash(self))
		for i, h in enumerate(slide):
			print(h, compiled, i)
			if h == compiled:
				return i
		return -1

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
