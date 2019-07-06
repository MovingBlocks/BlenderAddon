import bpy
import gpu
from mathutils import Matrix,Vector
from gpu_extras.batch import batch_for_shader


def draw_cube(xmin,xmax,ymin,ymax,zmin,zmax,color):
    indices = (
        (0, 1), (0, 2), (1, 3), (2, 3),
        (4, 5), (4, 6), (5, 7), (6, 7),
        (0, 4), (1, 5), (2, 6), (3, 7))

    coords = (
        (xmin, ymin, zmin), (xmax, ymin, zmin),
        (xmin, ymax, zmin), (xmax, ymax, zmin),
        (xmin, ymin, zmax), (xmax, ymin, zmax),
        (xmin, ymax, zmax), (xmax, ymax, zmax))

    shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
    batch = batch_for_shader(shader, 'LINES', {"pos": coords}, indices=indices)

    shader.bind()
    shader.uniform_float("color", color)
    batch.draw(shader)


def draw():
    selected_group_collection = bpy.context.scene.tera_selected_group

    if(selected_group_collection):
        length = len(selected_group_collection.objects)
        if (length > 0 and selected_group_collection.tera_block_index < length):
            selected_object = selected_group_collection.objects[selected_group_collection.tera_block_index]
            l = selected_object.location
            draw_cube(l[0] - .5,l[0] + .5,l[1] - .5,l[1] + .5,l[2],l[2] + 1,(0,1,0,.1))

    # shader.bind()
    # shader.uniform_float("color", (1, 0, 0, 1))
    # batch.draw(shader)

def register():
    global handler
    handler = bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')

def unregister():
    global handler
    bpy.types.SpaceView3D.draw_handler_remove(handler, 'WINDOW')