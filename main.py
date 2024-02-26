
import threading
import time

def sorting():
    zoznam.sort()
    print(zoznam)

def sorting_revers():
    zoznam.sort(reverse=True)
    print(zoznam)


zoznam = [11,2,45,87,29,5,2,78,45,103,4451,12,78899]
print(f"Zoznam cisel{zoznam}")

start_time=time.time()

thread1=threading.Thread(target=sorting(),args=("Vlakno1 bezi",))
thread2=threading.Thread(target= sorting_revers(),args=("vlakno 2 bezi",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

duration=time.time() -start_time