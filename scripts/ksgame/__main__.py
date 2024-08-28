# [Todo]
#  1 [pub] publih poc.
#    1.1 [pub] score.
#      1.1 [pub] note sequence.
#    1.1 [pub] brick reaction.
#    1.1 [pub] installation guide.
#    1.1 [pub] now make a video.
#  1 [Issue] capture from blender window not screen
#  1 [Issue] initially chrome key not working until clicked in blender 
# [Ideas]
#  1 servant/maid cafe shop clening game
#  1 music game
#  1 dance input/whistle input/air drums input/sequencer/fan copy
#  1 scene ideas/fan copy games from music videos(miku miku beam,soul soup,universe,tokyo flash,time paradox)
# [Done]
#  1 [Issue] blender key only partially working 

# This code is written for a Blender indie game project "Uncirtain Days"
# This code is published with the MIT license, as is, no support obligation.
# Kamiya Seisaku, Kamiya Kei, 2024

import bpy
import os
# import glob
# import os
import sys
import threading
dir = os.path.dirname(bpy.data.filepath)
libdir = os.path.join(dir, "scripts", "ksgame")
sys.path.append(libdir)

import importlib
import flask_server
importlib.reload(flask_server)
from flask_server import flask_server_wrapper
import shared_stuff as sf
import keymap as km
from screen_share import ScreenShareCamera
from animator import animatable_object

## Utilities ##################################################################
previous_txt = ""
previous_frame = 0

def showTxt(txt):
    global previous_txt
    global previous_frame
    text_obj_system = bpy.data.objects.get('ui.Text.system')
    text_obj_system.data.body = str(txt)
   
    if bpy.data.scenes[0].frame_current - previous_frame >= 1:
        print(str(txt))
    previous_frame = bpy.data.scenes[0].frame_current

# key_sm: key handling state machine
# Receives:
#  input_key: 'A', 'D'
# Returns:
#  input_key, only if it is a non-repeated key input
previous_input_key = ""
def key_sm(input_key): #key handling state machine
    global previous_input_key

    if input_key == "":
        previous_input_key = ""
        return ""
    else:
        if previous_input_key == input_key:
            previous_input_key = ""
            return ""
        else:
            previous_input_key = input_key
            current_frame = bpy.context.scene.frame_current
            if current_frame%1: #avoid repeats by resetting input_key every 10 frames
                input_key = ""
            return input_key

## modaltimer #############################################################
class ModalTimerOperator(bpy.types.Operator):
    bl_idname = "wm.modal_timer_operator"
    bl_label = "ks game"
    global fsw #flask server wrapper class

    def __init__(self):
        pass

    def modal(self, context, event):
        if isinstance(event, bpy.types.Event) == False:
            return {'PASS_THROUGH'}

        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}

        #HUD updates-------------------------------------------------
        text_obj_fn = bpy.data.objects.get('ui.Text.FN')
        current_frame = bpy.context.scene.frame_current
        text_obj_fn.data.body = str(f"FN:{current_frame}")

        self.move_focus(context, event, "")
        current_frame = bpy.context.scene.frame_current

        bpy.context.view_layer.update()
        # Redraw viewport (optional but recommended)
        if current_frame % 2:
            bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        #Story
        chat_text = bpy.data.objects.get('chat_text')
        chat1 = bpy.data.objects.get('chat1')
        if 30 <= current_frame < 50:

            self.set_visibility('chat1', "True")
            bpy.context.scene.update_tag()
            serif = [
                "今日は多いなー",
                "ドーナツ"
            ]
            chat_text.data.body = str('\n'.join(serif))
        elif 50 <= current_frame < 100:
            serif = [
                "こんなに取れっかな",
                "オラ自信ねえゾ"
            ]
            chat_text.data.body = str('\n'.join(serif))
        elif 100 <= current_frame < 120:
            chat_text.data.body = ""
        elif 120 <= current_frame < 123:
            self.set_visibility('chat1', "False")
        elif 130 <= current_frame < 135:
            self.set_visibility('chat1', "True")
            serif = [
                "取り損ねたドーナツは",
                "食べ終わったオニギリのごとし・・・"
            ]
            chat_text.data.body = str('\n'.join(serif))
       
        #Key input handling -----------------------------------------
        if sf.key_input_g in {'A', 'D'}:
            self.key_handling(context, event, sf.key_input_g)
            return {'PASS_THROUGH'}

        if event.type in {'A', 'D'}:
            sf.key_source_g = "blender event"
            sf.key_input_g = event.type
            self.key_handling(context, event, event.type)
            return {'PASS_THROUGH'}

        bpy.context.view_layer.update()

        return {'PASS_THROUGH'}

    def set_visibility(self, obj_name, state):
        obj = bpy.data.objects.get(obj_name)
        if state == "Toggle":
            is_visible = not obj.hide_viewport  # Toggle based on current state
        elif state == "True":
            is_visible = False  # Force visible
        elif state == "False":
            is_visible = True   # Force hidden
        else:
            print(f"Invalid state: {state}. Use 'True', 'False', or 'Toggle'.")
            return  # Exit the function if the state is invalid

        obj.hide_viewport = is_visible
        obj.hide_render = is_visible
        bpy.context.view_layer.update()

        print(f"Object '{obj.name}' visibility set to: {not is_visible}")


    def move_bike(self, context, event, key_input):
        bike_mover = animatable_object('bike-mover') 
        if key_input == 'A':
            if bike_mover.location.x < 4:
                bike_mover.location.x += 0.5
        if key_input == 'D':
            if bike_mover.location.x > 0:
                bike_mover.location.x -= 0.5

    def move_focus(self, context, event, key_input):
        showTxt("in move_focus1")

        # debug
        focus = bpy.data.objects.get('focus')
       
        frame_index = int(bpy.context.scene.frame_current / 30) % (16*5)
        song = [4, 3, 2, 1, 1, 2, 3, 4, 0, 2, 1, 2, 0, 1, 2, 0, 0, 3, 0, 4, 0, 3, 4, 3, 2, 1] * 5
        interval = -4.0
        offset = 0

        focus.location.x = song[frame_index ] - 0
        focus.location.y = offset + frame_index * interval
        focus.location.z = 4
        bpy.context.view_layer.objects.active = focus
        return

    def key_handling(self, context, event, key_input):
        sf.key_input_g = ""
        processed_key = key_sm(key_input)
        if processed_key == "":
            return

        self.move_bike(context, event, key_input)
       
        # donut hit ###############################################
        # Scoring logic
        frame_index = bpy.context.scene.frame_current % 32
        song = [4, 3, 2, 1, 1, 2, 3, 4, 0, 2, 1, 2, 0, 1, 2, 0, 0, 3, 0, 4, 0, 3, 4, 3, 2, 1] * 5
        interval = -4.0
        offset = -2.0

        x = song[frame_index] - 2
        y = offset + frame_index * interval
        z = 4

        # Check if player hit the correct note
        bike_mover = bpy.data.objects.get('bike-mover')
        focus = bpy.data.objects.get('focus')
        if abs(bike_mover.location.x - focus.location.x) < 0.25: 
            score_obj = bpy.data.objects.get('ui.Text.score')
            score_obj["score"] += 1
            showTxt("score +1")
        return

    def execute(self, context):
        km.set_obj_select_keymap("off")

        sf.key_source_g = ""
        sf.key_input_g = ""

        global previous_txt
        global previous_frame
        previous_txt = ""
        previous_frame = 0
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
        bpy.ops.screen.animation_play() # Play active scene animation
    
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        km.set_obj_select_keymap("on")
        bpy.app.handlers.frame_change_post.remove(self.modal)
        unregister()
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
    # video_camera = ScreenShareCamera(0, 0, 800, 600)  # Adjust dimensions as needed

    # Start the web server in a separate thread
    threading.Thread(
        target=fsw.socketio.run,
        args=(fsw.app, '0.0.0.0', 6999),
        kwargs={
            'allow_unsafe_werkzeug': True,
            'debug': False,
        }  # For development purposes
    ).start()
    # fsw.socketio.run(fsw.app, host='0.0.0.0', port=6999, debug=False) #non-threaded version

    bpy.utils.register_class(ModalTimerOperator)
    bpy.types.VIEW3D_MT_view.append(menu_func)

# Todo: comment out [debug codes]
#register()
#bpy.ops.wm.modal_timer_operator()
#init_bricks()
#unregister()

if __name__ == "__main__":
    register()
#  bpy.ops.wm.modal_timer_operator()