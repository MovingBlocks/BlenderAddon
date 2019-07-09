

if "bpy" in locals():
    import importlib
    importlib.reload(draw_util)
else:
    from . import draw_util

import bpy
import gpu
from mathutils import Matrix,Vector
from gpu_extras.batch import batch_for_shader
import bgl



def draw():
    selected_group_collection = bpy.context.scene.tera_selected_group

    if(selected_group_collection):
        for index,obj in enumerate(selected_group_collection.objects):
            l = obj.location
            if (obj.parent == None and obj.type in ['EMPTY']):
                if(index == selected_group_collection.tera_block_index):
                    shape = obj.tera_block
                    for aabb in shape.aabb:
                        origin = aabb.origin
                        extent = aabb.extent
                        draw_util.draw_wire_cube(
                            l[0] + origin[0] - extent[0],
                            l[0] + origin[0] + extent[0],
                            l[1] + origin[1] - extent[1],
                            l[1] + origin[1] + extent[1],
                            l[2] + origin[2] - extent[2],
                            l[2] + origin[2] + extent[2],(0, 0, 1, .8))

                    draw_util.draw_wire_cube(
                        l[0] - .5,
                        l[0] + .5,
                        l[1] - .5,
                        l[1] + .5,
                        l[2], l[2] + 1, (0, 1, 0, .4))
                else:
                    draw_util.draw_wire_cube(
                        l[0] - .5,
                        l[0] + .5,
                        l[1] - .5,
                        l[1] + .5,
                        l[2], l[2] + 1, (0, 0, 0, .4))
def register():
    global handler
    handler = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
def unregister():
    global handler
    bpy.types.SpaceView3D.draw_handler_remove(handler, 'WINDOW')