#!/usr/bin/env python
# -*- coding:utf-8 -*-
#py:v2.7

import os
import sys
import random
import tinify

tinify.key = random.choice(["CA30EQeQMcnrVt8Y4Gk4YilSsnJ5OJ7G"])
Const_Image_Format = [".jpg",".jpeg",".png"]

class FileFilt:
    fileList = []
    def __init__(self):
        pass
    def FindFile(self,pathh):
        global Const_Image_Format
        for root, dirs, files in os.walk(pathh):
            for file in files:
                lfile = os.path.join(root,file)
                if os.path.splitext(lfile)[1] in Const_Image_Format:
                    self.fileList.append(lfile)

def ComPress(filename):
    source = tinify.from_file(filename)
    source.to_file(filename)
    print "本月此key已用压缩次数:" + str(tinify.compression_count)

if __name__ == "__main__":
    b = FileFilt()
    b.FindFile(pathh = sys.argv[1])
    #print(b.counter)
    #print b.fileList
    if len(b.fileList) > 0:
        for k in b.fileList:
            #print k
            ComPress(k)
    else:
        print "无文件需要压缩!"
