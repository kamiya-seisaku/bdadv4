#main

import bpy
import os
import sys
dir = os.path.dirname(bpy.data.filepath) #Get directory of the .blend file
sys.path.append(dir) #Setting it as the python directory in the Blender Text editor 

from sub import sub

def testfunc():
    print("testfunc")
    
testfunc()
sub()
print(subtxt)
