#!/usr/bin/python
import os
import pprint
import sys

print('Content-Type: text/plain\n\nHello World!')

print('\nEnvironment:')
pprint.pprint(dict(os.environ))

print('\nInput:')
print(sys.stdin.read())
