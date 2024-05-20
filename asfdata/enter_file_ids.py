#!/usr/bin/env python3
#
#
#  enter_file_ids - create a scene list file with the granule names for ASF download
#
#

import os
import sys

fids=open('fileids','r')
sceneids=fids.read()
fids.close()

scenelist = sceneids.split(',')
#print (scenelist)

fscenes=open('scenelist','w')
for scene in scenelist:
    print (scene)
    fscenes.write(scene+'\n')

fscenes.close()

