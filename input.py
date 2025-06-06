print('give the input of x')
x=input()  #9
y=input()  #10
print(x+y) #910 as the input considered as string format and it is appending
we need to convert string to int
print("enter the values of x and y")
x=int(input()) #9
y=int(input()) #10
print(x+y) #19

x=int(input('enter the number'))
y=int(input('Enter the 2nd number'))
z=x+y
print(z)

"""if you want to work with character """
x=input('enter a character ')  #here we can give a string and the system accepts
print(x) #hello
# but we only need character not string  , So try array
x=input('enter a character ')[0]
print(x) #h
#eval is a function which takes the input from uses and does operation(+,-,/...) and give the output
x=eval(input('enter an expression')) #2+3+4
print(x) #9

"if we need to take the input from command line , you need to import SYS "
import sys as s
x=int(s.argv[1])
y=int(s.argv[2])
print(x+y)  #this did not work as the command line path is incorrect for me

