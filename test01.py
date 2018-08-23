# https://proghub.ru/t/python-3-basic

#
print(list(range(3))[2])

#
class myClass:
   def func(self):
       print('hello')


obj = myClass()
obj.func()

obj = myClass()
myClass.func(obj)

#
class myClass:
   i = 0
   def __init__(self):
       i = 1


obj = myClass()
print(obj.i)

#
word = 'foobar'
print(word[3:] + word[:3])

#
list = []

for i in range(100):
    list.append(lambda x, i=i: x + i)

print(list[42](3))

#
a = [1, 2, 3]
if a[2] < 3:
   print(a[a[1]])
else:
   print(a[1])


#
list = []

for i in range(100):
    list.append(lambda x: x + i)

print(list[42](3))

#
def summ(arg1, arg2):
    return arg1 + arg2


tup = 1, 2
#print(summ(tup))
#error

#
a = 3
b = a
a = a + 2
print(b)

#
value = 0
#value = value > 0 ? 0 : 1  error
print(value)

#
fruits = {'apple', 'banana', 'apple'}
print(fruits)

#
x=2
y=3
def mult(x, y):
   return x * y


print(mult)