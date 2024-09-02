import bpy
debug = False
class animatable_object:
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
    
    def run_action(self, action_name):
        # Get the action from the object's animation data
        action = self.obj.animation_data.action

        if action is None:
            self.obj.animation_data_create()
            action = bpy.data.actions.new(name="Generated NLA Action")
            self.obj.animation_data.action = action

        # Find or create an NLA track
        track = self.obj.animation_data.nla_tracks.find("Generated NLA Track")
        if track is None:
            track = self.obj.animation_data.nla_tracks.new(name="Generated NLA Track")

        # Add an NLA strip for the action
        strip = track.strips.new(name=f"ra_generated.{len(track.strips):04d}", start=bpy.context.scene.frame_current, action=bpy.data.actions[action_name])
