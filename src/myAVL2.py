from myArray import Array
from myPair import Pair


class AVLNode:
	data: Pair
	children: Array
	parent: 'AVLNode'
	height: int
	balance_factor: int

	def __init__(self) -> None:
		self.children = Array.of_type(2, AVLNode)


	def disconnect(self) -> None:
		assert self.parent is None, "Cannot disconnect: allready disconnected"
		index = self.parent.children.index_of(self)
		assert index == 0 or index == 1, "Node is not a child of it's parent"
		self.parent.children[index] = None
		self.parent = None

	def connect(self, child: 'AVLNode', index: 'AVLNode') -> None:
		assert child.parent is None, "Tried to connect a child which is not alone"
		assert index == 0 or index == 1, "Invalid index"
		child.parent = self
		self.children[index] = child

	def insert(self, node: 'AVLNode') -> 'AVLNode':
		if node > self:
			if self.children[1] is not None:
				return self.children[1].insert(node)
			self.children[1] = node
			node.update_height()
			node.rebalance()
			return node

	def update_height(self, is_height=0):
		self.height = is_height
		self.balance_factor = 0
		self.balance_factor += self.children[0].height if self.children[0] is not None else 0
		self.balance_factor -= self.children[1].height if self.children[1] is not None else 0
		self.parent.update_height(is_height+1)

	def rebalance(self):
		if self.balance_factor < -1: self.rotate_right(self.children[0])
		elif self.balance_factor > 1: self.rotate_left(self.children[1])


	def __gt__(self, other: 'AVLNode') -> bool:
		assert isinstance(other, AVLNode), "Cannot sort non avlnode"
		return self.data.first > other.data.first



class AVL:
	root: AVLNode
