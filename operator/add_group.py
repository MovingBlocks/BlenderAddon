from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )
import bpy

def get_groups(self, context):
    result = {(c.name,c.name,'') for c in bpy.data.collections}
    result.add(('none', 'none', 'no parents'))
    return result

def collection_update_prop(self, context):
    pass


class AddGroup(Operator):
    bl_idname = "tera.add_group"
    bl_label = "Add Group"
    bl_description = "Adds a new shape to group"

    parent: EnumProperty(
        name='block group',
        description='The collection to parent group to.',
        items=get_groups,
        update=collection_update_prop)

    name: StringProperty(
            name="name",
            default=""
            )


    def draw(self,context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self,"name")
        col.row().prop(self, "parent")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)

    def execute(self,context):
        if not self.name:
            self.report({"WARNING"},
                        "name for group required")
            return {'CANCELLED'}
        collection = bpy.data.collections.new(self.name)
        if(self.parent and self.parent == 'none'):
            bpy.context.scene.collection.children.link(collection)
        else:
            bpy.data.collections[self.parent].children.link(collection)
        return  {'FINISHED'}