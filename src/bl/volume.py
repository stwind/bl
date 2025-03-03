import os


def add(D, path, name=None):
    name = name or os.path.splitext(os.path.basename(path))[0]
    vol = D.volumes.new(name)
    vol.filepath = path
    return vol
