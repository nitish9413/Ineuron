# Q6
import multiprocessing
import time 
import random
import datetime

def processOne():
    print(f'Process_one_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Process_one_Endtime -> {datetime.datetime.now()}')
    
def processTwo():
    print(f'Process_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Process_two_Endtime -> {datetime.datetime.now()}')

def processThree():
    print(f'Process_two_Starttime -> {datetime.datetime.now()}')
    time.sleep(random.randint(1,5))
    print(f'Process_two_Endtime -> {datetime.datetime.now()}')
    
if __name__ == "__main__":    
    p1 = multiprocessing.Process(target=processOne)
    p2 = multiprocessing.Process(target=processTwo)
    p3 = multiprocessing.Process(target=processThree)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()