from Matrix import MatrixNxN
from colorama import init
from colorama import Fore, Back, Style

def main():
	init()
	print(Fore.RED)
	print(Back.CYAN)
	print(Style.DIM)


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


	a+=5
	print(a)


if __name__=='__main__':
	main()



