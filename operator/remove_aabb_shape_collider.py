
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

class RemoveAABBBlockCollider(Operator):
    bl_idname = "tera.remove_aabb_shape_collider"
    bl_label = "Remove AABB"
    bl_description = "Removes AABB"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        selected_object = util.getSelectedObjectShape()
        return (selected_object is not None)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "aabb")

    def execute(self, context):
        selected_object = util.getSelectedObjectShape()
        selected_object.tera_block.aabb.remove(selected_object.tera_block.aabb_index)
        # aabb.label = self.label
        return {'FINISHED'}


    def invoke(self, context, event):
        return self.execute(context)
