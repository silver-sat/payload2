
from hardware import get_hardware

rpi = get_hardware()

def setup_camera():
    rpi.setup_camera()

def take_photo(image_filename):
    rpi.take_photo(image_filename)

