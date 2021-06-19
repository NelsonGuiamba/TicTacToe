from classes import *
from minmax import Minmax
#def win(map):
#	def todo(map,d):
#		for y in map:
#			if y[0] != d:
#				return False
#		return True 
#	col = map.tocol()
#	dia = map.todia()
#	fil = map.tofil()
#	for d in 1,2:
#		for x in col:
#			if todo(x,d):
#				return d
#		for x in dia:
#			if todo(x,d):
#				return d
#		for x in fil:
#			if todo(x,d):
#				return d
#	return False
a = Map()

def leint(sms):
	while True:
		try:
			a = int(input(sms))
		except:
			print('numero invalido')
			continue
		return a

def menu():
	print('Jogo da velha')
	print('\tMenu')
	while True:
		print('Jogar como Xis [1]')
		print('Jogar como Bola [2]')
		print('Sair [3]')
		op = leint('Sua opcao:')
		if op < 0 or op > 3:
			print('Opcao invalida')
		break
	return op

def jogando(p):
	from os import system
	draw=0
	enemy = 2 if p == 1 else 1
	ia = Minmax(enemy)
	m = Map()
	system('clear')
	print('Comecando o jogo')
	m.show()
	while True:
		while True:
			y = leint('Digite a coluna [1 a 3] ')
			if y < 1 or y > 3:
				print('Coluna invalida')
				continue
			break
		while True:
			x = leint('Digite a fileira [1 a 3] ')
			if x < 1 or x > 3:
				print('Fileira invalida')
				continue_
			break
		try:
			m.draw(p,x-1,y-1)
		except:
			print('\033[31mCasa ocupada\033[m')
			continue
		
		draw+=1
		m.show()
		est = m.win()
		if draw == 5:
			print('\033[33mJogo empatado\033[m')
			return
		
		if est == p:
			print('\033[32mVoce venceu!!!\033[m')
			return
		m.draw(ia.player,*ia.play(m))
		m.show()

		if m.win() == enemy:
			print('\033[31mO computador venceu\033[m')
			return
		
		if est == False:
			continue
		
		
while True:
	op = menu()
	if op == 1 or op == 2:
		jogando(op)
	else:
		print('Volte sempre')
		break