if "bpy" in locals():
    import importlib
    importlib.reload(block_group_property)
    importlib.reload(block_property)
else:
    from . import block_group_property
    from .  import block_property

import bpy

def register():
    bpy.utils.register_class(block_group_property.BlockGroupPropertyGroup)
    bpy.types.Collection.block_group = bpy.props.PointerProperty(type=block_group_property.BlockGroupPropertyGroup)

def unregister():
    bpy.utils.unregister_class(block_group_property.BlockGroupPropertyGroup)