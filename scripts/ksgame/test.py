import bpy

bike_mover = bpy.data.objects.get('bike-mover')
bike_mover.location.x += 0.5
bpy.context.view_layer.objects.active = bike_mover
