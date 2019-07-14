import json
import re
from _ctypes import PyObj_FromPtr
import bpy, bmesh
from bpy.props import BoolProperty, StringProperty
import bpy_extras.io_utils
import json
import datetime
import mathutils



class NoIndent(object):
    """ Value wrapper. """

    def __init__(self, value):
        self.value = value


class Encoder(json.JSONEncoder):
    FORMAT_SPEC = '@@{}@@'
    regex = re.compile(FORMAT_SPEC.format(r'(\d+)'))

    def __init__(self, **kwargs):
        # Save copy of any keyword argument values needed for use here.
        self.__sort_keys = kwargs.get('sort_keys', None)
        super(Encoder, self).__init__(**kwargs)

    def default(self, obj):
        return (self.FORMAT_SPEC.format(id(obj)) if isinstance(obj, NoIndent)
                else super(Encoder, self).default(obj))

    def encode(self, obj):
        format_spec = self.FORMAT_SPEC  # Local var to expedite access.
        json_repr = super(Encoder, self).encode(obj)  # Default JSON.

        # Replace any marked-up object ids in the JSON repr with the
        # value returned from the json.dumps() of the corresponding
        # wrapped Python object.
        for match in self.regex.finditer(json_repr):
            # see https://stackoverflow.com/a/15012814/355230
            id = int(match.group(1))
            no_indent = PyObj_FromPtr(id)
            json_obj_repr = json.dumps(no_indent.value, sort_keys=self.__sort_keys)

            # Replace the matched id string with json formatted representation
            # of the corresponding Python object.
            json_repr = json_repr.replace(
                '"{}"'.format(format_spec.format(id)), json_obj_repr)

        return json_repr

class TERA_SHAPE_OT_shape_exporter(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    bl_idname = "tera.export_shape"
    bl_label = "Export Terasology Block Shape"

    filename_ext = ".shape"
    filter_glob = StringProperty(default="*.shape", options={'HIDDEN'})

    apply_modifiers = BoolProperty(
        name="Apply Modifiers",
        description="Apply Modifiers to the exported mesh",
        default=True)


    @classmethod
    def poll(cls, context):
        return context.active_object != None

    def meshify(self, bm):
        mesh = bpy.data.meshes.new('temp')
        bm.to_mesh(mesh)

        result = {}
        result['vertices'] = []
        result['normals'] = []
        result['texcoords'] = []
        result['faces'] = []

        for vert in mesh.vertices:
            result['vertices'].append(NoIndent([-vert.co.x, vert.co.y, vert.co.z]))
            result['normals'].append(NoIndent([-vert.normal.x, vert.normal.y, vert.normal.z]))

        uv_active = mesh.uv_layers.active
        for layer in uv_active.data:
            result['texcoords'].append(NoIndent([layer.uv[0],1.0 - layer.uv[1]]))
        mesh.calc_loop_triangles()
        for tri in mesh.loop_triangles:
            result['faces'].append(NoIndent([i for i in tri.loops]))

        bpy.data.meshes.remove(mesh)

        return result


    def execute(self, context):
        path = bpy.path.ensure_ext(self.filepath, self.filename_ext)

        if (context.scene.tera_shape_select_index > 0 and context.scene.tera_shape_select_index < len(bpy.data.objects)):
            selected_object = bpy.data.objects[context.scene.tera_shape_select_index]
            shape = selected_object.tera_shape

            result = {}
            result['displayName'] = shape.display_name
            result['author'] = shape.author

            now = datetime.datetime.now()
            result['exportDate'] = '{:%Y-%m-%d %H:%M:%S}'.format(now)

            meshes = {}
            is_full_side = {}
            for child in selected_object.children:
                if(child.type == 'MESH'):
                    if(child.data.tera_mesh.part not in meshes):
                        meshes[child.data.tera_mesh.part] = bmesh.new()
                        is_full_side[child.data.tera_mesh.part] = False

                    is_full_side[child.data.tera_mesh.part] = (True if is_full_side[child.data.tera_mesh.part] else child.data.tera_mesh.full_side)

                    mesh = bpy.data.meshes.new('temp')

                    temp = bmesh.new()
                    temp.from_mesh(child.data)
                    bmesh.ops.transform(temp,matrix=selected_object.matrix_world.inverted() @ child.matrix_world,verts=temp.verts)
                    temp.to_mesh(mesh)

                    meshes[child.data.tera_mesh.part].from_mesh(mesh)
                    bpy.data.meshes.remove(mesh)
                    temp.free()

            for key,value in meshes.items():
                # bmesh.ops.transform(value, matrix=matrix_world.inverted(), verts=value.verts)
                result[key] = self.meshify(value)
                result[key]['fullSide'] = is_full_side[key]
                value.free()

            result['collision'] = {}
            hasColliders = False
            if(shape.aabb):
                hasColliders = True
                if('colliders' not in result['collision']):
                    result['collision']['colliders'] = []

                for aabb in shape.aabb:
                    result['collision']['colliders'].append({
                        'type' : 'AABB',
                        'position' : NoIndent([aabb.origin[0],aabb.origin[1],aabb.origin[2]]),
                        'extents': NoIndent([aabb.extent[0], aabb.extent[1], aabb.extent[2]])
                    })

            if (hasColliders == True):
                result['collision']["symmetric"] = shape.symmetric
                result['collision']['yawSymmetric'] = shape.yaw_symmetric
                result['collision']['pitchSymmetric'] = shape.pitch_symmetric
                result['collision']['rollSymmetric'] = shape.roll_symmetric
                result['collision']['convexHull'] = shape.convex_hull

            file = open(path, "w", encoding="utf8")
            print("saving complete: %r " % path)
            file.write(json.dumps(result,indent=2, separators=(',', ': '),cls=Encoder))
            file.close()
        # filepath = self.filepath

        # from . import _export_block_shape
        # keywords = self.as_keywords(ignore=("filter_glob", "check_existing"))
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        layout.row().label(text="Selected Shape")
        layout.row().prop(self, "apply_modifiers")

        row = self.layout.row()
        row.template_list("TERA_SHAPES_UL_shape", "", bpy.data, "objects", context.scene, "tera_shape_select_index")
