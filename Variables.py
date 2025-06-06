#Variable , When we assign a value to a variable , system will get a memory and a address is assigned to that varaible
a=10
print(id(a))  #to print address  #140706150206168
b=a # now i am assigning value 10 to b , So the value of a and b are same , So in python the variable and b point to same address where value 10 is stored
# to check this we can print the address of a and b
print(id(b))  #140706150206168  #here the address is same , means when the value is same then the variable will point to same address
c=10
print(id(c))  #140706150206168 this also same
print(id(10)) # 140706150206168 here the address is not based on variable , it is based on value
#now i will change the value of a
a=11
print(id(a))  #140706150206200
#as we changed a will it effect B ?
print(id(b))  #140706150206168  # it is still referring to value 10
#now i will change value of b and c
b=13; c=14; print(id(b)) #140706150206264 # the address of the variable b changed as the value changed
print(id(c))#140706150206296 #the address of the variable b changed as the value changed
#Do we have value 10 in memory ?
print('address')
print(id(10))  #140706176223960  , We still have value of 10 in memory at this address  , which is not referred by anyone
# when ever you have a data and it will not be referred by any variable , then that will be garbage callected later
#Can you make variable constant ? (constant - the value of variable cannot be changed ) , in python we dont have constant , as the user can change the value of variable anytime
# to make a variable in constant the user can use Capital letter in variable name Example ABC=125
ABC=123
"""
#Datatypes
#NONE, Numeric, list ,tuple,set,string,Dictionary
#None , when nothing is specified the it is called as none
#Numeric (int,float,complex,bool)"""
a=10 # int
b=10.9 #float
#c=10+11j  #j means root of -1 , this is not working in pycharm
#complex datatype means  number + or - imaginary number(10j)
#can we change the datatype of a variable ? yes
print(int(b)) #10
print(type(b)) #<class 'float'>, because in print(int(b)) we are only printing the value of b by converting to make the value change we
# we need to assign the value
c=int(b)
print(type(c)) #<class 'int'>
print(float(a)) #10.0
#bool means TRUE or FALSE
d=c<b
print(c<b) #TRUE
print(type(d)) #<class 'bool'>
print(int(True)) #1
print(int(False)) #0

#Sequence
#list , Tuple , Set , String , Range , this comes under Sequence
#tuple , in tuple we cannot change the values
ls1=(10,12,14,14,15,'a','b') #when we use () brackets its taking as tuple
print(ls1) #(10, 12, 14, 14, 15, 'a', 'b')
print(type(ls1)) #<class 'tuple'>
print(ls1[1]) #12
# ls1[1]=19 # we cannot change values in tuple
print(ls1) #[21, 19, 31, 11, 11, 4, 'a', 'b']


#list # we change the values as needed
lst2=[21,24,31,11,11,4,'a','b'] #when we use square brackets its taking as list
print(type(lst2))  #<class 'list'>
print(lst2) #[21, 24, 31, 11, 11, 4, 'a', 'b'] #in  list the  data can be duplicate
lst2[1]=19 #we can change values in list
print(lst2) #[21, 19, 31, 11, 11, 4, 'a', 'b']

#set , Duplicate values are not allowed and the data is stored in the form of hash so order of data can vary every time
s={10,15,10,9,80,90,11,100}
print(s) #{80, 100, 90, 9, 10, 11, 15}
print(type(s)) #<class 'set'>
s={10,'aa',11,'aa',15,'ba'}
print(s) #{'aa', 'ba', 10, 11, 15}


#string , we  have string datatype , if you need character , we need to specify only 1 character assignment ex a='b' , this is a char  but in python this is also referred as string datatype itself
str1='hello'
print(str1) #hello
print(type(str1)) #<class 'str'>

#reputables, means you want to iterate the values from 1 to 50 then no need to specify manually 1 to 50 values , we cna use range function
#Range(Start,End,increment)
"""
x = range(3,6,2)
for i in x:
    print(i, x)
x=range(10)
"""
Dictionary  : USing Key we can fetch the data , Every value which we use is assigned to the key 
the Key should contain unique values 
"""
d={1:'hello',2:'bye'} #Key:value
print(d.keys())   #dict_keys([1, 2])
print(d.values()) #dict_values(['hello', 'bye'])
""" to fetch the value we need to use key instead of index number d[2] """
print(d[2])
e={'b':'ball','c':'cat','m':'monkey'}
print(e['b']) #ball
"""we can also use get function to do this """
print(e.get('b')) #ball















