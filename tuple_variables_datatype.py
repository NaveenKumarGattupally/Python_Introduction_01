#tuple is im mutable , we cannot change value
tup=(21,30,14,29)  #using () we specify its tuple
print(tup)
print(tup[1])  #30
#tup[1]=90 #TypeError: 'tuple' object does not support item assignment
print(tup.count(21)) # Count function counts the number of occurences ,here it count for 21 #1
print(tup)

#set is a collection of unique elements
s={1,8,9,1,25,90}
print(s) #{1, 8, 9, 90, 25} , set doest not follow sequence while storing . Set uses hash .the vale of 1 which it took only once
s1={8,9,11,15,90}
print(s.difference(s1))  # this will compare s with the value of s1 and store the value in S . It will give only the difference of s but not s1
#isdisjoint is uesd when you want to compare 2 sets and return false when few values matches , return ture if none match
x={'ba','aa','sa'}
y={'ba','ss','cc'}
print(x.isdisjoint(y))  #False # as the values ba is present in x and y
#is subset method , returns true if all the items present in u matches z
u={'a','b','l'}
z={'a','b','m','h','l'}
print(u.issubset(z)) #


