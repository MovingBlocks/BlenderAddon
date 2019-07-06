
if "bpy" in locals():
    import importlib
    importlib.reload(add_group)
    importlib.reload(remove_group)
    importlib.reload(add_block_to_group)
    importlib.reload(select_block_group)
else:
    from . import add_block_to_group
    from . import select_block_group
    from . import remove_group
    from . import add_group
import bpy


def register():
    bpy.utils.register_class(add_group.AddBlockGroup)
    bpy.utils.register_class(remove_group.RemoveBlockGroup)
    bpy.utils.register_class(add_block_to_group.AddBlockToGroup)
    bpy.utils.register_class(select_block_group.SelectedBlockGroup)


def unregister():
    bpy.utils.unregister_class(add_group.AddBlockGroup)
    bpy.utils.unregister_class(remove_group.RemoveBlockGroup)
    bpy.utils.unregister_class(add_block_to_group.AddBlockToGroup)
    bpy.utils.unregister_class(select_block_group.SelectedBlockGroup)