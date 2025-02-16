def connect(tree, links):
    for k, v in links:
        tree.links.new(k, v)
