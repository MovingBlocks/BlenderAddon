from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )
import bpy

def get_block_groups(self, context):
    return {(c.name,c.name,'') for c in bpy.data.collections}

def collection_update_prop(self, context):
    pass

class AddBlockToGroup(Operator):
    bl_idname = "tera.add_block_to_group"
    bl_label = "Add Block"
    bl_description = "Adds a new Block to Group"

    collection: EnumProperty(
        name='block group',
        description='The collection to reference.',
        items=get_block_groups,
        update=collection_update_prop)

    name:  StringProperty(
        name="name",
        default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)

    def draw(self,context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "name")
        col.row().prop(self,"collection")

    def execute(self,context):
        if not self.name:
            self.report({"WARNING"},
                        "name for group required")
            return {'CANCELLED'}
        collection = bpy.data.collections[self.collection]
        o = bpy.data.objects.new(self.name, None)
        collection.objects.link(o)
        o.empty_display_type = 'PLAIN_AXES'
        return  {'FINISHED'}



