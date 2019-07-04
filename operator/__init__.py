
if "bpy" in locals():
    import importlib
    importlib.reload(add_group)
    importlib.reload(add_block_to_group)
else:
    from . import add_block_group
    from . import add_block_to_group
import bpy


def register():
    bpy.utils.register_class(add_block_group.AddBlockGroup)
    bpy.utils.register_class(add_block_to_group.AddBlockToGroup)


def unregister():
    bpy.utils.unregister_class(add_block_group.AddBlockGroup)
    bpy.utils.register_class(add_block_to_group.AddBlockToGroup)