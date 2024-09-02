import bpy
debug = True
class hud:
    def __init__(self, object_name):
        self.obj = bpy.data.objects.get(object_name)
        if self.obj is None:
            raise ValueError(f"Object with name '{object_name}' not found.")

    @property
    def location(self):
        # if debug == False:
        return self.obj.location

    @location.setter
    def location(self, new_location):
        # if debug == False:
        self.obj.location = new_location
        # Make sure Blender updates its internal data
        bpy.context.view_layer.objects.active = self.obj

    @property
    def visible(self):
        if debug == False:
            return not self.obj.hide_viewport and not self.obj.hide_render

    @visible.setter
    def visible(self, is_visible):
        if debug == False:
            self.obj.hide_viewport = not is_visible
            self.obj.hide_render = not is_visible

    @property
    def text(self):
        if debug == False:
            if self.obj.type == 'FONT':
                return self.obj.data.body
            else:
                raise TypeError("The 'text' property is only available for Text objects.")

    @text.setter
    def text(self, new_text):
        if debug == False:
            if self.obj.type == 'FONT':
                self.obj.data.body = new_text
            else:
                raise TypeError("The 'text' property is only available for Text objects.")