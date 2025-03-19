from .util import set_attrs


def connect(tree, links):
    for k, v in links:
        tree.links.new(k, v)


def add_node(tree, type, inputs={}, attrs={}):
    node = tree.nodes.new(type)
    for k, v in inputs.items():
        node.inputs[k].default_value = v
    return set_attrs(node, **attrs)
