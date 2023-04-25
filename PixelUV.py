bl_info = {
    "name": "PixelUV",
    "description": "Helps pack UVs in a seperate channel",
    "author": "Cvrrytrash",
    "version": (0, 0),
    "blender": (3, 0, 0),
    "location": "Toolbar",
    "category": "Object"
}

import bpy

from operator import attrgetter

from bpy.props import (StringProperty, PointerProperty)

from bpy.types import (Panel, PropertyGroup,)

class Properties(PropertyGroup):
    zone_tag_input: StringProperty(
        default = "bz",
        name="Zone Identifier",
        description="identifying tag of the zone vertex groups"
    )

class Operators(bpy.types.Operator):
    bl_idname = "my.addon_operator"
    bl_label = "Generate Pixel UV map"

    def execute(self, context):
        mytool = context.scene.my_tool

        collection = context.collection
        zone_tag = mytool.zone_tag_input
        objects = []

        #getting_objects_from_collection
        for obj in collection.objects:
            objects.append(obj)
            vg_names = [vg.name for vg in obj.vertex_groups if vg.name[:len(zone_tag)] == zone_tag]

        objects.sort(key = attrgetter('name'))
        levels = len(objects)

        for lvl, obj in enumerate(objects):
            if "pixelUVmap" not in obj.data.uv_layers:
                obj.data.uv_layers.new(name="pixelUVmap")

            uvMap = obj.data.uv_layers["pixelUVmap"]

        return {'FINISHED'}

class PixelUV(Panel):
    bl_label = "PixelUV"
    bl_idname = "CVRRY_ADON_PT_layout"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PixelUV"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "zone_tag_input")
        layout.operator("my.addon_operator")

classes = (
    Properties,
    Operators,
    PixelUV
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=Properties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
