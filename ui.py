if "bpy" in locals():
    import importlib
    importlib.reload(util)
else:
    from . import util

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

class Shape_Collider_UL_AABB_list(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
        layout.prop(item, "label", text="", emboss=False, icon_value=icon)

class Window_PT_AABBBoxCollider(Panel):
    bl_label = "Terasology Colliders"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        selected_object = util.getSelectedObjectShape()
        return (selected_object is not None)

    def draw(self, context):
        selected_object = util.getSelectedObjectShape()
        row = self.layout.row()
        row.template_list("Shape_Collider_UL_AABB_list", "", selected_object.tera_block, "aabb", selected_object.tera_block,"aabb_index")

        col = row.column()
        col.operator("tera.add_aabb_shape_collider", icon='ADD', text="")
        col.operator("tera.remove_aabb_shape_collider", icon='REMOVE', text="")

        if( 0 <= selected_object.tera_block.aabb_index < len(selected_object.tera_block.aabb)):
            aabb = selected_object.tera_block.aabb[selected_object.tera_block.aabb_index]
            col = self.layout.column(align=True)
            col.row().prop(aabb, "label")
            col.row().prop(aabb, "origin")
            col.row().prop(aabb, "extent")


class Shape_UL_Mesh_list(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
        layout.prop(item, "name", text="", emboss=False, icon_value=icon)

    def filter_items(self, context, data, propname):
        obs = getattr(data, propname)

        filtered = [c.data.name for c in util.getSelectedObjectShape().children if c.type == 'MESH']

        # Default return values.
        flt_flags = []
        flt_neworder = []

        for idx, ob in enumerate(obs):
            logging.info(idx)
            flt_neworder.append(idx)
            if(ob.name in filtered):
                flt_flags.append(self.bitflag_filter_item)
            else:
                flt_flags.append(~self.bitflag_filter_item)

        return (flt_flags, flt_neworder)

class Window_PT_BlockUtilities(Panel):
    bl_label = "Terasology Shape Properties"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        return (util.getSelectedObjectShape() is not None)

    def draw(self, context):
        selected_object = util.getSelectedObjectShape()
        self.layout.row().template_list("Shape_UL_Mesh_list", "", bpy.data, "meshes", selected_object.tera_block,"mesh_index")
        if(0 <= selected_object.tera_block.mesh_index < len(bpy.data.meshes)):
            target_mesh = bpy.data.meshes[selected_object.tera_block.mesh_index]
            self.layout.row().prop(target_mesh.tera_mesh, 'part')




def register():
    bpy.utils.register_class(Shape_UL_Mesh_list)
    bpy.utils.register_class(Shape_Collider_UL_AABB_list)
    bpy.utils.register_class(Block_UL_list)
    bpy.utils.register_class(Window_PT_Blocks)
    bpy.utils.register_class(Window_PT_BlockUtilities)
    bpy.utils.register_class(Window_PT_AABBBoxCollider)


def unregister():
    bpy.utils.unregister_class(Shape_UL_Mesh_list)
    bpy.utils.unregister_class(Shape_Collider_UL_AABB_list)
    bpy.utils.unregister_class(Block_UL_list)
    bpy.utils.unregister_class(Window_PT_Blocks)
    bpy.utils.unregister_class(Window_PT_BlockUtilities)
    bpy.utils.unregister_class(Window_PT_AABBBoxCollider)