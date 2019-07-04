from bpy.types import Operator
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        )
import bpy
from utils import block_groups

def get_group_enum():
    collection = block_groups.get_groups()
    [(block_groups.get_group_name(c),) for c in collection]


class AddBlockToGroup(Operator):
    block_group: EnumProperty(
        name="Block Groups",
        description = "List of Groups",
        items= []
    )
    pass