"""Continue :  if i want to skip the value for example when the value is 3 it should skip"""

for i in range(5):
    print('hello',i,end=' ')   #hello 0 hello 1 hello 2 hello 3 hello 4

#to skip when the value is 3 using continue
for i in range(5):
    if(i==3):
        continue
    print('hello',i,end=' ')  #hello 0 hello 1 hello 2 hello 4

#Break we use Break if you want to exit when the condition is met , when the value meets 3 then the loop is skipped , for example from 3 till end it will not print

for i in range(5):
    if(i==3):
        break
    print('hello',i,end=' ')   #hello 0 hello 1 hello 2

#Pass - we use when we define a dummy function and we want that to be used for alter, in the below function nothing is defied for FUN1 , we want it to be used for later.

def fun1():
    pass
print('hello')   #hello
