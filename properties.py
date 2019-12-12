import bpy

from bpy.types import (PropertyGroup, Collection, Object)
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
    label: StringProperty(name="label",
                           description="label that describes aabb collider")
    origin: FloatVectorProperty(name="origin",
                                 description="origin of the collider shape",
                                 size=3)
    extent: FloatVectorProperty(name="extent",
                                 description="extent of the collider shape",
                                 size=3)


class TeraMeshShape(PropertyGroup):
    part: EnumProperty(
        name='shape side',
        description='determines the side that is occluded',
        items=[
            ('center', 'Center', ''),
            ('top', 'Top', ''),
            ('bottom', 'Bottom', ''),
            ('front', 'Front', ''),
            ('back', 'Back', ''),
            ('left', 'Left', ''),
            ('right', 'Right', ''),
        ]
    )
    full_side: BoolProperty(default=True, name="Full Side")


def on_mesh_change_index(self, context):
    bpy.context.view_layer.objects.active = bpy.data.objects[self.mesh_index]


class TeraShapeProperty(PropertyGroup):
    author: StringProperty(default="", name="Author")
    display_name: StringProperty(default="", name="Display Name")

    symmetric: BoolProperty(name="Symmetric")
    yaw_symmetric: BoolProperty(name="Yaw Symmetric")
    pitch_symmetric: BoolProperty(name="Pitch Symmetric")
    roll_symmetric: BoolProperty(name="Roll Symmetric")

    convex_hull: BoolProperty(name="Convex Hull")

    aabb: CollectionProperty(type=TeraColliderAABB)
    aabb_index: IntProperty()

    mesh_index: IntProperty(update=on_mesh_change_index)


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
