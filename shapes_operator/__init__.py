

if "bpy" in locals():
    import importlib
    importlib(tera_shape)
    importlib(tera_shape_collider)
    importlib(tera_shape_export)
else:
    import bpy
    from . import tera_shape
    from . import tera_shape_collider
    from . import tera_shape_export


