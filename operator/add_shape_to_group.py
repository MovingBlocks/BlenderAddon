import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
)
from bpy.types import Operator


def get_groups(self, context):
    return {(c.name,c.name,'') for c in bpy.data.collections}

def on_update_groups(self, context):
    pass

class AddShapeToGroup(Operator):
    bl_idname = "tera.add_shape_to_group"
    bl_label = "Add Shape"
    bl_description = "Adds a new Shape to Group"

    collection: EnumProperty(
        name='Shape Group',
        description='Add shape to group.',
        items=get_groups,
        update=on_update_groups)

    name:  StringProperty(
        name="name",
        default="")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)

    def draw(self,context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "name")
        if(bpy.context.area.type != 'PROPERTIES'):
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



