# ... (other imports)
from animator import animatable_object

# ... (inside ModalTimerOperator class)

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

        focus = animatable_object('focus') 
       
        frame_index = int(bpy.context.scene.frame_current / 30) % (16*5)
        song = [4, 3, 2, 1, 1, 2, 3, 4, 0, 2, 1, 2, 0, 1, 2, 0, 0, 3, 0, 4, 0, 3, 4, 3, 2, 1] * 5
        interval = -4.0
        offset = 0

        focus.location.x = song[frame_index ] - 0
        focus.location.y = offset + frame_index * interval
        focus.location.z = 4

    def key_handling(self, context, event, key_input):
        # ... (rest of the key_handling logic)

        # Check if player hit the correct note
        bike_mover = animatable_object('bike-mover')
        focus = animatable_object('focus')
        if abs(bike_mover.location.x - focus.location.x) < 0.25: 
            score_obj = animatable_object('ui.Text.score')
            score_obj["score"] += 1
            showTxt("score +1")

    def set_visibility(self, obj_name, state):
        obj = animatable_object(obj_name)
        if state == "Toggle":
            is_visible = not obj.visible 
        elif state == "True":
            is_visible = True
        elif state == "False":
            is_visible = False
        else:
            print(f"Invalid state: {state}. Use 'True', 'False', or 'Toggle'.")
            return 

        obj.visible = is_visible 

        print(f"Object '{obj_name}' visibility set to: {is_visible}")

 # ... (inside ModalTimerOperator.modal)
        #Story
        chat_text = animatable_object('chat_text')
        chat1 = animatable_object('chat1')
        if 30 <= current_frame < 50:
            chat1.visible = True 
            # ...
            chat_text.text = str('\n'.join(serif))
        # ...
        elif 120 <= current_frame < 123:
            chat1.visible = False
        elif 130 <= current_frame < 135:
            chat1.visible = True
            # ...
            chat_text.text = str('\n'.join(serif))

# ... (rest of the __main__.py code)