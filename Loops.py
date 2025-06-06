"we want system to decide the output based on the code so we use loops like if ..."
from tokenize import endpats

x=0
y=20
if (x==12):
    print("the value is less")
elif(x==12):
    print("the value is greater")
elif(x==12):
    print("the value is equal")
else:
    print("The value is not less, greater ,equal")

Loops : to repeat statements
a=1
while(a<5):
    print('Hello',end="")
    a=a+1
    b=1
    while(b<5):
        print('Team',end='')
        b=b+1

    print()

"for loop , we follow the sequence "
x='hello'   #this is only taking input as string
for i in x:
    print(i)

x=int(5)
print(x)
for i in range(4,20,6):   #4 10 16  , Start the value with 4 increment 6 (o/p 10) , then increment 6 (o/p 16) then increment 6 - end of data
    print(i)

"I want the values which are divisible by 2 should not be printed "
print('hi')
for i in range(10):
    if(i%2!=0):
        print(i,end='')   #13579

x=int(input('How many candies you need'))
i=1
max1=9
while i<=x:
    if(x>max1):
        print('we dont have that many candies')
        break
    else:
        print('candies  ',end='')
        i+=1
        
for  i in range(10):
    if(i%3==0 or i%5==0) :  #output 12478
        continue   #Continue will skip the remaining line in the loop and go to next step/loop
        print('the value is equl') #we are asking this statement to skip
    print(i,end='')
    i+=1

#Pass , i dont want to print odd numbers
for i in range(20):
    if(i%2==0):
        print(i,end='')
    else:
        pass   # to pass this block - means ignores this block
print('finished pass')    #024681012141618finished pass

prev1=0
prev2=1

for i in range(10):
    if(i>1):
       current=prev1+current
       prev1=prev2
       prev2=current
       print(current)
    elif(i==0):
        current=i
        print(i)
    elif(i==1):
        current=i
        print(i)










