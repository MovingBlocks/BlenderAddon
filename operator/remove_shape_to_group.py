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
    return {(c.name,c.name,'') for c in bpy.data.collections}

def on_update_groups(self, context):
    pass

def get_shapes(self, context):
    coll = self.collection
    return {(ob.name,ob.name,'') for ob in bpy.data.collections[coll].objects if (ob.parent == None and ob.type in ['EMPTY'])}

def on_update_shapes(self, context):
    pass

class RemoveShapeToGroup(Operator):
    bl_idname = "tera.remove_shape_to_group"
    bl_label = "Remove Shape"
    bl_description = "Removes a Shape from an assigned Group"

    collection: EnumProperty(
        name='block group',
        description='The collection to reference.',
        items=get_groups,
        update=on_update_groups)

    shape:  EnumProperty(
        name="name",
        description='Shape to remove.',
        items=get_shapes,
        update=on_update_shapes)

    def invoke(self,context,event):
        if(bpy.context.area.type == 'PROPERTIES'):
            return self.execute(context)
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self,context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self,"collection")
        col.row().prop(self,"shape")

    def execute(self,context):
        if not self.name:
            self.report({"WARNING"},
                        "name for group required")
            return {'CANCELLED'}
        bpy.data.objects.remove(bpy.data.objects[self.shape])
        return  {'FINISHED'}

