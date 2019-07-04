import bpy

from bpy.types import PropertyGroup
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )

class BlockGroupPropertyGroup(PropertyGroup):
    name: StringProperty(default="")