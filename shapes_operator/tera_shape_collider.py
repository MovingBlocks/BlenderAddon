if "bpy" in locals():
    import importlib
    importlib.reload(draw_util)
else:
    import bpy
    from .. import draw_util

from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        FloatVectorProperty
        )




def draw_aabb(self, context):
    obj = bpy.data.objects[context.scene.tera_shape_select_index]

    if (obj and self):
        l = obj.location
        origin = self.origin
        extent = self.extent
        indices, coords = draw_util.get_line_cube(
            l[0] + origin[0] - extent[0],
            l[0] + origin[0] + extent[0],
            l[1] + origin[1] - extent[1],
            l[1] + origin[1] + extent[1],
            l[2] + origin[2] - extent[2],
            l[2] + origin[2] + extent[2])
        draw_util.draw_wire_frame(indices, coords, (0, 0, 1, 1))


class TERA_SHAPES_OT_add_aabb_collider(Operator):
    bl_idname = "tera.add_aabb_collider"
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

    def __init__(self):
        pass

    @classmethod
    def poll(cls, context):
        return (context.scene.tera_shape_select_index > 0 and context.scene.tera_shape_select_index < len(bpy.data.objects))

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
        selected_object = bpy.data.objects[context.scene.tera_shape_select_index]
        aabb = selected_object.tera_shape.aabb.add()
        aabb.label = self.label
        aabb.origin = self.origin
        aabb.extent = self.extent
        return {'FINISHED'}


    def invoke(self, context, event):
        self.handler = bpy.types.SpaceView3D.draw_handler_add(draw_aabb, (self, context), 'WINDOW', 'POST_VIEW')
        return context.window_manager.invoke_props_dialog(self, width = 400)


class TERA_SHAPES_OT_remove_aabb_collider(Operator):
    bl_idname = "tera.remove_aabb_collider"
    bl_label = "Remove AABB"
    bl_description = "Removes AABB"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (context.scene.tera_shape_select_index > 0 and context.scene.tera_shape_select_index < len(bpy.data.objects))

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.row().prop(self, "aabb")

    def execute(self, context):
        selected_object = bpy.data.objects[context.scene.tera_shape_select_index]
        selected_object.tera_shape.aabb.remove(selected_object.tera_shape.aabb_index)
        # aabb.label = self.label
        return {'FINISHED'}


    def invoke(self, context, event):
        return self.execute(context)
