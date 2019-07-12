if "bpy" in locals():
    import importlib
    importlib.reload(properties_shapes)
    importlib.reload(space_collider_shapes)
else:
    from . import properties_shapes
    from . import space_collider_shapes



def register():
    bpy.utils.register_class(properties_shapes.TERA_SHAPES_PT_shapes)

    bpy.utils.register_class(space_collider_shapes.Shape_Collider_UL_AABB_list)
    bpy.utils.register_class(space_collider_shapes.Window_PT_AABBBoxCollider)
    bpy.utils.register_class(space_collider_shapes.Shape_UL_Mesh_list)
    bpy.utils.register_class(space_collider_shapes.Window_PT_BlockUtilities)


def unregister():
    bpy.utils.unregister_class(properties_shapes.TERA_SHAPES_PT_shapes)

    bpy.utils.unregister_class(space_collider_shapes.Shape_Collider_UL_AABB_list)
    bpy.utils.unregister_class(space_collider_shapes.Window_PT_AABBBoxCollider)
    bpy.utils.unregister_class(space_collider_shapes.Shape_UL_Mesh_list)
    bpy.utils.unregister_class(space_collider_shapes.Window_PT_BlockUtilities)