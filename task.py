from Matrix import MatrixNxN

def main():
	matrix0=MatrixNxN()
	matrix1x1=MatrixNxN(1)
	matrix2x2=MatrixNxN(-2.5,6.6,0.66,3.4)
	matrix4x4=MatrixNxN(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
	
	#matrix5x5 --> matrixNxN   , N->Inf
	print(matrix2x2)


	a=MatrixNxN(1,2,3,4,5,6,7,8,9)
	b=MatrixNxN(1,2,3,4,5,6,7,8,9)
	c=a.add(b)
	c=a+b
	c.display()
	print(c)
	f=a*b
	f.display()
	print(f)

	a+=b
	print(a)
	a+=5
	print(a)


	a=a+5
	print(a)
	a=a-99
	print(a)
	a=a-c
	print(a)
	a-=4
	print(a)
	c-=b
	print(c)

	c-=b+55
	c.display()

	c=b*7
	print(c)
	c*=7
	print(c)


if __name__=='__main__':
	main()



