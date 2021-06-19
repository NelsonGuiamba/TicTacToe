from tree import Tree
class linkedTree(Tree):
	class _Node:
		__slots__ = ['_parent','_children','_element']
		def __init__(self,ele,p=None):
			self._parent = p
			self._children = []
			self._element = ele
		def element(self):return self._element
	class Position(Tree.Position):
		def __init__(self,container,node):
			self._container = container
			self._node = node
			
		def element(self):
			return self._node._element
		
		def __eq__(self,other):
			return type(self) == type(self) and self._node == other._node
	
	def _validate(self,p):
		if not isinstance(p, self.Position):
			raise TypeError('p must be proper Position type')
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._parent is p._node:      # convention for deprecated node
			raise ValueError('p is no longer valid')
		return p._node
	
	def  _make_position(self, node):
		return self.Position(self, node) if node is not None else None
	
	def __init__(self):
		self._root = None
		self._size = 0
	def root(self): return self._make_position(self._root)
	
	def parent(self,p):
		node = self._validate(p)
		return node._parent
		
	def num_children(self,p):
		node = self._validate(p)
		return len(node._children)
	
	def children(self,p):
		node = self._validate(p)
		for i in node._children:
			yield self._make_position(i)
	
	def __len__(self):return self._size
	
	def add_root(self,e):
		
		if self._root is not None:
			raise ValueError('Root exists')
		self._root = self._Node(ele=e)
		self._size += 1
		return self._make_position(self._root)
	
	def add_children(self,p,e):
		
		p = self._validate(p)
		node = self._Node(e,p)
		p._children.append(node)
		self._size += 1
		return self._make_position(node)
	def replace_tree(self,p):
		p = self._validate(p)
		self._root = p