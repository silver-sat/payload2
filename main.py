
from hardware import get_hardware

from files import photo_filename, most_recent_photo, remove_photo
from camera import setup_camera, take_photo
from twitter import setup_twitter, send_text_tweet, send_photo_tweet, \
                    make_twitter_status_text, make_twitter_status_for_photo

MODEPINS = (10,11,12)
UPPINS = (20,21,22)

rpi = get_hardware()

def main():
    
    rpi.setup_gpio_pins()
    
    rpi.gpio_pins_set_high(*UPPINS)
    
    if rpi.gpio_pins_are_high(*MODEPINS):
        if setup_camera():
            filename = photo_filename()
            if filename:
                take_photo(filename)
    else:
        if setup_twitter():
            filename = most_recent_photo()
            if not filename:
                message = make_twitter_status_text()
                send_text_tweet(message)
            else:
                message = make_twitter_status_for_photo()
                if send_photo_tweet(message, filename):
                    remove_photo(filename)
        
if __name__ == "__main__":
    main()
        
        