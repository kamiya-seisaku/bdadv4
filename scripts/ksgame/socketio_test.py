#from Harry McKenzie at https://blender.stackexchange.com/questions/299995/frame-change-handler-called-on-mouse-press-and-release-event-when-scrubbing
import bpy
from pprint import pformat

print("1")

def uiText(new_text):
    text_object = bpy.data.objects['ui.Text.key']
    text_object.data.body = new_text

class FrameMouseHandler:
    print("FrameMouseHandler")
    def __init__(s):
        print("__init__")
        s.LMB_STATE_NONE = 0
        s.LMB_STATE_PRESS = 1
        s.LMB_STATE_RELEASE = 2
        s.LMB_STATE_DRAG = 3
        s.LMB_STATE_DRAG_RELEASE = 4
        s.frame = -1
        s.state = s.LMB_STATE_NONE

    def frame_get(s):
        print("frame_get")
        return s.frame

    def update_frame(s):
        print("update_frame")
        s.frame = bpy.context.scene.frame_current

    def update_state(s, state):
        print("update_state")
        s.state = state

    def update_handler(s, handler):
        print("update_handler")
        bpy.app.handlers.frame_change_post.clear()
        bpy.app.handlers.frame_change_post.append(handler)

    def reset(s):
        print("reset")
        s.update_handler(s.on_frame_press)
        s.update_state(s.LMB_STATE_NONE)

    def on_frame_change(s, scene, depsgraph):
        print("on_frame_change")
        print(f"s.state: {s.state}")
        uiText(f"s.state: {s.state}")
        prev_frame = s.frame_get()
        s.update_frame()
        if prev_frame == s.frame_get():
            if s.state == s.LMB_STATE_DRAG:
                print("Mouse stop scrubbing and release on frame:", s.frame_get())
            else:
                print("Mouse released on frame:", s.frame_get())
            s.reset()
        else:
            print("Mouse scrubbing, currently at frame:", s.frame)
            s.update_state(s.LMB_STATE_DRAG)

    def on_frame_press(s, scene, depsgraph):
        print("on_frame_press")
        s.update_frame()
        print("Mouse pressed on frame:", s.frame_get())
        s.update_handler(s.on_frame_change)
        s.update_state(s.LMB_STATE_PRESS)

        
handler = FrameMouseHandler()
print("handler set to FrameMouseHandler")
handler.reset()









#import bpy
#import websocket
#import json

#def on_message(ws, message):
#    try:
#        event_name, data = message.split(":", 2)  # Split on colon, max 2 splits
#        if event_name == 'server.js:emit-message':
#            print(f"Received message: {data}")
#            # Process data in Blender (e.g., bpy.ops.mesh.primitive_cube_add())
#    except ValueError:  
#        print(f"Unexpected message format: {message}")

#def on_error(ws, error):
#    print(f"Error: {error}")

#def on_close(ws, close_status_code, close_msg):
#    print("Connection closed")

#def on_open(ws):
#    print("Connected to server")

##def check_escape_key():
##    # Check for Escape key press (in Blender context)
##    for event in bpy.context.window_manager.events:
##        if event.type == 'ESC':
##            print("Escape key pressed. Terminating script.")
##            ws.close()  # Close WebSocket connection
##            return True  # Exit the function to prevent further execution
##    return False

#websocket.enableTrace(True) #Optional: add this line for more debugging info 
#ws = websocket.WebSocketApp("ws://localhost:3000",
#                           on_open=on_open,
#                           on_message=on_message,
#                           on_error=on_error,
#                           on_close=on_close)

## Start an event timer to check for Escape key periodically
##bpy.app.timers.register(check_escape_key)  

#ws.run_forever()  # Keep the connection open
