
from bpy.types import Operator
from bpy_extras.io_utils import ExportHelper

from bpy.props import BoolProperty, StringProperty
import json
import datetime
from mathutils import Vector
from . import constants
from . import json_no_indent

class ExportToBlockShape(Operator, ExportHelper):
    bl_idname = "export_scene.collection"
    bl_label = "Export Collection of Terasology Block Shape"

    filename_ext = ".shape"
    filter_glob = StringProperty(default="*.shape", options={'HIDDEN'})

    apply_modifiers = BoolProperty(
        name="Apply Modifiers",
        description="Apply Modifiers to the exported mesh",
        default=True)

    def execute(self, context):
        pass