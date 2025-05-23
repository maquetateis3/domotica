from microbit import *

while True:
    if button_a.is_pressed():
        pin14.write_digital(1)
        music.play(music.RINGTONE)
        sleep(5000)
        pin14.write_digital(0)
