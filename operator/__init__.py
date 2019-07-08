if "bpy" in locals():
    import importlib
    importlib.reload(add_group)
    importlib.reload(remove_group)
    importlib.reload(add_shape_to_group)
    importlib.reload(select_group)
    importlib.reload(add_aabb_shape_collider)
    importlib.reload(remove_shape_to_group)
else:
    from . import add_shape_to_group
    from . import select_group
    from . import remove_group
    from . import add_group
    from . import add_aabb_shape_collider
    from . import remove_shape_to_group
import bpy


def register():
    bpy.utils.register_class(add_group.AddGroup)
    bpy.utils.register_class(remove_group.RemoveGroup)
    bpy.utils.register_class(add_shape_to_group.AddShapeToGroup)
    bpy.utils.register_class(select_group.SelectGroup)
    bpy.utils.register_class(remove_shape_to_group.RemoveShapeToGroup)
    bpy.utils.register_class(add_aabb_shape_collider.AddAABBBlockCollider)

def unregister():
    bpy.utils.unregister_class(add_group.AddGroup)
    bpy.utils.unregister_class(remove_group.RemoveGroup)
    bpy.utils.unregister_class(add_shape_to_group.AddShapeToGroup)
    bpy.utils.unregister_class(select_group.SelectGroup)
    bpy.utils.unregister_class(add_aabb_shape_collider.AddAABBBlockCollider)
    bpy.utils.unregister_class(remove_shape_to_group.RemoveShapeToGroup)