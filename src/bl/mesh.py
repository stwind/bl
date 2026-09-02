import numpy as np
import bmesh


def update(mesh):
    bm = bmesh.new()
    bm.from_mesh(mesh)
    bm.to_mesh(mesh)
    bm.free()


def get_vertices(mesh):
    verts = np.zeros((len(mesh.vertices) * 3), dtype=np.float32)
    mesh.vertices.foreach_get("co", verts)
    return verts.reshape(-1, 3)


def get_triangles(mesh, dtype=np.uint32):
    triangles = np.zeros((len(mesh.loop_triangles) * 3), dtype=dtype)
    mesh.loop_triangles.foreach_get("vertices", triangles)
    return triangles.reshape(-1, 3)


def normalize_verts(mesh):
    verts = get_vertices(mesh)
    verts -= verts.mean(0)
    verts /= np.linalg.norm(verts, axis=-1).max()
    mesh.vertices.foreach_set("co", verts.ravel())
    update(mesh)


def get_aabb(mesh):
    aabb = np.zeros((2, 3), dtype="f4")
    for v in mesh.vertices:
        aabb[0, 0], aabb[1, 0] = min(aabb[0, 0], v.co.x), max(aabb[1, 0], v.co.x)
        aabb[0, 1], aabb[1, 1] = min(aabb[0, 1], v.co.y), max(aabb[1, 1], v.co.y)
        aabb[0, 2], aabb[1, 2] = min(aabb[0, 2], v.co.z), max(aabb[1, 2], v.co.z)
    return aabb


def add(D, name, verts, faces=[], edges=[], smooth=True):
    mesh = D.meshes.new(name)
    mesh.from_pydata(verts, edges, faces)
    if smooth:
        mesh.shade_smooth()
    return mesh


def add_color_attribute(mesh, name, data, type="FLOAT_COLOR", domain="POINT"):
    attr = mesh.color_attributes.new(name, type, domain)
    attr.data.foreach_set("color", data.ravel())
    return attr


PROP_NAME = {
    "FLOAT": "value",
    "INT": "value",
    "INT8": "value",
    "BOOLEAN": "value",
    "FLOAT_VECTOR": "vector",
    "FLOAT2": "vector",
    "FLOAT_COLOR": "color",
    "BYTE_COLOR": "color",
    "QUATERNION": "value",
    "FLOAT4X4": "value",
}


def add_attribute(mesh, name, data, type="FLOAT", domain="POINT"):
    attr = mesh.attributes.new(name, type, domain)
    attr.data.foreach_set(PROP_NAME[type], data)
    return attr


DATATYPE_SIZE = {
    "FLOAT": 1,
    "INT": 1,
    "INT8": 1,
    "BOOLEAN": 1,
    "FLOAT_VECTOR": 3,
    "FLOAT2": 2,
    "FLOAT_COLOR": 4,
    "BYTE_COLOR": 4,
    "QUATERNION": 4,
    "FLOAT4X4": 16,
}

DATATYPE_DTYPE = {
    "FLOAT": np.float32,
    "INT": np.int32,
    "INT8": np.int8,
    "BOOLEAN": np.bool,
    "FLOAT_VECTOR": np.float32,
    "FLOAT2": np.float32,
    "FLOAT_COLOR": np.float32,
    "BYTE_COLOR": np.float32,
    "QUATERNION": np.float32,
    "FLOAT4X4": np.float32,
}


def get_attribute_data(mesh, name):
    attr = mesh.attributes[name]
    data_type = attr.data_type
    data = np.zeros(
        DATATYPE_SIZE[data_type] * len(attr.data), dtype=DATATYPE_DTYPE[data_type]
    )
    attr.data.foreach_get(PROP_NAME[data_type], data)
    return data
