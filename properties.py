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


class TeraColliderAABB(PropertyGroup):
    label = StringProperty(name="label",
                           description="label that describes aabb collider")
    origin = FloatVectorProperty(name="origin",
                                 description="origin of the collider shape",
                                 size=3)
    extent = FloatVectorProperty(name="extent",
                                 description="extent of the collider shape",
                                 size=3)


class TeraMeshShape(PropertyGroup):
    part = EnumProperty(
        name='shape side',
        description='determines the side that is occluded',
        items=[
            ('Center','Center',''),
            ('Top', 'Top', ''),
            ('Bottom', 'Bottom', ''),
            ('Center', 'Center', ''),
            ('Front', 'Front', ''),
            ('Back', 'Back', ''),
            ('Left', 'Left', ''),
            ('Right', 'Right', ''),
        ]
    )

def on_mesh_change_index(self, context):
    bpy.context.view_layer.objects.active = bpy.data.objects[self.mesh_index]


class TeraBlockProperty(PropertyGroup):

    author = StringProperty(default="")
    symmetric = BoolProperty(name="symmetric")
    yawSymmetric = BoolProperty(name="yawSymmetric")
    pitchSymmetric = BoolProperty(name="pitchSymmetric")
    rollSymmetric = BoolProperty(name="rollSymmetric")

    aabb = CollectionProperty(type=TeraColliderAABB)
    aabb_index = IntProperty()
    mesh_index = IntProperty(update=on_mesh_change_index)


def register():
    bpy.utils.register_class(TeraMeshShape)
    bpy.utils.register_class(TeraColliderAABB)
    bpy.utils.register_class(TeraBlockProperty)

    bpy.types.Object.tera_block = PointerProperty(type=TeraBlockProperty)
    bpy.types.Mesh.tera_mesh = PointerProperty(type=TeraMeshShape)

    bpy.types.Scene.tera_selected_group =  PointerProperty(type=Collection)
    bpy.types.Collection.tera_block_index = IntProperty()


def unregister():
    bpy.utils.unregister_class(TeraMeshShape)
    bpy.utils.unregister_class(TeraColliderAABB)
    bpy.utils.unregister_class(TeraBlockProperty)