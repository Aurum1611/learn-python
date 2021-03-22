import threading

print(threading.current_thread().getName(),"\n")

if threading.current_thread() == threading.main_thread():
    print("MainThread")
else:
    print("Another Thread")
