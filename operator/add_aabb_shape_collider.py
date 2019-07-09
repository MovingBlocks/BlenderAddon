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
    if(obj and self):
        l = obj.location
        origin = self.origin
        extent = self.extent
        draw_util.draw_wire_cube(
            l[0] + origin[0] - extent[0],
            l[0] + origin[0] + extent[0],
            l[1] + origin[1] - extent[1],
            l[1] + origin[1] + extent[1],
            l[2] + origin[2] - extent[2],
            l[2] + origin[2] + extent[2], (0, 0, 1, 1))

    # draw_util.draw_wire_cube()

class AddAABBBlockCollider(Operator):
    bl_idname = "tera.add_aabb_shape_collider"
    bl_label = "Add AABB"
    bl_description = "Adds AABB to Shape"
    bl_options = {'REGISTER', 'UNDO'}

    label = StringProperty(name="label",
                           description="label that describes aabb collider")
    origin = FloatVectorProperty(name="origin",
                                 description="origin of collider",
                                 )

    extent = FloatVectorProperty(name="extent",
                                 description="extent of collider",
                                 )


    handler = None


    @classmethod
    def poll(cls, context):
        selected_object = util.getSelectedObjectShape()
        return (selected_object is not None)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "label")
        col.row().prop(self, "origin")
        col.row().prop(self, "extent")


    def execute(self, context):
        if(self.handler != None):
            bpy.types.SpaceView3D.draw_handler_remove(self.handler, 'WINDOW')
            self.handler = None
        if not self.label:
            self.report({"WARNING"},
                        "label for aabb required")
            return {'CANCELLED'}
        selected_object = util.getSelectedObjectShape()
        aabb = selected_object.tera_block.aabb.add()
        aabb.label = self.label
        aabb.origin = self.origin
        aabb.extent = self.extent
        return {'FINISHED'}


    def invoke(self, context, event):
        self.handler = bpy.types.SpaceView3D.draw_handler_add(draw_aabb, (self, context), 'WINDOW', 'POST_VIEW')
        return context.window_manager.invoke_props_dialog(self, width = 400)
