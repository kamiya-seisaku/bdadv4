import bpy

def set_obj_select_keymap(set):
    #sets activation of 'A' key keymap in object mode to "(De)select All" operator
    #Arguments: set
    #    "on": turn activation on
    #    "off": turn activation off
    #    "toggle": toggles activation
    print(f"set={set}")

    keymap = bpy.context.window_manager.keyconfigs.user.keymaps['Object Mode']

    # Find the specific keymap item
    for kmi in keymap.keymap_items:
        if kmi.idname == 'object.select_all' and kmi.type == 'A':
            break  # Exit the loop once found and modified

    print(f"keymap activation(before)={kmi.active}")

    # Display a message indicating the new state
    if set == "toggle":
        kmi.active = not kmi.active  # Toggle active state
    elif set == "on":
        kmi.active = True
    elif set == "off":
        kmi.active = False
    else:
        print("unknown argument value")

    print(f"keymap activation(after)={kmi.active}")
    if kmi.active:
        print("'(De)select All' shortcut with 'A' key is now activated.")
    else:
        print("'(De)select All' shortcut with 'A' key is now deactivated.")

def test():
    print("arg set = on")
    set_obj_select_keymap("on")
    print("arg set = off")
    set_obj_select_keymap("off")
    print("arg set = toggle")
    set_obj_select_keymap("toggle")
    
if __name__ == '__main__':
    test()