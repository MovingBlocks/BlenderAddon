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
            ('Front', 'Front', ''),
            ('Back', 'Back', ''),
            ('Left', 'Left', ''),
            ('Right', 'Right', ''),
        ]
    )

def on_mesh_change_index(self, context):
    bpy.context.view_layer.objects.active = bpy.data.objects[self.mesh_index]


class TeraShapeProperty(PropertyGroup):
    author = StringProperty(default="")

    symmetric = BoolProperty(name="Symmetric")
    yaw_symmetric = BoolProperty(name="Yaw Symmetric")
    pitch_symmetric = BoolProperty(name="Pitch Symmetric")
    roll_symmetric = BoolProperty(name="Roll Symmetric")

    aabb = CollectionProperty(type=TeraColliderAABB)
    aabb_index = IntProperty()

    mesh_index = IntProperty(update=on_mesh_change_index)


def register():
    bpy.utils.register_class(TeraMeshShape)
    bpy.utils.register_class(TeraColliderAABB)
    bpy.utils.register_class(TeraShapeProperty)

    bpy.types.Object.tera_shape = PointerProperty(type=TeraShapeProperty)
    bpy.types.Mesh.tera_mesh = PointerProperty(type=TeraMeshShape)

    bpy.types.Scene.tera_shape_select_index = IntProperty()


def unregister():
    bpy.utils.unregister_class(TeraMeshShape)
    bpy.utils.unregister_class(TeraColliderAABB)
    bpy.utils.unregister_class(TeraShapeProperty)
