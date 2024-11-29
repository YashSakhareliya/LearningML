import time
import threading

def Print_Numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers : {i}")

def Print_Letters():
    for i in "abcde":
        time.sleep(2)
        print(f"Numbers : {i}")

t1 = threading.Thread(target=Print_Numbers)
t2 = threading.Thread(target=Print_Letters)


t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()


# Print_Numbers()
# Print_Letters()
Current_time = time.time()-t
print(Current_time)

