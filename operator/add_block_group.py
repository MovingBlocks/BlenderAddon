from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )
import bpy

class AddBlockGroup(Operator):
    bl_idname = "block.groups.add_groups"
    bl_label = "new Group"
    bl_description = "Adds a new Group"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}

    title: StringProperty(
            name="name",
            default=""
            )
    def draw(self,context):
        layout = self.layout

        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(self,"title")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)

    def execute(self,context):
        if not self.title:
            self.report({"WARNING"},
                        "Title for block set required")
            return {'CANCELLED'}
        coll = bpy.data.collections.new('blocks' + '_' + self.title )
        bpy.context.scene.collection.children.link(coll)
        return  {'FINISHED'}