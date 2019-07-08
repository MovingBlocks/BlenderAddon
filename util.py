import bpy
def getSelectedObjectShape():
    selected_group_collection = bpy.context.scene.tera_selected_group
    length = len(selected_group_collection.objects)
    if (length > 0 and selected_group_collection.tera_block_index < length):
        return selected_group_collection.objects[selected_group_collection.tera_block_index]
    return None
