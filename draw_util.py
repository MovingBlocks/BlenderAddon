import bpy
import gpu
from mathutils import Matrix,Vector
from gpu_extras.batch import batch_for_shader

def get_cube_coords(xmin,xmax,ymin,ymax,zmin,zmax):
    return (
        (xmin, ymin, zmin), (xmax, ymin, zmin),
        (xmin, ymax, zmin), (xmax, ymax, zmin),
        (xmin, ymin, zmax), (xmax, ymin, zmax),
        (xmin, ymax, zmax), (xmax, ymax, zmax))


def draw_solid_cube(xmin,xmax,ymin,ymax,zmin,zmax,color):
    pass

def draw_wire_cube(xmin,xmax,ymin,ymax,zmin,zmax,color):
    coords = get_cube_coords(xmin,xmax,ymin,ymax,zmin,zmax)

    indices = (
        (0, 1), (0, 2), (1, 3), (2, 3),
        (4, 5), (4, 6), (5, 7), (6, 7),
        (0, 4), (1, 5), (2, 6), (3, 7))

    shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
    batch = batch_for_shader(shader, 'LINES', {"pos": coords}, indices=indices)

    shader.bind()
    shader.uniform_float("color", color)
    batch.draw(shader)

