import bpy

class animatable_object:
    def __init__(self, object_name):
        self.obj = bpy.data.objects.get(object_name)
        if self.obj is None:
            raise ValueError(f"Object with name '{object_name}' not found.")

    @property
    def location(self):
        return self.obj.location

    @location.setter
    def location(self, new_location):
        self.obj.location = new_location
        # Make sure Blender updates its internal data
        bpy.context.view_layer.objects.active = self.obj

    @property
    def visible(self):
        return not self.obj.hide_viewport and not self.obj.hide_render

    @visible.setter
    def visible(self, is_visible):
        self.obj.hide_viewport = not is_visible
        self.obj.hide_render = not is_visible

    @property
    def text(self):
        if self.obj.type == 'FONT':
            return self.obj.data.body
        else:
            raise TypeError("The 'text' property is only available for Text objects.")

    @text.setter
    def text(self, new_text):
        if self.obj.type == 'FONT':
            self.obj.data.body = new_text
        else:
            raise TypeError("The 'text' property is only available for Text objects.")