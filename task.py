#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
from Matrix2x2 import represent2𝑥2matrice as Matrix
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.RED)
print(Back.CYAN)
print(Style.DIM)

matrix_1 =Matrix(4 ,5 ,6 ,7)
matrix_2 =Matrix(2 ,2 ,2 ,1)
#matrix_3 =Matrix() //null matrix

#print(Matrix.display(matrix_3))
print('-------Matrix 1-------\n')

print(Matrix.display(matrix_1))
print('\n-------Matrix 2-------\n')
print(Matrix.display(matrix_2))
print('\n-------Matrix 3---"+ operator"----\n')
matrix_3=matrix_1+matrix_2
print(Matrix.display(matrix_3))
print('\n-------Matrix 4---.add()----\n')

matrix_4=matrix_3.add(matrix_2)
print(Matrix.display(matrix_4))
print('\n---display instance using __str__--\n')
print(matrix_4)

print('\n-------Matrix 5---".prod()"----\n')
matrix_5=matrix_1.prod(matrix_2)
print(matrix_5)

print('\n-------Matrix 5---" * operator"----\n')
matrix_6=matrix_1*matrix_2
print(matrix_6)









