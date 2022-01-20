from os import *
import platform

if platform.system() == 'Windows':
    from win.path_py import *
elif platform.system() == 'Darwin':
    from unix.path_py import *
else:
    from unix.path_py import *