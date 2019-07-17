from bpy.types import (Panel, UIList, BlendDataCollections)
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
    CollectionProperty
)
import bpy


class TERA_SHAPES_UL_shape(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
        layout.prop(item, "name", text="", emboss=False, icon_value=icon)

    def filter_items(self, context, data, propname):
        obs = getattr(data, propname)

        # Default return values.
        flt_flags = []
        flt_neworder = []

        for idx, ob in enumerate(obs):
            flt_neworder.append(idx)
            if(ob.parent == None and ob.type in ['EMPTY'] and ob.name.startswith('shape_')):
                flt_flags.append(self.bitflag_filter_item)
            else:
                flt_flags.append(~self.bitflag_filter_item)

        return (flt_flags, flt_neworder)


class TERA_SHAPES_PT_shapes(Panel):
    bl_idname = "TERA_SHAPES_PT_shapes"
    bl_label = "Terasology Shapes"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw(self, context):
        row = self.layout.row()
        row.template_list("TERA_SHAPES_UL_shape", "", bpy.data,
                          "objects", context.scene, "tera_shape_select_index")

        col = row.column()
        col.operator("tera.add_shape", icon='ADD', text="")
        col.operator("tera.remove_shape", icon='REMOVE', text="")

        if(context.scene.tera_shape_select_index > 0 and context.scene.tera_shape_select_index < len(bpy.data.objects)):
            selected_object = bpy.data.objects[context.scene.tera_shape_select_index]
            if(selected_object):
                self.layout.row().prop(selected_object.tera_shape, "author")
                self.layout.row().prop(selected_object.tera_shape, "display_name")
                self.layout.row().prop(selected_object.tera_shape, "symmetric")
                self.layout.row().prop(selected_object.tera_shape, "yaw_symmetric")
                self.layout.row().prop(selected_object.tera_shape, "pitch_symmetric")
                self.layout.row().prop(selected_object.tera_shape, "roll_symmetric")
