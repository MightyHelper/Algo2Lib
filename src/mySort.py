from .myIterable import Iterable
from .myLinkedList import LinkedList


def merge_sort_recursive(ll: Iterable, hasher, start: int, end: int) -> LinkedList:
	"""Standard mergesort implementation"""
	if end - start == 0: return LinkedList()
	if end - start == 1: return LinkedList() + ll[start]
	out = LinkedList()
	mid = int((start + end + 1) / 2)
	a = merge_sort_recursive(ll, hasher, start, mid)
	b = merge_sort_recursive(ll, hasher, mid, end)
	ia = 0
	ib = 0
	la = len(a)
	lb = len(b)
	for i in range(la + lb):
		va = hasher(a[ia]) if ia < la else 1000000000000
		vb = hasher(b[ib]) if ib < lb else 1000000000000
		if va < vb:
			out += a[ia]
			ia += 1
		else:
			out += b[ib]
			ib += 1
	return out


def merge_sort(ll: Iterable, hasher) -> LinkedList:
	"""Overload to hide start and end parameters"""
	return merge_sort_recursive(ll, hasher, 0, len(ll))


def main_sort(iterable: Iterable, hasher) -> LinkedList:
	return merge_sort(iterable, hasher)
