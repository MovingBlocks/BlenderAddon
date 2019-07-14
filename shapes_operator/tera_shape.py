import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
)
from bpy.types import Operator


class TERA_SHAPES_OT_add_shape(Operator):
    bl_idname = "tera.add_shape"
    bl_label = "Add Shape"
    bl_description = "Adds a new Shape"

    name =  StringProperty(
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
        o = bpy.data.objects.new('shape_' + self.name, None)
        o.empty_display_type = 'PLAIN_AXES'
        o.tera_shape.display_name = self.name
        bpy.context.collection.objects.link(o)
        return  {'FINISHED'}


class TERA_SHAPES_OT_remove_shape(Operator):
    bl_idname = "tera.remove_shape"
    bl_label = "Remove Shape"
    bl_description = "Removes a shape and children"


    def get_shapes(self, context):
        coll = self.collection
        return {(ob.name, ob.name, '') for ob in bpy.data.collections[coll].objects if
                (ob.parent == None and ob.type in ['EMPTY'])}

    def on_update_shapes(self, context):
        pass

    def __init__(self):
        self.shape =  EnumProperty(
        name="name",
        description='Shape to remove.',
        items=self.get_shapes,
        update=self.on_update_shapes)


    def invoke(self, context, event):
        if (bpy.context.area.type == 'PROPERTIES'):
            return self.execute(context)
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "collection")
        col.row().prop(self, "shape")

    def execute(self, context):
        if not self.name:
            self.report({"WARNING"},
                        "name for group required")
            return {'CANCELLED'}
        bpy.data.objects.remove(bpy.data.objects[self.shape])
        return {'FINISHED'}


