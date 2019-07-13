if "bpy" in locals():
    import importlib
    importlib.reload(tera_shape_collider)
    importlib.reload(tera_shape)
    # importlib(tera_shape_export)
else:
    import bpy
    from . import tera_shape
    from . import tera_shape_collider
    # from . import tera_shape_export

def register():
    bpy.utils.register_class(tera_shape.TERA_SHAPES_OT_add_shape)
    bpy.utils.register_class(tera_shape.TERA_SHAPES_OT_remove_shape)
    bpy.utils.register_class(tera_shape_collider.TERA_SHAPES_OT_add_aabb_collider)
    bpy.utils.register_class(tera_shape_collider.TERA_SHAPES_OT_remove_aabb_collider)

def unregister():
    bpy.utils.unregister_class(tera_shape.TERA_SHAPES_OT_add_shape)
    bpy.utils.unregister_class(tera_shape.TERA_SHAPES_OT_remove_shape)
    bpy.utils.unregister_class(tera_shape_collider.TERA_SHAPES_OT_add_aabb_collider)
    bpy.utils.unregister_class(tera_shape_collider.TERA_SHAPES_OT_remove_aabb_collider)


