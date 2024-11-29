import time
import multiprocessing

def Print_Numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Numbers : {i}")

def Print_Letters():
    for i in "abcde":
        time.sleep(1.5)
        print(f"Numbers : {i}")


if __name__ == "__main__":

    t1 = multiprocessing.Process(target=Print_Numbers)
    t2 = multiprocessing.Process(target=Print_Letters)


    t = time.time()
    t1.start()
    t2.start()

    t1.join()
    t2.join()


    # Print_Numbers()
    # Print_Letters()
    Current_time = time.time()-t
    print(Current_time)

