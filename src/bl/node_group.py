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
        for k, v in sock.get("attrs", {}).items():
            setattr(socket, k, v)

    return group
