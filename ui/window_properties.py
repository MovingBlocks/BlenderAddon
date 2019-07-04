from bpy.types import Panel
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )
import bpy

class WindowPanelProperties(Panel):
    bl_idname = "Window_PT_Blocks"
    bl_label = "Terasology Scene Properties"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    def draw(self, context):
        self.layout.label(text="Hello Worssld")
        col = self.layout.column(align=True)
        col.operator("block.groups.add_groups", text="add")

        box = self.layout.box()
        for collection in bpy.data.collections:
            collection_names = collection.name.split('_',1)
            if(len(collection_names) == 2 and collection_names[0] == 'blocks'):
                title = collection_names[1]
                row = box.row(align=True)
                container = row.box()
                container.label(text = title)