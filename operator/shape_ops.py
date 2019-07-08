
def get_groups(self, context):
    return {(c.name,c.name,'') for c in bpy.data.collections}

def on_update_groups(self, context):
    pass

def get_shapes(self, context):
    coll = self.collection
    return {(ob.name,ob.name,'') for ob in bpy.data.collections[coll].objects if (ob.parent == None and ob.type in ['EMPTY'])}

def on_update_shapes(self, context):
    pass

class ShapeOps:
    collection: EnumProperty(
        name='block group',
        description='The collection to reference.',
        items=get_groups,
        update=on_update_groups)

    shapes:  EnumProperty(
        name="name",
        description='Shape to remove.',
        items=get_shapes,
        update=on_update_shapes)