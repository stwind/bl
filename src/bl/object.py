import os
import bpy
import mathutils as mu


def look_at(obj, target=mu.Vector((0, 0, 0)), track="-Z", up="Y"):
    obj.rotation_euler = (
        (target - obj.location).normalized().to_track_quat(track, up).to_euler()
    )
    return obj


def import_vdb(D, path, name=None, scale=(1, 1, 1), **kw):
    obj_name = os.path.splitext(os.path.basename(path))[0]
    bpy.ops.object.volume_import(filepath=path, **kw)
    obj = D.objects[obj_name]
    obj.name = name or obj_name
    obj.scale = scale
    return obj


def add_node_group_modifier(obj, name, group):
    mod = obj.modifiers.new(name=name, type="NODES")
    mod.node_group = group
    return mod
