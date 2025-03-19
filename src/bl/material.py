from .node_tree import add_node, connect


def add(D, name, use_nodes=True, clear=True):
    mat = D.materials.new(name)
    mat.use_nodes = use_nodes
    if clear:
        mat.node_tree.nodes.clear()
    return mat


def color_attribute(mat, attr_name):
    tree = mat.node_tree

    attr = add_node(tree, "ShaderNodeAttribute", attrs={"attribute_name": attr_name})
    out = add_node(tree, "ShaderNodeOutputMaterial")

    connect(tree, [(attr.outputs["Color"], out.inputs["Surface"])])

    return mat


def diffuse(mat, color=(1, 1, 1), roughness=1):
    tree = mat.node_tree

    diff = add_node(
        tree, "ShaderNodeBsdfDiffuse", {"Color": (*color, 1), "Roughness": roughness}
    )
    out = add_node(tree, "ShaderNodeOutputMaterial")

    connect(tree, [(diff.outputs["BSDF"], out.inputs["Surface"])])

    return mat


def diffuse_ao(
    mat, color=(1, 1, 1), roughness=1, ao_dist=0.1, ao_color=(0.1, 0.1, 0.1)
):
    tree = mat.node_tree

    diff = add_node(
        tree, "ShaderNodeBsdfDiffuse", {"Color": (*color, 1), "Roughness": roughness}
    )

    ao = add_node(tree, "ShaderNodeAmbientOcclusion", {"Distance": ao_dist})
    mix = add_node(tree, "ShaderNodeMixShader")
    diffuse = add_node(
        tree, "ShaderNodeBsdfDiffuse", {"Color": (*ao_color, 1), "Roughness": roughness}
    )

    out = add_node(tree, "ShaderNodeOutputMaterial")

    connect(
        tree,
        [
            (ao.outputs["Color"], mix.inputs["Fac"]),
            (diffuse.outputs["BSDF"], mix.inputs[1]),
            (diff.outputs["BSDF"], mix.inputs[2]),
            (mix.outputs["Shader"], out.inputs["Surface"]),
        ],
    )

    return mat


def normal(mat):
    tree = mat.node_tree

    tc = add_node(tree, "ShaderNodeTexCoord")
    mul = add_node(
        tree, "ShaderNodeVectorMath", {1: (0.5, 0.5, 0.5)}, {"operation": "MULTIPLY"}
    )
    add = add_node(
        tree, "ShaderNodeVectorMath", {1: (0.5, 0.5, 0.5)}, {"operation": "ADD"}
    )
    out = add_node(tree, "ShaderNodeOutputMaterial")

    connect(
        tree,
        [
            (tc.outputs["Normal"], mul.inputs[0]),
            (mul.outputs["Vector"], add.inputs[0]),
            (add.outputs["Vector"], out.inputs["Surface"]),
        ],
    )

    return mat
