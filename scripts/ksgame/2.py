# This code is written for a Blender indie game project "Uncirtain Days"
# This code is published with the MIT license, as is, no support obligation.
# Kamiya Seisaku, Kamiya Kei, 2024
# ... (other imports)
from screen_share import ScreenShareCamera  # Import the ScreenShareCamera class
# ... (other imports)


# ... (Utility functions, ModalTimerOperator class, menu_func remain the same)



def register():
    showTxt("register")
    global fsw
    fsw = flask_server_wrapper()

    video_camera = ScreenShareCamera(0, 0, 800, 600)  # Adjust dimensions as needed
    
    # ... (rest of the register function remains the same)


def unregister():
    # ... (unregister function remains the same)


if __name__ == "__main__":
    register()
#   bpy.ops.wm.modal_timer_operator()
#   unregister()
