import bpy
import os
import sys
import threading
import time

# Import the ScreenShareCamera class from the current directory
from screen_share import ScreenShareCamera

# ... (rest of your imports)
# ... (your other classes and functions)

def register():
    showTxt("register")
    global fsw

    # Reload the screen_share module to ensure changes are reflected
    import screen_share
    import importlib
    importlib.reload(screen_share)

    # Now import ScreenShareCamera again
    from screen_share import ScreenShareCamera  

    fsw = flask_server_wrapper()

    # ... (rest of the register function remains the same)
