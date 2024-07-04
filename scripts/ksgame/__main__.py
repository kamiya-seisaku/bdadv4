# This code is written for a Blender indie game project "Uncirtain Days"
# This code is published with the MIT license, as is, no support obligation.
# Kamiya Seisaku, Kamiya Kei, 2024
import bpy
import os
import glob
#from flask_socketio import SocketIO, emit
#import threading
import os
import sys
import threading
dir = os.path.dirname(bpy.data.filepath)
libdir = os.path.join(dir, "scripts", "ksgame")
sys.path.append(libdir)

from flask_server import flask_server_wrapper
import shared_stuff as sf

## Utilities ##################################################################
previous_txt = ""

def showTxt(txt):
    global previous_txt
    if previous_txt == txt:
        return
    previous_txt = txt
    print(str(txt))
    text_obj_system = bpy.data.objects.get('ui.Text.system')
    text_obj_system.data.body = str(txt)    

## modaltimer #############################################################
class ModalTimerOperator(bpy.types.Operator):
    bl_idname = "wm.modal_timer_operator"
    bl_label = "ks game"
    global fsw #flask server wrapper class

    def __init__(self):
        pass

    def modal(self, context, event):
        current_frame = bpy.context.scene.frame_current
        if isinstance(event, bpy.types.Event) == False:
            return {'PASS_THROUGH'}

        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}

        if sf.key_input_g in {'A', 'D'}:
            showTxt(f'in ModalTimerOperator/modal/if sf.key_input_g in A, D: sf.key_input_g = {sf.key_input_g}')
            self.key_handling(context, event, sf.key_input_g)
            return {'PASS_THROUGH'}

        if event.type in {'A', 'D'}:
            sf.key_source_g = "blender event"
            sf.key_input_g = event.type
            self.key_handling(context, event, sf.key_input_g)
            return {'PASS_THROUGH'}

        return {'PASS_THROUGH'}

    def key_handling(self, context, event, key_input):
        showTxt(f"in key_handling: key_input(arg of key_handling)= {key_input}")
        bike_mover = bpy.data.objects.get('bike-mover')
        text_obj_toggle = bpy.data.objects.get('ui.Text.toggle')
        text_obj_fn = bpy.data.objects.get('ui.Text.FN')
        if text_obj_toggle.data.body == str(f"bike_mover is moving"):
            # bike_mover["is_moving"] = False
            text_obj_toggle.data.body = str(f"bike_mover is not moving")
        else:
            # bike_mover["is_moving"] = True
            text_obj_toggle.data.body = str(f"bike_mover is moving")
            et = event.type
            frame_number = bpy.context.scene.frame_current
            # to show the score in the 3D view, the body of the ui text object
            # is set according to the same object's custom property "score"
            text_obj_fn.data.body = str(f"FN:{frame_number}")
            # key event handling
            if key_input == 'A':
                if bike_mover.location.x < 1:
                    bike_mover.location.x += 0.5
            if key_input == 'D':
                if bike_mover.location.x > -1:
                    bike_mover.location.x -= 0.5
            bpy.context.view_layer.objects.active = bike_mover #Need this to make location changes into blender data
            bpy.context.view_layer.update() #Need this for the change to be visible in 3D View
            
        return

    def execute(self, context):

        bike_mover = bpy.data.objects['bike-mover']
        bike_mover.location = [0, 0, 0]
        bpy.context.view_layer.objects.active = bike_mover #Need this to make location changes into blender data
        bpy.context.view_layer.update() #Need this for the change to be visible in 3D View

        wm = context.window_manager
        bpy.app.handlers.frame_change_post.append(self.modal)
        wm.modal_handler_add(self)

        bpy.context.window.workspace = bpy.data.workspaces['Scripting'] # Switch blender UI to modeling workspace

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
        bpy.app.handlers.frame_change_post.remove(self.modal)
        unregister()
#        self.fsw.socketio.stop()
        # wm = context.window_manager
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
    showTxt("unregister")
    global fsw
    fsw.socketio.stop()
    bpy.utils.unregister_class(ModalTimerOperator)
    bpy.types.VIEW3D_MT_view.remove(menu_func)

def register():
    showTxt("register")
    global fsw
    fsw = flask_server_wrapper()
    # Start the web server in a separate thread
    threading.Thread(
        target=fsw.socketio.run,
        args=(fsw.app, '0.0.0.0', 3000),
        kwargs={'allow_unsafe_werkzeug': True}  # For development purposes
    ).start()

    bpy.utils.register_class(ModalTimerOperator)
    bpy.types.VIEW3D_MT_view.append(menu_func)

# Todo: comment out [debug codes]
#register()
#bpy.ops.wm.modal_timer_operator()
#init_bricks()
#unregister()

if __name__ == "__main__":
    register()
#    bpy.ops.wm.modal_timer_operator()
