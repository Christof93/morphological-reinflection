# -*- coding: UTF-8 -*-
import codecs,sys

with codecs.open(sys.argv[1],"r","utf-8") as nn,codecs.open(sys.argv[2],"w","utf-8") as gold, codecs.open(sys.argv[3],"w","utf-8") as transl:
    for line in nn.readlines():
        line=line.split("\t")
        
        gold.write(" ".join(line[0])+"\n")
        transl.write(" ".join(line[2])+"\n")
