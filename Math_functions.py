"""We need to import the math function before using """
import math
x=math.sqrt(25)
print(x)  #5.0
""" ceil means rounding of means 2.5 is 2 , 2.9 means 3 , Floor means 2.5 means 2, 2.9 means 2"""
print(math.ceil(2.9))  #3
print(math.pow(3,2)) #9.0
print(math.pi) #3.141592653589793
"instead of using Math can we use M instead  use IMPORT MATH AS M "
import math as m
print(m.pi) #3.141592653589793
"if you need only few functions instead of all use  FROM MATH IMPORT SQRT,POW"
print(pow(2,2)) #4