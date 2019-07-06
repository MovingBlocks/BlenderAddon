from bpy.types import (Operator,Collection)
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        PointerProperty
        )
import bpy

class SelectedBlockGroup(Operator):
    bl_idname = "tera.select_block_group"
    bl_label = "Select Group"
    bl_description = "Select a Group"

    target = StringProperty(
        name="name",
        default=""
    )

    def draw(self, context):
        pass

    def invoke(self, context, event):
        return self.execute(context)


    def execute(self,context):
        # context.scene.block_group_meta.selected_group = self.selected
        if(self.target in bpy.data.collections):
            context.scene.tera_selected_group = bpy.data.collections[self.target]
            return {'FINISHED'}
        self.report({"WARNING"}, "Can't find Group")
        return {'CANCELLED'}