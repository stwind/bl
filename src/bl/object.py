import mathutils as mu
from .util import set_attrs


def look_at(obj, target=mu.Vector((0, 0, 0)), track="-Z", up="Y"):
    obj.rotation_euler = (
        (target - obj.location).normalized().to_track_quat(track, up).to_euler()
    )
    return obj


def add(D, data, name=None, **kw):
    name = name or data.name
    obj = D.objects.new(name, data)
    return set_attrs(obj, **kw)


def add_node_group_modifier(obj, name, group):
    mod = obj.modifiers.new(name=name, type="NODES")
    mod.node_group = group
    return mod


def add_collection_instance(D, coll, name=None):
    instance = D.objects.new(name=name or coll.name, object_data=None)
    instance.instance_type = "COLLECTION"
    instance.instance_collection = coll
    return instance
