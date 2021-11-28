'''
Created on 4 Oct. 2021

@author: praka
'''
import time
import multiprocessing as mp

def square(list1):
    print("Calculate square numbers:\n")
    for x in list1:
        time.sleep(0.5)
        print("Square of "+ str(x) + " is " + str(x*x) + "\n")
        #print("Square process is assigned to " + threading.current_thread().name + "\n")
        
        
def cube(list1):
    print("\nCalculate cube numbers:\n")
    for x in list1:
        time.sleep(0.5)
        print("Cube of "+ str(x) + " is " + str(x*x*x) + "\n")
        #print("Cube process is assigned to " + threading.current_thread().name + "\n")
        
list1 = [1, 2, 3, 4, 5]

t = time.time()
#square(list)
#cube(list)

#print("Main thread is " + threading.main_thread().name + "\n")
p1 = mp.Process(target=square, args=(list,))
p2 = mp.Process(target=cube, args=(list,))

p1.start()
p2.start()

p1.join()
p2.join()

print("\nTime taken for this execution is " + str(time.time() - t) )