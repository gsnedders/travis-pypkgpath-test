from __future__ import print_function

from os.path import abspath, join, dirname

import py

start = abspath(join(dirname(__file__), "foo", "bar.py"))

path = py.path.local(start)

def isimportable(name):
    if name and (name[0].isalpha() or name[0] == '_'):
        name = name.replace("_", '')
        return not name or name.isalnum()

pkgpath = None
for parent in path.parts(reverse=True):
    print()
    print("parent: %s" % parent)
    if parent.isdir():
        print("isdir")
        if not parent.join('__init__.py').exists():
            print("__init__.py doesn't exist")
            break
        if not isimportable(parent.basename):
            print("isn't importable")
            break
        pkgpath = parent

print()
print("pkgpath: %s" % pkgpath)
