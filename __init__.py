bl_info = {
    "name": "Terasology Shapes",
    "author": "Michael Pollind",
    "blender": (2, 80, 0),
    "location": "Object",
    "description": "A tool for creating Terasology block shapes.",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

import os

if "bpy" in locals():
    import importlib
    importlib.reload(shapes_ui)
    importlib.reload(shapes_operator)
    importlib.reload(properties)
    importlib.reload(vieport)
else:
    import bpy
    from . import shapes_ui
    from . import shapes_operator
    from . import properties
    from . import vieport

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


def register():
    shapes_ui.register()
    shapes_operator.register()
    properties.register()
    vieport.register()


def unregister():
    shapes_ui.unregister()
    shapes_operator.unregister()
    properties.unregister()
    vieport.unregister()

if __name__ == '__main__':
    register()

