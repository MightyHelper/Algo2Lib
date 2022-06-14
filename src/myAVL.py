from typing import Union

from myArray import Array
from myCopy import copy
from myLinkedList import LinkedList
from myPair import Pair


class AVL:
	def __init__(self, root: 'AVLNode' = None):
		self.root = root

	def __setitem__(self, key: int, value: any):
		node = AVLNode(key, value)
		if self.root is None:
			self.root = node
			return
		self.root = self.root.insert(node)

	def __getitem__(self, item: int) -> any:
		if self.root is None:
			return None
		result = self.root.search(item)
		return result.value if result is not None else None

	def __delitem__(self, key: int):
		if self.root is None:
			raise ValueError(f"Item {key} to delete not found")
		self.root = self.root.delete(key)

	def __str__(self):
		return f"AVL{'[]' if self.root is None else self.root.in_order()}"


class AVLNode:
	def __init__(self, key: int, value: any = None):
		if value is None:
			value = key
		self.parent = None
		self.children = Array.of_type(2, AVLNode)
		self.data = Pair(key, value)
		self.balance_factor = 0
		self.height = 0

	def __copy__(self):
		out = AVLNode(self.key, self.value)
		out.children = copy(self.children)
		for x in out.children:
			if x: x.parent = out
		out.balance_factor = self.balance_factor
		return out

	def __getattr__(self, item: str) -> Union[any, 'AVLNode']:
		if item == 'key': return self.data.first
		elif item == 'value': return self.data.second
		elif item == 'left': return self.children[0]
		elif item == 'right': return self.children[1]
		else: return super().__getattribute__(item)

	def __setattr__(self, key: str, value: Union[any, 'AVLNode']):
		if key == 'key': self.data.first = value
		elif key == 'value': self.data.second = value
		elif key == 'left': self.children[0] = value
		elif key == 'right': self.children[1] = value
		else: return super().__setattr__(key, value)

	def _insert_on_child(self, child: int, node: 'AVLNode') -> None:
		if self.children[child] is None: self.attach(node, child)
		else: self.children[child].insert(node)
		# self.balance_factor += 1 if child == 0 else -1
		self.height = self.get_height()
		self.balance_factor = self.calculate_bf()

	def _rebalance(self) -> 'AVLNode':
		if self.balance_factor ** 2 < 2: return self
		direction = 1 if self.balance_factor > 1 else 0
		return self.children[1 - direction].rotate(direction)

	def insert(self, node: 'AVLNode'):
		result = self.compare_keys(node.key)
		if result == -1:
			raise ValueError("Duplicate keys in AVL")
		self._insert_on_child(result, node)
		return self._rebalance()

	def delete(self, key: int) -> 'AVLNode':
		result = self.compare_keys(key)
		if result == -1: return self
		if self.children[result] is not None:
			return self.children[result].delete(key)
		raise ValueError(f"Item {key} to delete not found")

	def search(self, key: int) -> 'AVLNode':
		result = self.compare_keys(key)
		if result == -1: return self
		return self.children[result].search(key) if self.children[result] is not None else None

	def compare_keys(self, key: int) -> int:
		if self.key < key: return 1
		if self.key > key: return 0
		if self.key == key: return -1

	def in_order(self, rem=1000) -> LinkedList:
		out = LinkedList()
		if rem < 0: return out
		if self.children[0] is not None: out = out + self.children[0].in_order(rem - 1)
		out = out + self
		if self.children[1] is not None: out = out + self.children[1].in_order(rem - 1)
		return out

	def post_order(self) -> LinkedList:
		out = LinkedList()
		if self.children[0] is not None: out = out + self.children[0].post_order()
		if self.children[1] is not None: out = out + self.children[1].post_order()
		out = out + self
		return out

	def pre_order(self) -> LinkedList:
		out = LinkedList()
		out = out + self
		if self.children[0] is not None: out = out + self.children[0].post_order()
		if self.children[1] is not None: out = out + self.children[1].post_order()
		return out

	def get_height(self):
		return max(self.left.get_height() if self.left else 0, self.right.get_height() if self.right else 0) + 1

	def calculate_bf(self):
		lh = (0 if self.left is None else self.left.get_height())
		rh = (0 if self.right is None else self.right.get_height())
		self.balance_factor = lh - rh
		if self.left: self.left.calculate_bf()
		if self.right: self.right.calculate_bf()
		return self.balance_factor

	def post_rotate_get_bf(self, direction):
		p = self
		r = p.parent
		A = p.children[1 - direction]
		B = p.children[direction]
		C = r.other_child(p) if r else None

		b_A = A.balance_factor if A else 0
		b_B = B.balance_factor if B else 0
		b_C = C.balance_factor if C else 0

		b_p = b_B - b_A
		b_r = b_C - b_p

		b_r = b_C - b_B
		b_p = b_r - b_A

		if r: r.balance_factor = b_r
		p.balance_factor = b_p

	def rotate(self, direction=0):
		beta_node, pivot, root, x, zero = self.get_named_for_rotation(direction)
		if pivot is not None:
			pivot = pivot.rotate(1 - direction)
			beta_node, pivot, root, x, zero = pivot.get_named_for_rotation(direction)
		print(pivot.in_order())
		root.detach()
		pivot.detach()
		if beta_node: beta_node.detach()
		if root: root.attach(beta_node, 1 - direction)
		if zero: zero.attach(pivot, x)
		pivot.attach(root, direction)
		# print(pivot.in_order()); pivot.post_rotate_get_bf(direction)
		print(pivot.treed())
		pivot.calculate_bf()
		print(pivot.treed())
		return pivot

	def get_named_for_rotation(self, direction):
		pivot = self
		beta_node = pivot.children[direction]
		root = pivot.parent
		zero = root.parent if root else None
		x = zero.children.index_of(root) if zero else None
		return beta_node, pivot, root, x, zero

	def remove_child(self, child: 'AVLNode'):
		self.children[self.children.index_of(child)] = None
		child.parent = None

	def detach(self):
		if self.parent: self.parent.remove_child(self)

	def attach(self, node: 'AVLNode', index: int):
		self.children[index] = node
		if node: node.parent = self

	def other_child(self, child: 'AVLNode') -> 'AVLNode':
		return self.children[1 - self.children.index_of(child)]

	def __repr__(self) -> str:
		return str(self)

	def __str__(self) -> str:
		return f"{self.data}_{self.balance_factor}"

	# return f"[{self.left}_{self.data}_{self.right}]"

	def treed(self, indent=0):
		# return f"[{self.left.treed() if self.left else 'X'}_{self.balance_factor}_{self.right.treed() if self.right else 'X'}]"
		l = self.left.treed(indent + 1) if self.left else (indent * '    ') + '  /X'
		r = self.right.treed(indent + 1) if self.right else (indent * '    ') + '  \\X'
		return f"{l}\n{indent * '    '}{self.get_height()}|{self.balance_factor}\n{r}"
