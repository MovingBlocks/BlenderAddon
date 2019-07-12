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
