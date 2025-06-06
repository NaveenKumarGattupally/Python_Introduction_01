"""
"Addition +, substraction, multiplication , division , "
x=10+2;y=10*2;z=10/2;
a=x+10;
print(a) #22
To assign multiple values
#a,b,c=3,4,9
print(a) #3
print(c) #9
unary operator , we can just give an operator before a number or variable
n=7
print(-n) #-7
c=-n
print(c) #-7
print(n<c) #flase
print(n==c) #false because n=7 and c=-7
print(c<=n) #True
print(c!=n) #Not equal to #True

logical operator , if we have two conditions and we want to compare them
p,q,r=10,13,16
print(p<11 and q>2 and r>10) #true
# For AND operator 1 1 gives 1 , 1 0 gives 0 ,0 1 gives 0 ,0 0 gives 0
# For OR operator 1 1 gives 1 , 1 0 gives 1 , 0 1 gives 1, 0 0 gives 0
# For NOT operator if the output is true it returns FALSE
x=True
y=not(x)
print(y)  #false  """


#number conversion , We can convert the number from decimal to binary , in decimal we have 10 as base(0,1,2....9) , in BINARY 2 as base  (1,0), in octal base is 8,hexa 16(0 to 9 ,a to f)
print(bin(25)) #0b11001 #here 0b means binary fromat
"""How to convert decimal to number divide the number with 2 for example 25 divide by  2 , first time 25/2 remainder is 1, then 12/2 remainder is 0,6 divided 2 remainder is 0 , then 3 divided by 2 remainder is 1  and coefficient is 1
25/2 ==> output is 12 remainder 1 , 12/2  output 6  remainder is 0, 6/2 output is 3 remainder is 0, 3/2 output 1 remainder 1 , now the binary digits are 11001( read the remainders from right to left )
"""
print(0b11001) #25
print(oct(25)) #0o31
print(hex(25)) #0x19
""""Bit wise operators ,complement ~ ,and  &, or  |,XOR ^, leftshift <<, right shift >> """
print(~12)  # reverse (00001100 is 12) then complement of 12 is 13 means reverse  11110011 that is ~13
# 13 in binary is 00001011 , once complement is 11110100(reverse ) , then twos complement is 11110100 +1 that is 11110111 means -13 , so the value of +12 and -13 are same
#output is -13
print(12&13) #12 #how ? 12 binary format and 13 binary format then the output is 12
print(12|13) #13

# XOR operation 0 0 gives 0, 1 0 gives 1, 0 1 gives 1, 1 1 gives 0
print(12^13) #1
print(10<<2) #left shift 2 bits 10 binary is 1010 and left shift two zeros to 10 tha is 101000 that is 40
print(10>>2) #mean right shift 1010 means 0010 that is 2










