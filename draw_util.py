import bpy
import gpu
import bgl
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

def draw_line(x1,y1,z1,x2,y2,z2):
    pass

def draw_wire_cube(xmin,xmax,ymin,ymax,zmin,zmax,color):
    coords = get_cube_coords(xmin,xmax,ymin,ymax,zmin,zmax)

    bgl.glEnable(bgl.GL_DEPTH_TEST)
    bgl.glEnable(bgl.GL_BLEND)
    # bgl.glDepthRange(0.0, 0.9)

    indices = (
        (0, 1), (0, 2), (1, 3), (2, 3),
        (4, 5), (4, 6), (5, 7), (6, 7),
        (0, 4), (1, 5), (2, 6), (3, 7))

    shader = gpu.shader.from_builtin('3D_UNIFORM_COLOR')
    batch = batch_for_shader(shader, 'LINES', {"pos": coords}, indices=indices)

    shader.bind()
    shader.uniform_float("color", color)
    batch.draw(shader)

    # bgl.glDisable(bgl.GL_DEPTH_TEST)
    bgl.glDisable(bgl.GL_DEPTH_TEST)
    bgl.glDisable(bgl.GL_BLEND)



