from .util import set_attrs
from .node_tree import add_node, connect


def add(D, name, sockets={}):
    group = D.node_groups.new(name, "GeometryNodeTree")
    group.is_modifier = True
    group.interface.new_socket(
        "Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )
    group.interface.new_socket(
        "Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )
    group_input = group.nodes.new("NodeGroupInput")
    group_output = group.nodes.new("NodeGroupOutput")
    group_output.is_active_output = True

    group.links.new(group_input.outputs[0], group_output.inputs[0])

    for name, sock in sockets.items():
        socket = group.interface.new_socket(
            name, in_out=sock["in_out"], socket_type=sock["socket_type"]
        )
        set_attrs(socket, **sock.get("attrs", {}))

    return group


def add_lights(D, coll):
    group = add(
        D,
        "lights",
        {
            "Target": {
                "in_out": "INPUT",
                "socket_type": "NodeSocketVector",
                "attrs": {"subtype": "XYZ"},
            }
        },
    )
    group.links.clear()

    iop = add_node(group, "GeometryNodeInstanceOnPoints", {"Pick Instance": True})
    ci = add_node(
        group,
        "GeometryNodeCollectionInfo",
        {
            "Collection": coll,
            "Separate Children": True,
            "Reset Children": True,
        },
    )
    pos = add_node(group, "GeometryNodeInputPosition")
    sub = add_node(group, "ShaderNodeVectorMath", attrs={"operation": "SUBTRACT"})
    artv = add_node(group, "FunctionNodeAlignRotationToVector")

    connect(
        group,
        [
            (group.nodes["Group Input"].outputs["Geometry"], iop.inputs["Points"]),
            (iop.outputs["Instances"], group.nodes["Group Output"].inputs["Geometry"]),
            (ci.outputs["Instances"], iop.inputs["Instance"]),
            (pos.outputs["Position"], sub.inputs[0]),
            (group.nodes["Group Input"].outputs["Target"], sub.inputs[1]),
            (sub.outputs["Vector"], artv.inputs["Vector"]),
            (artv.outputs["Rotation"], iop.inputs["Rotation"]),
        ],
    )

    return group
