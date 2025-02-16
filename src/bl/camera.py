from bpy import context as C


def add(D, name="Camera", lens=120, clip_start=0.1, clip_end=1000):
    camera = D.cameras.new(name)
    camera.lens = lens
    camera.clip_start = clip_start
    camera.clip_end = clip_end
    return camera


def add_ortho(
    D, size=(C.scene.render.resolution_x, C.scene.render.resolution_y), scale=1, **kw
):
    camera = add(D, **kw)
    camera.type = "ORTHO"
    camera.ortho_scale = max(*size) / min(*size) * 2 * scale
    return camera
