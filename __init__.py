bl_info = {
    "name": "Terasology Blocks",
    "author": "Michael Pollind",
    "blender": (2, 80, 0),
    "location": "Object",
    "description": "A tool for creating .",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

import os


if "bpy" in locals():
    import importlib
    importlib.reload(ui)
    importlib.reload(operator)
    importlib.reload(properties)
    importlib.reload(vieport)
else:
    import bpy
    from . import ui
    from . import operator
    from . import properties
    from . import vieport
import bpy

from bpy.utils import previews

from bpy.types import (
    Panel, WindowManager, PropertyGroup,
    AddonPreferences, Menu
    )

from bpy.props import (
    EnumProperty, PointerProperty,
    StringProperty, BoolProperty,
    IntProperty, FloatProperty, FloatVectorProperty
    )


class Terasology_Block_Pref(AddonPreferences):
    bl_idname = __name__

    author: StringProperty(
        name="Author",
        description="Is this side of the block complete",
        default=""
    )
    display_name: StringProperty(
        name="Display Name",
        description="The name of the shape, displayed in game",
        default="")

    # collisionType: EnumProperty(
    #     name="Collision Type",
    #     description="Type of collision to use for this block",
    #     items=[("FullCube", "Full Cube", "The entire block is solid"),
    #            ("AutoAABB", "Auto AABB", "An AABB is calculated that encompasses the block mesh"),
    #            ("ConvexHull", "Auto Convex Hull", "A convex hull is calculated that encompasses the block mesh"),
    #            ("Manual", "Manual", "One or more colliders are specified to describe the collision")])
    #
    # collisionSymmetric: BoolProperty(
    #     name="Is Collision Symmetric",
    #     description="Whether the collision is symmetric for all rotations of the block",
    #     default=False)
    #
    # collisionSymmetricX: BoolProperty(
    #     name="Is Symmetric Around X",
    #     description="Whether the block is symmetric when rotating around X (in Blender)",
    #     default=False)
    #
    # collisionSymmetricY: BoolProperty(
    #     name="Is Symmetric Around Y",
    #     description="Whether the block is symmetric when rotating around Y (in Blender)",
    #     default=False)
    #
    # collisionSymmetricZ: BoolProperty(
    #     name="Is Symmetric Around Z",
    #     description="Whether the block is symmetric when rotating around Z (in Blender)",
    #     default=False)
    #
    # billboardNormals: BoolProperty(
    #     name="Use Billboard Normals",
    #     description="Are normals set up for billboards (pointing up)",
    #     default=False)
    #
    # fullSide: BoolProperty(
    #     name="Full Side",
    #     description="Is this side of the block complete",
    #     default=False)
    #
    # colliderType: EnumProperty(
    #     name="Collider Type",
    #     description="Type of collider this mesh provides",
    #     items=[("None", "None", "This mesh is not a collider"),
    #            ("AABB", "AABB", "This mesh provides a aabb collider"),
    #            ("Sphere", "Sphere", "This mesh provides a sphere collider")],
    #     default="None")

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.row()
        col = row.column()
        col.label(text="Configurations")
        col.prop(self,"display_name", text="Display")
        # box.label(text=)


def register():
    ui.register()
    operator.register()
    properties.register()
    vieport.register()
    # bpy.utils.register_class(Terasology_Block_Pref)
    # TOOLS_PT_panel.register()

def unregister():
    ui.unregister()
    operator.unregister()
    properties.unregister()
    vieport.unregister()
    # bpy.utils.unregister_class(Terasology_Block_Pref)
    # TOOLS_PT_panel.unregister()

if __name__ == '__main__':
    register()

