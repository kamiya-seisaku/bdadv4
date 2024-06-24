######## 2024/6/20 checked out from bdadv3/66afa65 (key in view3d working yay)#####
######## 2024/6/20 to add websock #######################

# This code is written for a Blender indie game project "Uncirtain Days"
# This code is published with the MIT license, as is, no support obligation.
# Kamiya Seisaku, Kamiya Kei, 2024
import bpy
# import sys
import os
import glob
from mathutils import Vector
# import asyncio
import websockets
# import json
from flask import Flask, send_file
from flask_socketio import SocketIO, emit
import threading

### global variables
key_input = ""

# Todo:
# 1 blender freezing issue
#   1.1 threading: want server to be conducting.  
#       1.1.1 give web server a thread. 
# 1 key message not comong to blender
# 1 web casting


class ModalTimerOperator(bpy.types.Operator):
    bl_idname = "wm.modal_timer_operator"
    bl_label = "ks game"
    path_util = None
    fsw = None

    def __init__(self):
        pass
        # self.fsw = flask_server_wrapper()

    def modal(self, context, event):
        self.key_handling(context, event, key_input)
        self.showTxt("ABC")
        return {'PASS_THROUGH'}

    def showTxt(self, txt):
        print(str(txt))
        text_obj_key = bpy.data.objects.get('ui.Text.key')
        text_obj_key.data.body = str(txt)

    def key_handling(self, context, event, key_input):
        return

    def execute(self, context):
        self.key_handling(context, event, key_input)
        self.showTxt("ABC")
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        return {'PASS_THROUGH'}

###############################################################################
# BLender menu/operator registration ##########################################
# Register ModalTimerOperator in layout menu ##################################
###############################################################################
# Define the "view" menu in the 3D Viewport
def menu_func(self, context):
    self.layout.operator(ModalTimerOperator.bl_idname, text=ModalTimerOperator.bl_label)

# Register and add to the "view" menu (required to also use F3 search "Modal Timer Operator" for quick access).
def unregister():
    bpy.utils.unregister_class(ModalTimerOperator)
    bpy.types.VIEW3D_MT_view.remove(menu_func)

def register():
    bpy.utils.register_class(ModalTimerOperator)
    bpy.types.VIEW3D_MT_view.append(menu_func)

# Todo: comment out [debug codes]
#register()
#bpy.ops.wm.modal_timer_operator()
#init_bricks()
#unregister()

if __name__ == "__main__":
    print("__name__==main")
    register()
    bpy.ops.wm.modal_timer_operator()
