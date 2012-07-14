"""
pass an output file from 'make VERBOSE=1' as the only argument to this script
example:
make VERBOSE=1 > test.txt
python clang_complete_generator.py test.txt

this script will then generate a .clang_complete config file for
the clang_complete plugin for vim
"""
import sys

includes = set([])
defines = set([])

f = open(sys.argv[1], "r")
for line in f.readlines():
    strippedLine = line.strip()
    words = strippedLine.split(" ")
    for word in words:
        if "-I" in word[:2]:
            includes.add(word)
        elif "-D" == word[:2]:
            defines.add(word)

f = open(".clang_complete", "w")

for e in includes:
    f.write(e + "\n")

for e in defines:
    f.write(e + "\n")
