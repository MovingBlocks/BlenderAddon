import bpy
import bpy_extras.io_utils
import json
import bmesh

parts = ["Center", "Top", "Bottom", "Front", "Back", "Left", "Right"]


class TERA_SHAPE_OT_shape_importer(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    bl_idname = "tera.import_shape"
    bl_label = "Import Terasology Block Shape"

    filename_ext = ".shape"

    def execute(self, context):
        path = bpy.path.ensure_ext(self.filepath, self.filename_ext)
        nameDisplay = self.filepath[self.filepath.rfind("\\") + 1:self.filepath.rfind(".")]

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='OBJECT')

        if bpy.ops.object.select_all.poll():
            bpy.ops.object.select_all(action='DESELECT')

        file = open(path)
        payload = json.loads(file.read())

        o = bpy.data.objects.new('shape_' + nameDisplay, None)
        o.empty_display_type = 'PLAIN_AXES'
        o.tera_shape.display_name = nameDisplay
        bpy.context.collection.objects.link(o)

        if 'displayName' in payload:
            o.tera_shape.display_name = payload['displayName']
        if 'author' in payload:
            o.tera_shape.author = payload['author']

        for part in parts:
            if(part.lower() in payload):
                sub_payload = payload[part.lower()]

                bm = bmesh.new()
                verticies = []
                for v in sub_payload['vertices']:
                    verticies.append(bm.verts.new((-v[0], v[2], v[1])))

                bm.verts.ensure_lookup_table()
                bm.verts.index_update()

                for face_index in sub_payload['faces']:
                    bm.faces.new([verticies[i] for i in face_index])

                uv_layer = bm.loops.layers.uv.new()
                for face in bm.faces:
                    for loop in face.loops:
                        uv = sub_payload['texcoords'][loop.vert.index]
                        loop[uv_layer].uv = (uv[0], 1.0 - uv[1])

                mesh = bpy.data.meshes.new("mesh")
                bm.to_mesh(mesh)
                object = bpy.data.objects.new(part.capitalize(), mesh)
                bpy.context.collection.objects.link(object)
                object.data.tera_mesh.part = part.lower()
                object.parent = o
                bm.free()

                if 'fullSide' in sub_payload:
                    object.data.tera_mesh.full_side = sub_payload['fullSide']
                else:
                    object.data.tera_mesh.full_side = False

        payload_collision = None
        if 'collision' in payload:
            payload_collision = payload['collision']
        if(payload_collision is not None):
            if 'symmetric' in payload_collision:
                o.tera_shape.symmetric = payload_collision['symmetric']
            if 'yawSymmetric' in payload_collision:
                o.tera_shape.yaw_symmetric = payload_collision['yawSymmetric']
            if 'pitchSymmetric' in payload_collision:
                o.tera_shape.pitch_symmetric = payload_collision['pitchSymmetric']
            if 'rollSymmetric' in payload_collision:
                o.tera_shape.roll_symmetric = payload_collision['rollSymmetric']
            if 'convexHull' in payload_collision:
                o.tera_shape.convex_hull = payload_collision['convexHull']
            else:
                if 'colliders' in payload_collision:
                    for collider in payload_collision['colliders']:
                        if(collider['type'] == 'AABB'):
                            p = collider['position']
                            e = collider['extents']
                            aabb = o.tera_shape.aabb.add()
                            aabb.label = "ImportedAABB"
                            aabb.origin = [p[0], p[2], p[1]]
                            aabb.extent = [e[0], e[2], e[1]]
                        elif collider['type'] == 'Sphere':
                            p = collider['position']
                            r = collider['radius']
                            bpy.ops.mesh.primitive_uv_sphere_add(
                                segments=16, location=(-p[0], p[1], p[2]), size=r)
                            bpy.ops.object.transform_apply(
                                location=True, scale=True, rotation=True)

        return {'FINISHED'}
