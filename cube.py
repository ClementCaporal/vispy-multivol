import numpy as np
from vispy import app, scene, io

from multivol import MultiVolume
from multivol import get_translucent_cmap

# Prepare canvas
canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)
canvas.measure_fps()

# Set up a viewbox to display the image with interactive pan/zoom
view = canvas.central_widget.add_view()

# Create rgb_cube
size = 256
step = np.linspace(0, 255, size)
rgb_cube = np.meshgrid(step, step, step)

# Set whether we are emulating a 3D texture
emulate_texture = False

reds = get_translucent_cmap(1, 0, 0)
blues = get_translucent_cmap(0, 0, 1)
greens = get_translucent_cmap(0, 1, 0)

volumes = [(rgb_cube[0], None, reds),
            (rgb_cube[1], None, greens),
            (rgb_cube[2], None, blues)]
volume1 = MultiVolume(volumes, parent=view.scene, threshold=0.225,
                               emulate_texture=emulate_texture, n_volume_max=3)

# Create three cameras (Fly, Turntable and Arcball)
fov = 60.
cam2 = scene.cameras.TurntableCamera(parent=view.scene, fov=fov,
                                     name='Turntable')
view.camera = cam2  # Select turntable at first

if __name__ == '__main__':
    print(__doc__)
    app.run()