import bpy


class TerasolgyProperties(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Terasology Tools"
    bl_category = "Tera Tools"

    @classmethod
    def poll(cls, context):
        return True# (context.active_object)

    def draw(self, context):
        obj = context.active_object
        wm = context.window_manager
        layout = self.layout
        scene = context.scene
        layout.prop(scene, 'teraAuthor')

        # layout.prop(scene, 'wm.tera_create_shape')

        # row.operator("coa_tools.show_help", text="", icon="INFO")
        # if obj == None or (obj != None and obj.mode not in ["EDIT", "WEIGHT_PAINT", "SCULPT"]):
        row = layout.row(align=True)
        row.operator("wm.tera_create_shape", text="Create New Shape", icon="TEXTURE_DATA")

class CutoutAnimationTools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_label = "Shapes"
    bl_category = "Tera Tools"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and 'terra_shape' in obj and obj['terra_shape'] == 1)# (context.active_object)

    def draw(self, context):
        obj = context.active_object

        pass