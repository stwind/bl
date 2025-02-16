def add(D, name, type, shape="DISK", energy=5, size=1):
    light = D.lights.new(name, type)
    light.shape = shape
    light.energy = energy
    light.size = size
    return light
