import bpy

from bpy.types import (PropertyGroup,Collection,Object)
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        StringProperty,
        CollectionProperty,
        PointerProperty,
        FloatVectorProperty
        )


class TeraBlockAABB(PropertyGroup):
    label = StringProperty(name="label",
                           description="label that describes aabb collider")
    origin = FloatVectorProperty(name="origin",
                                 description="origin of the collider shape",
                                 size=3)
    extent = FloatVectorProperty(name="extent",
                                 description="extent of the collider shape",
                                 size=3)


class TeraBlockProperty(PropertyGroup):

    author = StringProperty(default="")
    aabb = CollectionProperty(type=TeraBlockAABB)
    aabb_index = IntProperty()

def register():
    bpy.utils.register_class(TeraBlockAABB)
    bpy.utils.register_class(TeraBlockProperty)

    bpy.types.Object.tera_block = PointerProperty(type=TeraBlockProperty)

    bpy.types.Scene.tera_selected_group =  PointerProperty(type=Collection)
    bpy.types.Collection.tera_block_index = IntProperty()


def unregister():
    bpy.utils.unregister_class(TeraBlockAABB)
    bpy.utils.unregister_class(TeraBlockProperty)