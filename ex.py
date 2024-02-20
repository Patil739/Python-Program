import threading
import os

def hello(n):
    print(f"Hi{name}!")
def bye (name):
    print(f"bye{name}!")

if __name__== "__main__":
    t1=threading.Thread(target=hello,args=("yash",))
    t2=threading.Thread(target=bye,args=("yash",))


    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done!")
