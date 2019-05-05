import math

class MatrixNxN:
	def __init__(self,*args):
		self.matrix=[]
		args_elements=[]
		self.matrix_length=[i for i in args]
		
		#if math.sqrt(len(args))-int(math.sqrt(len(args))):
		#	print('Matrix should be a N X N !!!')
		#	return 1

		for value in args:
			args_elements.append(value)
			if len(args_elements)==math.sqrt(len(args)):
				self.matrix.append(args_elements)
				args_elements=[]


	def __add__(self,other):
		
		return MatrixNxN(*(sft(self.matrix,other.matrix)))
	def add(self,other):
		return MatrixNxN(*(sft(self.matrix,other.matrix)))



	def display(self):
		arat(self.matrix)
	def __str__(self):
		
		return '\n'.join([''.join(['{:{}}'.format(item,4) for item in row]) for row in self.matrix])


	def __mul__(self, other):
		return MatrixNxN(*(prodh(self.matrix,other.matrix)))
	def __iadd__(self,other):
		if isinstance(other, (int,float)):
			return MatrixNxN(*(egalplus(self.matrix,other)))
		else:
		     return MatrixNxN(*(sft(self.matrix,other.matrix)))
	def __imul__():
		if isinstance(other, (int)):
			return MatrixNxN(*(egalmul(self.matrix,other)))
		else:
		     return MatrixNxN(*(prodh(self.matrix,other.matrix)))
def prodh(matrix,omatrix):
	if len(matrix) != len(omatrix):
			print('matrix should be the same size ')
			return 1
	c=[]
	result=[[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*omatrix)] for X_row in matrix]
	for i in range(len(result)):
		for j in range(len(result[0])):
			c.append(result[i][j])
	
	return c
def arat(matrix):
	print()
	print('\n'.join([''.join(['{:{}}'.format(item,4) for item in row]) for row in matrix]))
def sft(matrix,omatrix):
	if len(matrix) != len(omatrix):
			print('matrix should be the same size ')
			return 1
	c=[]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			c.append(matrix[i][j]+omatrix[i][j])
		
	return c

def egalplus(matrix,value):
	c=[]
	if isinstance(value, int):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				c.append(matrix[i][j]+value)
	return c
def egalmul(matrix,value):
	c=[]
	if isinstance(value, int):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				c.append(matrix[i][j]*value)
	return c





		
