import imp
import os
import sys

INTERP = "/usr/bin/python3"
if sys.executable != INTERP: 
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'start.py')
application = wsgi.app
