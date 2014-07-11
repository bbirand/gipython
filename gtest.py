from gevent import spawn, wait
import time
def work():
    while True:
        print "Hello"
        time.sleep(2)
