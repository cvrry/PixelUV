bl_info = {
    "name": "PixelUV",
    "description": "Helps pack UVs in a seperate channel",
    "author": "Cvrrytrash",
    "version": (1, 2 ),
    "blender": (3, 0, 0),
    "location": "Toolbar",
    "category": "Object"
}

import bpy
#import bmesh

#are you modifying the add-on? have fun!

from operator import attrgetter

from bpy.props import (StringProperty, PointerProperty)

from bpy.types import (Panel, PropertyGroup,)

def check_if_belongs(obj, verts, vg_name):
    for i in verts:
        try:
            obj.vertex_groups[vg_name].weight(i)
        except:
            return False
        
    return True

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
        zone_tag_len = len(zone_tag)
        objects = []
        vg_names_list = []

        uv_map_name = 'pixelUVmap'

        print("starting\n")

        #getting_objects_&_vertex_groups_from_collection
        for obj in collection.objects:
            objects.append(obj)
            vg_names_list.append([vg.name for vg in obj.vertex_groups if vg.name[:zone_tag_len] == zone_tag])

        objects.sort(key = attrgetter('name'))
        num_levels = len(objects)
        num_zones = max(len(vg_names) for vg_names in vg_names_list)

        #loop_for_each_obj_aka_level
        for lvl_id, obj in enumerate(objects):

            mesh = obj.data

            #checks_for_UV_map_exist_creates_if_absent
            if uv_map_name not in obj.data.uv_layers:
                obj.data.uv_layers.new(name=uv_map_name)

            uv_map = obj.data.uv_layers[uv_map_name]

            #loop_for_each_vertex_group_aka_zone
            for vg_name in vg_names_list[lvl_id]:
                zone_id = int(vg_name[zone_tag_len:])

                uv_coord = ((zone_id + 0.5)/num_zones,1 - (lvl_id + 0.5)/num_levels)

                for face in obj.data.polygons:
                    for loop in face.loop_indices:
                        if(check_if_belongs(obj, face.vertices, vg_name)):
                            uv_map.data[loop].uv = uv_coord

                print("[vertex group] ", vg_name, "set")
            
                    
            mesh.update()   
            print("[object] ",obj.name, "UV set\n")

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


#registers_classes
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