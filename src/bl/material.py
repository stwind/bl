def add(D, name, use_nodes=True):
    mat = D.materials.new(name)
    mat.use_nodes = use_nodes
    return mat
