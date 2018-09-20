import bpy

class CreateShapeRoot(bpy.types.Operator):
    bl_idname = "wm.tera_create_shape"
    bl_label = "Create Sprite Object"
    bl_options = {"REGISTER","UNDO"}

    def execute(self, context):
        context.scene.objects.active = None
        bpy.ops.object.empty_add(type='PLAIN_AXES', radius=1, view_align=False,location=context.scene.cursor_location)
        empty = bpy.context.active_object
        empty.name ='shape'
        empty.show_name = True
        empty.show_x_ray = True
        empty["terra_shape"] = True
        bpy.ops.ed.undo_push(message="Create Shape Object")
        return {"FINISHED"}
