from __future__ import division
import sys

with open(sys.argv[1],"r") as t,open(sys.argv[2],"r") as r:
    test_lines=t.readlines()
    correct_lines=r.readlines()
    correct=len([t for test,gold in zip(test_lines,correct_lines) if test.split("\t")[2]==gold.split("\t")[2]])
    all=len(correct_lines)
    print correct
    print all
    print correct/all
