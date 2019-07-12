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
    ui.register()
    operator.register()
    properties.register()
    vieport.register()


def unregister():
    ui.unregister()
    operator.unregister()
    properties.unregister()
    vieport.unregister()

if __name__ == '__main__':
    register()

