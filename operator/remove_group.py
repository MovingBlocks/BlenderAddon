from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )
import bpy

class RemoveGroup(Operator):
    bl_idname = "tera.remove_group"
    bl_label = "Remove Group"
    bl_description = "Remove Group"

    def invoke(self, context, event):
        return self.execute(context)

    def execute(self,context):
        selected_group = context.scene.tera_selected_group
        bpy.data.collections.remove(selected_group)
        return {'FINISHED'}