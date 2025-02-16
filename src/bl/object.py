import mathutils as mu


def look_at(obj, target=mu.Vector((0, 0, 0)), track="-Z", up="Y"):
    obj.rotation_euler = (
        (target - obj.location).normalized().to_track_quat(track, up).to_euler()
    )
    return obj
