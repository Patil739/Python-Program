'''class Number:
    def __init__(self,aa):
        self.a=aa
    def show(self):
        print('inside base class')
        print('the value of a:',self.a)
class Strings(Number):
    def __init__(self,str1,aa):
        self.str=str1
        Number.__init__(self,aa)
    def show1(self):
        print('inside derived class ')
        print('the value of str=',self.str)

a=Strings(100,'mp')
a.show1()
a.show()'''

'''def msg():
    print('no argu')
#def msg(a):
#   print('on argu')
#def mesg(a,b):
#   print('two argu')

msg()
#msg(1)
#msg(2,3)'''

'''class Demo:
    def __init__(self,a):
        self.a=a
    def __add__(self,obj):
       return self.a+obj.a
obj1=Demo(10)
obj2=Demo(30)
str1=Demo('lead')
str2=Demo('soft')

print(obj1+obj2)
print(str1+str2)'''

'''class student:
    branch='IT'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

a=student('mrunal',43)
b=student('sakshi',49)

print(a.name, sep=' ')
print(a.roll, end=' ')
print(b.name, sep =' ')
print(b.roll, end=' ')
print(a.branch)
print(b.branch)'''

'''from datetime import date
class Demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthyear(cls,year,name):
        return cls(name,date.today().year==year)
    @staticmethod
    def isAdult(age):
        return age>18

per=Demo('suraj',1999)
per1=Demo.fromBirthyear('suraj',1666)

print(per.age)
print(per1.age)
print(Demo.isAdult(17))'''

'''import sys
a=int(input('enter no:'))
b=int(input('enter no:'))

try:
    c=a/b
    print(a)

except:
    print('division by zero is not possible...')

finally:
    print('error occured')'''
'''class ValueTooSmall(Exception):
    'base'
    pass
class ValueToolarge(Exception):
    's'
    pass

n=10
while(True):
    try:
        temp=int(input('enter no:'))
        if (temp<n):
            raise ValueTooSmall
        elif(temp>n):
            raise ValueTOOlarge

    except ValueTooSmall:
        print('numb is to small')
        print()
    except ValueToolarge:
        print('numb is to large')
        print()'''

def write():
    roll=int(input('enter roll no'))
    name=input('enter name')
    mobileno=input('enter mob no')
    f=open('student.txt','a')
    f.write(str(roll)+name+mobileno)
    f.close()
    print('data writen to file successfully..')

write()
write()

def read():
    f=open('student.txt','r')
    print(f.readline())

read()
        
            

    

        
