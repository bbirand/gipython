#!/usr/bin/env python 
if __name__ == '__main__':
    import gevent.monkey
    gevent.monkey.patch_all()

    import sys
    print sys.version

    from IPython import start_ipython

    sys.exit(start_ipython())
