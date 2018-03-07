#!/usr/bin/python
import sys

print("Coming through stdout")
# stdout is saved
save_stdout = sys.stdout

fh = open("test.txt","w")
