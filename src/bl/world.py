def add(D, name, use_nodes=True):
    world = D.worlds.new(name)
    world.use_nodes = use_nodes
    return world


def use_environment(world, image, strength=0.1, rotation=(0, 0, 0)):
    tree = world.node_tree

    env = tree.nodes.new("ShaderNodeTexEnvironment")
    env.image = image
    bg = tree.nodes["Background"]
    bg.inputs["Strength"].default_value = strength
    tree.links.new(env.outputs["Color"], bg.inputs["Color"])

    tc = tree.nodes.new("ShaderNodeTexCoord")
    mapping = tree.nodes.new("ShaderNodeMapping")
    mapping.vector_type = "POINT"
    mapping.inputs["Rotation"].default_value = rotation
    tree.links.new(tc.outputs["Generated"], mapping.inputs["Vector"])
    tree.links.new(mapping.outputs["Vector"], env.inputs["Vector"])

    hsv = tree.nodes.new("ShaderNodeHueSaturation")
    hsv.inputs["Hue"].default_value = 0
    hsv.inputs["Saturation"].default_value = 0
    hsv.inputs["Value"].default_value = 0.03
    bg1 = tree.nodes.new("ShaderNodeBackground")
    tree.links.new(hsv.outputs["Color"], bg1.inputs["Color"])

    lp = tree.nodes.new("ShaderNodeLightPath")
    mix = tree.nodes.new("ShaderNodeMixShader")
    tree.links.new(lp.outputs["Is Camera Ray"], mix.inputs["Fac"])
    tree.links.new(bg.outputs["Background"], mix.inputs[1])
    tree.links.new(bg1.outputs["Background"], mix.inputs[2])

    tree.links.new(mix.outputs["Shader"], tree.nodes["World Output"].inputs["Surface"])
