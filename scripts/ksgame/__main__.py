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

# Todo:
# 1 blender freezing issue
#   1.1 threading: want server to be conducting.  
#       1.1.1 give web server a thread. 
# 1 key message not comong to blender
# 1 web casting

class flask_server_wrapper:
    print("flask_server_wrapper")
    
    app = Flask(__name__)
    socketio = SocketIO(app)
    key_input = None

    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('message')
    def handle_message(message):
        print(f'Received message {message}')
        key_input = ''  # Reset key input
        if message[0:7]=='keyup':
            key_input = ''
        elif message[0:7]=='keydown:':
            if message[8:9]=='d':
                key_input = 'D'
            elif message[8:9]=='a':
                key_input = 'A'

    @app.route('/')
    def index():
        return send_file('../../public/index.html')

class ModalTimerOperator(bpy.types.Operator):
    bl_idname = "wm.modal_timer_operator"
    bl_label = "ks game"
    path_util = None
    fsw = None

    def __init__(self):
        self.fsw = flask_server_wrapper()

    def modal(self, context, event):
        current_frame = bpy.context.scene.frame_current

        # Avoids "AttributeError: 'Depsgraph' object has no attribute 'type'" when mouse cursor is not in 3D view
        if isinstance(event, bpy.types.Event) == False:
            return {'PASS_THROUGH'}

        # 2024/6/9 omit old keyhandling for now ##########################
        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}

        # Todo: need repeated key event handling: pass event while action "brick_hit" is playing in nla (getting better but not perfect)
        # Add and play action "brick_hit" at the scene frame when the bike hits the brick (object distance < threshold)
        if self.fsw.key_input in {'A', 'D'}:
            key_input = self.fsw.key_input
            self.key_handling(context, event, key_input)
            return {'PASS_THROUGH'}

        if event.type in {'A', 'D'}:
            key_input = event.type
            self.key_handling(context, event, key_input)
            return {'PASS_THROUGH'}

        return {'PASS_THROUGH'}

    def key_handling(self, context, event, key_input):
        # Check if the bike is already moving
        # if moving skip the key event handling
        # (without imprementing this socond side move happens in the next frame)
        bike_mover = bpy.data.objects.get('bike-mover')
        text_obj_key = bpy.data.objects.get('ui.Text.key') # get ui text object for key event capture display
        text_obj_fn = bpy.data.objects.get('ui.Text.FN') # get ui text object for frame number display
        # if bike_mover["is_moving"]: # not clear how bike mover custom properties are changing, lets instead use ui_text
        if text_obj_key.data.body == str(f"bike_mover is moving"):
            # bike_mover["is_moving"] = False
            text_obj_key.data.body = str(f"bike_mover is not moving")
        else:
            # bike_mover["is_moving"] = True
            text_obj_key.data.body = str(f"bike_mover is moving")
            et = event.type
            frame_number = bpy.context.scene.frame_current
            # to show the score in the 3D view, the body of the ui text object
            # is set according to the same object's custom property "score"
            text_obj_fn.data.body = str(f"FN:{frame_number}")
            # key event handling
            if et == 'A':
                if bike_mover.location.x < 1:
                    bike_mover.location.x += 0.5
            if et == 'D':
                if bike_mover.location.x > -1:
                    bike_mover.location.x -= 0.5
            bpy.context.view_layer.objects.active = bike_mover #Need this to make location changes into blender data
            bpy.context.view_layer.update() #Need this for the change to be visible in 3D View

        # self.path_util.update_path_bricks(bpy.context.scene.frame_current)
        return

    def execute(self, context):
        #start the web server in a separate thread
        threading.Thread(target=self.fsw.socketio.run, args=(self.fsw.app, '0.0.0.0', 3000)).start()
        # socketio.run(app, host='0.0.0.0', port=3000)

        bike_mover = bpy.data.objects['bike-mover']
        bike_mover.location = [0, 0, 0]
        bpy.context.view_layer.objects.active = bike_mover #Need this to make location changes into blender data
        bpy.context.view_layer.update() #Need this for the change to be visible in 3D View

        wm = context.window_manager
        bpy.app.handlers.frame_change_post.append(self.modal)
        wm.modal_handler_add(self)

        bpy.context.window.workspace = bpy.data.workspaces['Modeling'] # Switch blender UI to modeling workspace

        # Switch 3D view shading to rendered
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.spaces[0].shading.type = 'RENDERED'

        score_obj = bpy.data.objects.get('ui.Text.score')
        score_obj["score"] = 0 # Reset game score
        # score = score_obj["score"] # Reset game score
        # score = 0
        bpy.ops.screen.animation_play() # Play active scene animation
 
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        self.fsw.socketio.stop()
        # wm = context.window_manager
        # bpy.app.handlers.frame_change_post.remove(self.modal)
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
register()
bpy.ops.wm.modal_timer_operator()
#init_bricks()
#unregister()

if __name__ == "__main__":
    register()
    bpy.ops.wm.modal_timer_operator()
