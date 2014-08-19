#!/usr/bin/env python
# EASY-INSTALL-ENTRY-SCRIPT: 'ipython==2.2.0','console_scripts','ipython'
__requires__ = 'ipython==2.1.0'
import gevent.monkey
gevent.monkey.patch_all()

import sys
print sys.version

from pkg_resources import load_entry_point

sys.exit(
   load_entry_point('ipython==2.1.0', 'console_scripts', 'ipython')()
   )
