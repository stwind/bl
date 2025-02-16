import numpy as np
import bmesh


def update_mesh(mesh):
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.to_mesh(mesh)
    bm.free()


def get_verts(mesh):
    verts = np.zeros((len(mesh.vertices) * 3), dtype=np.float32)
    mesh.vertices.foreach_get("co", verts)
    return verts.reshape(-1, 3)


def normalize_verts(mesh):
    verts = get_verts(mesh)
    verts -= verts.mean(0)
    verts /= np.linalg.norm(verts, axis=-1).max()
    mesh.vertices.foreach_set("co", verts.ravel())
    update_mesh(mesh)


def get_extent(mesh):
    verts = get_verts(mesh)
    return verts.min(0), verts.max(0)
