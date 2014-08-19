import time
import gevent
from gevent import spawn, wait

def work():
    while True:
        print "Hello"
        gevent.sleep(1)
        #time.sleep(1)
