
if "bpy" in locals():
    import importlib
    importlib.reload(window_properties)
else:
    from . import window_properties
import bpy


def register():
    bpy.utils.register_class(window_properties.WindowPanelProperties)


def unregister():
    bpy.utils.unregister_class(window_properties.WindowPanelProperties)