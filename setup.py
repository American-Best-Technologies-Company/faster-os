from setuptools import setup
from Cython.Build import cythonize
import platform

if platform.system() == 'Windows':
    setup(ext_modules=cythonize(
        "win/path.py",
        compiler_directives={
            'language_level': "3",
        },
    ))

else:

    setup(ext_modules=cythonize(
        "unix/path.py",
        compiler_directives={
            'language_level': "3",
        },
    ))
