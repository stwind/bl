from .util import set_attrs


def use_collections(vl, collections=[]):
    for coll in vl.layer_collection.children:
        coll.exclude = coll.name not in collections

    return vl


def add(view_layers, name, cycles_use_pass_shadow_catcher=False, collections=[], **kw):
    vl = view_layers.new(name)
    vl.cycles.use_pass_shadow_catcher = cycles_use_pass_shadow_catcher

    use_collections(vl, collections)

    return set_attrs(vl, **kw)
