from threading import Thread

def fun1():
    while True:
        print("Working1")
def fun2():
    while True:
        print("Working2")

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)

t1.start()
t2.start()