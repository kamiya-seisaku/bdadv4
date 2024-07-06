# ... other imports
from screen_share import ScreenShareCamera


class flask_server_wrapper:
    # ... other attributes

    def __init__(self):
        top, left, width, height = (
            self.monitor["top"],
            self.monitor["left"],
            self.monitor["width"],
            self.monitor["height"],
        )

        # Initialize the camera with positional arguments
        self.video_camera = ScreenShareCamera(top, left, width, height)

    # ... other methods
