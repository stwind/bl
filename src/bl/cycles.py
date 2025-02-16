def setup(prefs, compute_device_type="OPTIX"):
    cprefs = prefs.addons["cycles"].preferences
    cprefs.compute_device_type = compute_device_type
    for d in cprefs.devices:
        d.use = d.type == compute_device_type
