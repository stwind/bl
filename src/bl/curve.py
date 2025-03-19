from .util import set_attrs


def add(D, lines, name="curve", ctype="CURVE", stype="POLY", cyclic=False, **kw):
    cu = D.curves.new(name, ctype)
    cu.dimensions = "3D"
    for points in lines:
        spline = cu.splines.new(type=stype)
        spline.points.add(len(points) - 1)
        for i, p in enumerate(points):
            spline.points[i].co = (*p, 1)
        spline.use_cyclic_u = cyclic
        spline.use_cyclic_v = cyclic
    return set_attrs(cu, **kw)
