import bpy

def get_group_name(coll):
    coll_name = coll.name.split('_',1)
    if(len(coll_name) == 2 and coll_name[0] == 'blocks'):
        return coll_name[1]
    return None

def get_groups():
    result = []
    for collection in bpy.data.collections:
        split_name = collection.name.split('_',1)
        if(len(split_name) == 2 and split_name[0] == 'blocks'):
            result.append(collection)
    return result
