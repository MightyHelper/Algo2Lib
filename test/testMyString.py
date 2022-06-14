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
		self.assertEqual(str(w * 3), "WorldWorldWorld")
		self.assertEqual(str(w[0:2]), "Wo")
		self.assertEqual(str(w[1:]), "orld")
		self.assertEqual(str(w[1::2]), "ol")
		self.assertEqual(str(w[::2]), "Wrd")
		self.assertEqual(str(w[-1]), "d")
		self.assertEqual(str(w[-3:-1]), "rl")
		self.assertEqual(str(w[-3:]), "rld")
		self.assertEqual(str(w[-3::2]), "rd")

	def test_ej1(self):
		"""Exists char"""
		self.assertTrue('o' in String("Hello"))
		self.assertTrue('H' in String("Hello"))
		self.assertFalse('z' in String("Hello"))
		self.assertFalse('1' in String("Hello"))

	def test_ej2(self):
		"""Is Palindrome"""
		self.assertTrue(String("").is_palindrome())
		self.assertTrue(String("a").is_palindrome())
		self.assertTrue(String("aa").is_palindrome())
		self.assertTrue(String("aba").is_palindrome())
		self.assertTrue(String("abba").is_palindrome())
		self.assertTrue(String("abacabadabacaba").is_palindrome())
		self.assertFalse(String("ab").is_palindrome())
		self.assertFalse(String("abab").is_palindrome())
		self.assertFalse(String("ababab").is_palindrome())
		self.assertFalse(String("abababab").is_palindrome())
		self.assertFalse(String("ababababab").is_palindrome())

	def test_ej3(self):
		"""MostRepeated char"""
		self.assertEqual(String("").most_repeated_char(), String(""))
		self.assertEqual(String("a").most_repeated_char(), String("a"))
		self.assertEqual(String("aa").most_repeated_char(), String("a"))
		self.assertEqual(String("aba").most_repeated_char(), String("a"))
		self.assertEqual(String("abba").most_repeated_char(), String("a"))
		self.assertEqual(String("abacabadabacaba").most_repeated_char(), String("a"))
		self.assertEqual(String("ab").most_repeated_char(), String("a"))
		self.assertEqual(String("abab").most_repeated_char(), String("a"))
		self.assertEqual(String("ababab").most_repeated_char(), String("a"))
		self.assertEqual(String("babaabbb").most_repeated_char(), String("b"))

	def test_ej4(self):
		"""LongestIsland"""
		self.assertEqual(String("").longest_island(), 0)
		self.assertEqual(String("a").longest_island(), 1)
		self.assertEqual(String("aa").longest_island(), 2)
		self.assertEqual(String("aba").longest_island(), 1)
		self.assertEqual(String("abba").longest_island(), 2)
		self.assertEqual(String("abacabadabacaba").longest_island(), 1)
		self.assertEqual(String("cdaaaaaasssbbb").longest_island(), 6)

	def test_ej5(self):
		"""IsAnagram"""
		self.assertTrue(String("").is_anagram(String("")))
		self.assertTrue(String("a").is_anagram(String("a")))
		self.assertTrue(String("aa").is_anagram(String("aa")))
		self.assertTrue(String("aab").is_anagram(String("aba")))
		self.assertTrue(String("baba").is_anagram(String("abba")))
		self.assertTrue(String("abacabadabacaba").is_anagram(String("aaaabcdabbacaba")))
		self.assertFalse(String("abacabadabacabaa").is_anagram(String("aaaabcdabbacaba")))
		self.assertFalse(String("abacabadabacabaa").is_anagram(String("aaaabcdabbacabab")))

	def test_ej6(self):
		"""BalancedParentheses"""
		self.assertTrue(String("").balanced("(", ")"))
		self.assertTrue(String("unrelated").balanced("(", ")"))
		self.assertTrue(String("(unrelated)").balanced("(", ")"))
		self.assertTrue(String("(unr(ela)ted)").balanced("(", ")"))
		self.assertFalse(String("(unr(elated)").balanced("(", ")"))
		self.assertFalse(String("unrela)(ted").balanced("(", ")"))
		self.assertFalse(String("unrela)()(ted").balanced("(", ")"))
		self.assertFalse(String("unr(elated))").balanced("(", ")"))

	def test_ej7(self):
		"""reduceLen"""
		self.assertEqual(String("").reduce_length_adjacent(), String(""))
		self.assertEqual(String("aaabccddd").reduce_length_adjacent(), String("abd"))
		self.assertEqual(String("faabbccddeef").reduce_length_adjacent(), String(""))
		self.assertEqual(String("acav").reduce_length_adjacent(), String("acav"))

	def test_ej8(self):
		"""String contained"""
		# self.assertTrue(String("").contains_in_order(String("")))
		# self.assertTrue(String("aaafffmmmarillzzzllhooo").contains_in_order(String("amarillo")))
		self.assertFalse(String("aaafffmmmarrrilzzzhooo").contains_in_order(String("amarillo")))

	def test_ej9(self):
		"""Match with wildcards"""
		self.assertTrue(String("").match_with_wildcard(String(""), "♢"))
		self.assertTrue(String("cabccbacbacab").match_with_wildcard(String("ab♢ba♢c"), "♢"))
		self.assertTrue(String("ma--tc0hme").match_with_wildcard(String("ma♢tc♢hme"), "♢"))
		self.assertFalse(String("ma--tc0hme").match_with_wildcard(String("ma♢tc♢hme"), " "))
		self.assertFalse(String("ab--ba-d").match_with_wildcard(String("ab♢ba♢c"), "♢"))

	def test_indexof(self):
		"""Index of"""
		self.assertEqual(String("").index_of("a"), -1)
		self.assertEqual(String("aa").index_of("a"), 0)
		self.assertEqual(String("aa").index_of("b"), -1)
		self.assertEqual(String("aab").index_of("b"), 2)
		self.assertEqual(String("aab").index_of("a", 0), 0)
		self.assertEqual(String("aab").index_of("a", 1), 1)
		self.assertEqual(String("aab").index_of("a", 2), -1)
		self.assertEqual(String("1234567890")[0:3], String("123"))
		self.assertEqual(String("123")[0:3], String("123"))

if __name__ == '__main__':
	unittest.main()
