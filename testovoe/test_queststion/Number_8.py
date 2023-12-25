import threading

thread_1 = threading.Thread(target=print("suka"))
thread_2 = threading.Thread(target=print("sam_suka"))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
