

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
    bgl.glEnable(bgl.GL_DEPTH_TEST)
    bgl.glEnable(bgl.GL_BLEND)

    for index,obj in enumerate(bpy.data.objects):
        loc = obj.location
        if (obj.parent == None and obj.type in ['EMPTY']):
            if(index == bpy.context.scene.tera_shape_select_index):
                shape = obj.tera_shape
                for aabb in shape.aabb:
                    origin = aabb.origin
                    extent = aabb.extent
                    indices, coords = draw_util.get_line_cube(loc[0] + origin[0] - extent[0],
                        loc[0] + origin[0] + extent[0],
                        loc[1] + origin[1] - extent[1],
                        loc[1] + origin[1] + extent[1],
                        loc[2] + origin[2] - extent[2] + .5,
                        loc[2] + origin[2] + extent[2]  + .5)
                    draw_util.draw_wire_frame(indices,coords,(0, 0, 1, .8))

                if (0 <= shape.mesh_index < len(bpy.data.meshes)):
                    part = bpy.data.meshes[shape.mesh_index].tera_mesh.part
                    if(part == 'Top'):
                        indices, coords =draw_util.get_line(loc[0],loc[1],loc[2] + 1 ,loc[0],loc[1],loc[2] + 1.5)
                        draw_util.draw_wire_frame(indices, coords, (0, 0, 1, .8))
                    if (part == 'Bottom'):
                        indices, coords =draw_util.get_line(loc[0], loc[1], loc[2], loc[0], loc[1], loc[2] - .5)
                        draw_util.draw_wire_frame(indices, coords, (0, 0, 1, .8))
                    if (part == 'Front'):
                        indices, coords =draw_util.get_line(loc[0], loc[1] + .5, loc[2] + .5, loc[0], loc[1] + 1.5, loc[2] + .5)
                        draw_util.draw_wire_frame(indices, coords, (0, 0, 1, .8))
                    if (part == 'Back'):
                        indices, coords =draw_util.get_line(loc[0], loc[1] - .5, loc[2] + .5, loc[0], loc[1] - 1.5, loc[2] + .5)
                        draw_util.draw_wire_frame(indices, coords, (0, 0, 1, .8))
                    if (part == 'Left'):
                        indices, coords =draw_util.get_line(loc[0] - .5, loc[1], loc[2] + .5, loc[0] - 1.5, loc[1], loc[2] + .5)
                        draw_util.draw_wire_frame(indices, coords, (0, 0, 1, .8))
                    if (part == 'Right'):
                        indices, coords =draw_util.get_line(loc[0] + .5, loc[1], loc[2] + .5, loc[0] + 1.5, loc[1], loc[2] + .5)
                        draw_util.draw_wire_frame(indices,coords,(0, 0, 1, .8))

                indices, coords = draw_util.get_line_cube(loc[0] - .5,
                    loc[0] + .5,
                    loc[1] - .5,
                    loc[1] + .5,
                    loc[2], loc[2] + 1)
                draw_util.draw_wire_frame(indices, coords, (0, 1, 0, .4))
            else:
                indices, coords = draw_util.get_line_cube(loc[0] - .5,
                    loc[0] + .5,
                    loc[1] - .5,
                    loc[1] + .5,
                    loc[2], loc[2] + 1)
                draw_util.draw_wire_frame(indices, coords, (0, 0, 0, .4))

    bgl.glDisable(bgl.GL_DEPTH_TEST)
    bgl.glDisable(bgl.GL_BLEND)
def register():
    global handler
    handler = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
def unregister():
    global handler
    bpy.types.SpaceView3D.draw_handler_remove(handler, 'WINDOW')