# Introduction to python
# It is interpreted high level language , it is case sensitive
# Python Variables
2+3
#output is 5
x=2
# variable is a container where we are storing the data , which also has a unique address assigned to it
 #Variable means we can change the vales like i can assign x=3
print(x)
#output will be 3
#d=_+10
#if you want to use output of previous operation use underscore(but this did not work in pycharm)
a='hrithvik'
print(a + 'gattupally')
#you can append a string with another string using +
#how to fetch a character from a string , here variable a is assigned to 8 letters , now i need only character "v" in my output
b=a[5]
print(b)
#If I want to print the characters from right to left here print a[-1] will give output as "K"
c=a[-1]
print(c)
#if you want to print 2 characters [starting address:Ending address] here i want to start with r and end with h then i use [1:5]
d=a[1:5]
print(d)
#if you dont specify Ending address then it will pick all the characters till end , here output is rithvik
d=a[1:]
d=a[:4] #here the starting is r and ending with h
#Once the value is assigned it cannot be changes a[4]='s' Error : Str object does not support item assignment
#stings in python is immutable
#how to know the length of variable a
print(len(a))

#LIST
# to group number and strings together we use LIST,mutable(we can change the values)
nums = [12,50,11,'a','m',4]
print(nums) #[12, 50, 11, 'a', 'm', 4]
print(nums[1]) # 50
print(nums[2:5]) #[11, 'a', 'm']
print(nums[-2]) # m
names = ['abc','efg',a,6]
z=nums+names
print(z) #[12, 50, 11, 'a', 'm', 4, 'abc', 'efg', 'hrithvik', 6]
print(nums)
nums.insert(1,2) #[12, 2, 50, 11, 'a', 'm', 4] #index will add the value in between
print(nums)
print(nums.count(4))   #1
nums.append('a') #[12, 2, 50, 11, 'a', 'm', 4, 'a']
print(nums) #append will add the data at end of the list
nums.reverse()
print(nums) #['a', 4, 'm', 'a', 11, 50, 2, 12]
print(nums.__len__()) #8
print(nums.__contains__(4))   #true
nums.remove(50)
print(nums)  #['a', 4, 'm', 'a', 11, 2, 12]
nums.pop(-2) #based on index number we are deleting  , if we say pop() and dont specify value the last element will be removed
#['a', 4, 'm', 'a', 11, 12]
del nums[-1] #['a', 4, 'm', 'a', 11]
print(nums)
nums.append(5)
print(nums)
nums3=['v','g','a','m']
nums2=['v','h','r','a']
print(nums3)
nums2.sort(reverse=False) # reverse fales means sort in assending order #['a', 'h', 'r', 'v']
print(nums2)
nums3.sort(reverse=True) # Reverse True means Decending order #['v', 'm', 'g', 'a']
nums4=['la','bammma','fabb','bba','zx']
nums4.sort(key=len) #['la', 'zx', 'bba', 'fabb', 'bammma']
print(nums4)
nums4.clear() #[]
#if you want to add multiple values use Extend
nums4=['cba','mca',1,'qui']
nums4.extend([4,2])  #_iterable in syntax means we should use [] # 4,2 will be added to the end of list
print(nums4)
print()  #




