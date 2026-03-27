'''
Tuples are similar to lists
They are immutable
They are represented by ()
tuble is a iterable
'''

tp=67,90,81 #packing of a tuple

a,b=10,20 #unpacking of a tuple

def f1(a,b):
    a=a+10
    b=b+20
    return a,b

x=f1(10,20)
print(x)

#unpacking the list
x,y=f1(20,20)

print(x)
print(y)

s="hello"
s1=s
s="test"
print(s)
print(s1)

'''
If we want to pass multiple parameters 
as input then we use a *variable name 
in the parameters list

'*' is called expansion operator of tuple
'''
def add(a,b,*t):
    sum=a+b
    for i in t:
        sum+=i
    return sum

sum=add(9,4)
sum_multiple=add(9,4,3,2)
print(sum)
print(sum_multiple)
