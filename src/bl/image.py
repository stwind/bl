import os
import bpy


def open(D, path):
    bpy.ops.image.open(filepath=path)
    return D.images[os.path.basename(path)]
