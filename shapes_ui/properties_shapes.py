if "bpy" in locals():
    import importlib
    importlib.reload(util)
else:
    from .. import util

from bpy.types import (Panel,UIList,BlendDataCollections)
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        CollectionProperty
        )
import bpy

class TERA_SHAPES_PT_shapes(Panel):
    bl_idname = "TERA_SHAPES_PT_shapes"
    bl_label = "Terasology Blocks"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw_collection(self,context,col,root_collection):
        for collection in root_collection.children:
            selected_group = context.scene.tera_selected_group
            row = col.row()

            row.split(factor=.2)
            r2 = row.column()
            r3 = r2.row()

            r3.operator("tera.select_group",emboss=False, icon='DECORATE_KEYFRAME' if selected_group == collection else 'DECORATE_ANIMATE',text="").target = collection.name
            r3.label(text=collection.name)
            self.draw_collection(context,r2.column(),collection)


    def draw(self, context):
        selected_group_collection = context.scene.tera_selected_group
        row = self.layout.row()
        row1 = row.box()
        col = row1.column()
        col.label(text="Block Groups")
        scn = bpy.context.scene
        self.draw_collection(context,col,scn.collection)

        col = row.column()
        col.operator("tera.add_group", icon='ADD', text="")
        col.operator("tera.remove_group", icon='REMOVE', text="")


        row = self.layout.row()
        if(selected_group_collection):
            row.template_list("Block_UL_list","",selected_group_collection,"objects",selected_group_collection,"tera_block_index")
            col = row.column()
            selected_object = util.getSelectedObjectShape()

            # right and and remove
            op = col.operator("tera.add_shape_to_group", icon='ADD', text="")
            op.collection = selected_group_collection.name
            op = col.operator("tera.remove_shape_to_group", icon='REMOVE', text="")
            op.collection = selected_group_collection.name
            op.shape = selected_object.name


            if(selected_object):
                self.layout.row().prop(selected_object.tera_block,"author")
                self.layout.row().prop(selected_object.tera_block, "symmetric")
                self.layout.row().prop(selected_object.tera_block, "yawSymmetric")
                self.layout.row().prop(selected_object.tera_block, "pitchSymmetric")
                self.layout.row().prop(selected_object.tera_block, "rollSymmetric")

