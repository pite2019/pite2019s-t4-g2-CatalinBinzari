from Matrix import MatrixNxN

def main():
	
	


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


if __name__=='__main__':
	main()



