import bpy

from bpy.types import (PropertyGroup,Collection,Object)
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        CollectionProperty,
        PointerProperty
        )

class TeraBlockProperty(PropertyGroup):
    author = StringProperty(default="")

# class TeraBlockCollectionProperty(PropertyGroup):
#     name = StringProperty(default="")
#     expanded = BoolProperty(default=True)


def register():
    bpy.utils.register_class(TeraBlockProperty)

    bpy.types.Object.tera_block = PointerProperty(type=TeraBlockProperty)

    bpy.types.Scene.tera_selected_group =  PointerProperty(type=Collection)
    bpy.types.Collection.tera_block_index = IntProperty()


def unregister():
    bpy.utils.unregister_class(TeraBlockProperty)
    # bpy.utils.unregister_class(TeraBlockCollectionProperty)