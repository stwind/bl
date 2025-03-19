import bpy


def print(C, *args):
    for area in C.screen.areas:
        if area.type != "CONSOLE":
            continue

        with C.temp_override(area=area):
            text = " ".join([str(arg) for arg in args])
            for line in text.split("\n"):
                bpy.ops.console.scrollback_append(text=line)


def set_attrs(obj, **kw):
    for k, v in kw.items():
        setattr(obj, k, v)
    return obj
