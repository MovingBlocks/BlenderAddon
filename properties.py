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
    name = StringProperty(default="")
    author = StringProperty(default="")

# class TeraBlockCollectionProperty(PropertyGroup):
#     name = StringProperty(default="")
#     expanded = BoolProperty(default=True)


def register():
    bpy.utils.register_class(TeraBlockProperty)

    # bpy.types.empty
    # bpy.utils.register_class(TeraBlockCollectionProperty)
    bpy.types.Object.tera_block = PointerProperty(type=TeraBlockProperty)
    # bpy.types.Collection.tera_group = bpy.props.PointerProperty(type=TeraBlockCollectionProperty)
    bpy.types.Scene.tera_selected_group =  PointerProperty(type=Collection)
    bpy.types.Collection.tera_block_index = IntProperty()


def unregister():
    bpy.utils.unregister_class(TeraBlockProperty)
    # bpy.utils.unregister_class(TeraBlockCollectionProperty)