from .. import util
if "bpy" in locals():
    import importlib
    importlib.reload(draw_util)
    importlib.reload(util)
else:
    from .. import draw_util
    from .. import util

from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        FloatVectorProperty
        )
import bpy



def draw_aabb(self,context):
    obj = util.getSelectedObjectShape()
    if(obj):
        l = obj.location
        draw_util.draw_wire_cube(l[0] + self.origin[0] - .10, l[0] + .5, l[1] - .5, l[1] + .5, l[2], l[2] + 1, (0, 1, 0, .1))
    # draw_util.draw_wire_cube()

class AddAABBBlockCollider(Operator):
    bl_idname = "tera.add_aabb_shape_collider"
    bl_label = "Add AABB"
    bl_description = "Adds AABB to Shape"

    label = StringProperty(name="label",
                           description="label that describes aabb collider")
    origin = FloatVectorProperty(name="origin",
                                 description="origin of the collider shape",
                                 size=3)
    extent = FloatVectorProperty(name="extent",
                                 description="extent of the collider shape",
                                 size=3)
    handler = None

    def __init__(self):
        print("Start")

    def __del__(self):
        bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
        print("End")

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "label")
        col.row().prop(self, "origin")
        col.row().prop(self, "extent")

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        self.handler = bpy.types.SpaceView3D.draw_handler_add(draw_aabb, (self, context), 'WINDOW', 'POST_VIEW')
        return context.window_manager.invoke_props_dialog(self, width=400)