import bpy
from bpy_extras import view3d_utils
from mathutils import Vector

def get_3d_view_pixel_coords():
    context = bpy.context

    for window in context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        # Ensure region_3d exists and is valid
                        if not hasattr(area.spaces.active, "region_3d"):
                            continue  # Skip this region if region_3d is not available
                        
                        rv3d = area.spaces.active.region_3d

                        # Convert region coordinates to 3D using (0, 0, 0) as initial guess
                        # This will give us the depth_location at the origin of the region.
                        coord = region.view2d.region_to_view(0, 0)
                        depth_location = view3d_utils.region_2d_to_location_3d(region, rv3d, coord, (0, 0, 0))

                        # Correcting depth_location type
                        depth_location = Vector(tuple(depth_location)) 

                        # Get 3D viewport edges in 3D with depth_location
                        v3d = view3d_utils.region_2d_to_location_3d(region, rv3d, (0, 0), depth_location=depth_location)
                        v3d_upright = view3d_utils.region_2d_to_location_3d(region, rv3d, (1, 1), depth_location=depth_location)

                        # Add the region offset within the window
                        v3d = Vector(v3d) + Vector((region.x, region.y, 0))  # Convert to tuple explicitly
                        v3d_upright = Vector(v3d_upright) + Vector((region.x, region.y, 0))

                        # Extract the coordinates
                        left, bottom, _ = v3d
                        right, top, _ = v3d_upright

                        # Calculate width, height, and center coordinates
                        width = right - left
                        height = top - bottom
                        center_x = (left + right) // 2
                        center_y = (top + bottom) // 2

                        return left, bottom, width, height, center_x, center_y
    
    return None  # No 3D Viewport found

# Example usage
pixel_coords = get_3d_view_pixel_coords()
if pixel_coords:
    left, bottom, width, height, center_x, center_y = pixel_coords
    print(f"3D Viewport found at ({left}, {bottom}) with dimensions ({width}, {height}) on your display(s).")
    print(f"Center coordinates: ({center_x}, {center_y})")
else:
    print("3D Viewport not found in any open Blender window.")
