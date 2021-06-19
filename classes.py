class Map:
	def __init__(self):
		self.map= [[0,0,0],[0,0,0],[0,0,0]]
		
	def tomap(self,m):
		r = ''
		for l in m:
			for i in l:
				if i == 0:
					r += ' _ '
				elif i == 1:
					r += '\033[34m X \033[m'
				elif i == 2:
					r += '\033[35m O \033[m'
			r += '\n'
		return r
	
	def show(self):
		print(self.tomap(self.map))
	
	def tofil(self):
		a = [[y,(xx,yy)]for xx,x in enumerate(self.map) for yy,y in enumerate(x)]
		return a[:3],a[3:6],a[6:]
		
	def todia(self):
		c = self.tocol()
		x = 0
		y = 2
		a = []
		b = []
		for l in c:
			a.append(l[x])
			b.append(l[y])
			x += 1
			y -= 1
		return a,b
	
	def tocol(self):
		a = [[x[0],(c,0)] for c,x in enumerate(self.map)]
		b = [[x[1],(c,1)] for c,x in enumerate(self.map)]
		c = [[x[2],(c,2)] for c,x in enumerate(self.map)]
		return (a,b,c)
		
	def draw(self,data,x,y):
		if self.map[x][y] == 0:
			self.map[x][y] = data
		else:
			raise ValueError('casa ocupada')
	def win(map):#map is self
		def todo(map,d):
			for y in map:
				if y[0] != d:
					return False
			return True 
		col = map.tocol()
		dia = map.todia()
		fil = map.tofil()
		for d in 1,2:
			for x in col:
				if todo(x,d):
					return d
			for x in dia:
				if todo(x,d):
					return d
			for x in fil:
				if todo(x,d):
					return d
		return False
	def __str__(self):return str(self.map)
		