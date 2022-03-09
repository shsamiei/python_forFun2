import threading
from threading import Thread

def f():
    print('current thread is: ' + threading.current_Thread().getName())

print(threading.currentThread().getName())

#Thread(target=f)
Thread(name='salam', target=f).start()
Thread(name='khoobi', target=f).start()
#Thread(target=f).start()