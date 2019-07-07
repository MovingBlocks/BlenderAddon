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

import logging

class Block_UL_list(UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname,index, flt_flag):
        ob = data
        layout.prop(item, "name", text="", emboss=False, icon_value=icon)

    def filter_items(self, context, data, propname):
        obs = getattr(data, propname)

        # Default return values.
        flt_flags = []
        flt_neworder = []

        for idx, ob in enumerate(obs):
            logging.info(idx)
            flt_neworder.append(idx)
            if(ob.parent == None and ob.type in ['EMPTY']):
                flt_flags.append(self.bitflag_filter_item)
            else:
                flt_flags.append(~self.bitflag_filter_item)

        return (flt_flags, flt_neworder)



class Window_PT_Blocks(Panel):
    bl_idname = "Window_PT_Blocks"
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

            r3.operator("tera.select_block_group",emboss=False, icon='DECORATE_KEYFRAME' if selected_group == collection else 'DECORATE_ANIMATE',text="").target = collection.name
            r3.label(text=collection.name)
            self.draw_collection(context,r2.column(),collection)

    def draw(self, context):
        # self.layout.label(text="Block Groups")
        selected_group_collection = context.scene.tera_selected_group

        row = self.layout.row()
        row1 = row.box()
        col = row1.column()
        col.label(text="Block Groups")
        scn = bpy.context.scene
        self.draw_collection(context,col,scn.collection)

        col = row.column()
        col.operator("tera.add_block_group", icon='ADD', text="")
        col.operator("tera.remove_block_group", icon='REMOVE', text="")


        row = self.layout.row()
        if(selected_group_collection):
            row.template_list("Block_UL_list","",selected_group_collection,"objects",selected_group_collection,"tera_block_index")

        col = row.column()
        op = col.operator("tera.add_block_to_group", icon='ADD', text="")
        if(selected_group_collection):
            op.collection = selected_group_collection.name

        col.operator("tera.add_block_group", icon='REMOVE', text="")
        length = len(selected_group_collection.objects)
        if(length > 0 and selected_group_collection.tera_block_index < length):
            selected_object = selected_group_collection.objects[selected_group_collection.tera_block_index]
            # self.layout.row().label(text=selected_object.name)
            self.layout.row().prop(selected_object.tera_block,"author")


class Window_PT_BlockUtilities(Panel):
    bl_label = "Terasology Block Properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        pass

def register():
    bpy.utils.register_class(Block_UL_list)
    bpy.utils.register_class(Window_PT_Blocks)
    bpy.utils.register_class(Window_PT_BlockUtilities)


def unregister():
    bpy.utils.unregister_class(Block_UL_list)
    bpy.utils.unregister_class(Window_PT_Blocks)
    bpy.utils.unregister_class(Window_PT_BlockUtilities)