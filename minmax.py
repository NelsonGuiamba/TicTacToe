import  sys
sys.path.append('../Goodrich/ch08')
from linkedTree import linkedTree as	Arvore
from classes import Map
from copy import deepcopy
class Minmax:
	def __init__(self,p):
		self.tree = Arvore()
		self.player = p
		self.first = False
	def empty(self,b):
		l = []
		for i in range(3):
			for j in range(3):
				if b[i][j] == 0:
					l.append([i,j])
		return l
	
	def play(self,m):
		if len(self.empty(m.map)) == 8:
			return (1,1)
		if len(self.empty(m.map)) == 9:
			for x,y in  [(1,1),(0,0),(0,2),(2,2),(2,0)]:
				if m.map[x][y] == 0:
					self.tree = Arvore()
					#print('caso bases') known position return available corner
					return x,y
		if not self.first :
			self.tree.add_root(dict(map=m,res=0,jogada=None))
			self._minmax(self.player,self.tree.root())
			self.first = True
		else:
			for i in  self.tree.children(self.tree.root()):
				if i.element()['map'].map == m.map:
					self.tree.replace_tree(i)
					break
		if self.player == 1:
			#look for minium
			op =  self.tree._make_position(self.tree._root._children[0])
			for jogar in self.tree.children(self.tree.root()):
				if jogar.element()['res'] < op.element()['res']:
					op = jogar
			self.tree.replace_tree(op)
			return op.element()['jogada']
		else:
			#look for maxium
			op =  self.tree._make_position(self.tree._root._children[0])
			for jogar in self.tree.children(self.tree.root()):
				if jogar.element()['res'] > op.element()['res']:
					op = jogar
			self.tree.replace_tree(op)
			return op.element()['jogada']
		
	def _minmax(self,i,tmp=None):
		w = tmp.element()['map'].win()
		if w == 1:
			tmp.element()['res'] = -1
			return
		elif w == 2:
			tmp.element()['res'] = 1
			return
		elif len(self.empty(tmp.element()['map'].map)) ==0:
			tmp.element()['res'] = 0
			return
		eq = None
		for jogar in self.empty(tmp.element()['map'].map):
			m  = deepcopy(tmp.element()['map'])
			m.draw(i,*jogar)
			p = self.tree.add_children(tmp,dict(map=m,res=None,jogada=jogar))
			self._minmax(self.change(i),p)
			#if p.element()['res'] == 0:input('sim')
			if eq is None:
				eq = p.element()['res']
			elif i == 1:
				if p.element()['res'] < eq:
					eq = p.element()['res']
			elif i == 2:
				if p.element()['res'] > eq:
					eq = p.element()['res']
			
		tmp.element()['res'] = eq
	def change(self,x):
		if x == 1:return 2
		return 1


if __name__ == '__main__':
	m = Map()

	ia = Minmax(1)
	m.show()
	print('Fim')
#input(str(type(m)))
#ia.tree.add_root(dict(map=m,res=0,jogada=None))
	m.draw(ia.player,*ia.play(m))
	m.show()
#print('*'*29)
#for i in ia.tree.breadthfirst():
#		i.element()['map'].show()
#		print(i.element()['jogada'],i.element()['res'])
#		input()