gipython
========

Trying to get IPython work with gevent

To install
-------------
    $ virtualenv ve
    $ . ve/bin/activate
    $ pip install -r requirements.txt
    $ ./gipython
    
    In [1]: import gtest
    
    In [2]: gtest.spawn(gtest.work)
    Out[2]: <Greenlet at 0x10287caf0: work>
    
    In [3]: gtest.wait()
    Hello
    Hello
