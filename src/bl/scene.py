def setup(
    scene,
    size=(640, 360),
    transparent=False,
    preview_samples=64,
    samples=128,
    use_adaptive_sampling=True,
    use_denoising=True,
    pixel_filter_type="BLACKMAN_HARRIS",
    view_transform="AgX",
    look="None",
    display_device="sRGB",
    max_bounces=12,
    diffuse_bounces=4,
    engine="CYCLES",
    device="GPU",
    filepath="output.png",
    color_mode="RGBA",
    compression=0,
):
    scene.render.engine = engine
    scene.cycles.device = device
    scene.cycles.samples = samples
    scene.cycles.preview_samples = preview_samples
    scene.cycles.use_adaptive_sampling = use_adaptive_sampling
    scene.cycles.use_denoising = use_denoising
    scene.cycles.pixel_filter_type = pixel_filter_type
    scene.cycles.max_bounces = max_bounces
    scene.cycles.diffuse_bounces = diffuse_bounces
    scene.render.resolution_x = size[0]
    scene.render.resolution_y = size[1]
    scene.render.filepath = filepath
    scene.render.film_transparent = transparent
    scene.render.image_settings.compression = compression
    scene.render.image_settings.color_mode = color_mode
    scene.view_settings.view_transform = view_transform
    scene.view_settings.look = look
    scene.display_settings.display_device = display_device
