def connect(tree, links):
    for k, v in links:
        tree.links.new(k, v)


def add_node(tree, type, inputs={}, attrs={}):
    node = tree.nodes.new(type)
    for k, v in inputs.items():
        node.inputs[k].default_value = v
    for k, v in attrs.items():
        setattr(node, k, v)
    return node
