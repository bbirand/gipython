import time
from gevent import spawn, wait

def work():
    while True:
        print "Hello"
        time.sleep(1)
