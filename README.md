gipython
========

Trying to get IPython work with gevent..

# To install with system Python
    $ virtualenv ve
    $ . ve/bin/activate
    $ pip install -r requirements.txt
    $ ./gipython

## Expected output
    In [1]: import gtest
    
    In [2]: gtest.spawn(gtest.work)
    Out[2]: <Greenlet at 0x10287caf0: work>
    Hello
    Hello

## Observed output
    
    In [1]: import gtest
    
    In [2]: gtest.spawn(gtest.work)
    Out[2]: <Greenlet at 0x10287caf0: work>
    
    In [3]: gtest.wait()
    Hello
    Hello

# For Anaconda Python distribution

I tried the same with the `gipython_anacond.py` file, but I still don't get
the proper behavior of the `Hello` lines printing without calling `wait()`.

