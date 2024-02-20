'''class car:
    def __init__(self,year,speed):
        self.speed=speed
        self.year=year
    def getSpeed(self):
        print('122mph')
        print(self.speed)
        print(self.year)
    def setSpeed(self, speed ):
        self.speed=speed
        print(self.speed)
        
        
      
        

BMW= car(2018,100)
BMW.getSpeed()
BMW.setSpeed(200)

class Sedan(car):#child class
    def accelerate(self):
        print('123')
    def opentrunk(self):
        print('trunk has been opened')
            
class Svm(car):#child class
    def accelerate(self):
        print('365')

h=Sedan(2018,150)

h.accelerate()
r=Svm(2018,150)
r.accelerate()'''

'''from threading import *
class MyThread(Thread):
    def run(self):
        for i in  range(5):
            print("this is child class")
t=MyThread()
t.start()
for i in range(4):
    print("\n parent thraed")'''
'''from threading import *
class Demo:
    def show(self):
        for i in range(2):
            print("child class")
d=Demo()
t=Thread(target=d.show())
t.start()
for i in range(4):
    print("\n parent thraed")'''

from threading import*
import time
class Demo:
    def num(self):
        for i in range(1,6):
            print("the number is:",i)
            time.sleep(10)
    def double(self):
        for i in range(1,5):
            print(2*i)
    def square(self):
         for i in range(1,5):
            print(i*i)
d=Demo()
d.num()
d.double()
d.square()


        






