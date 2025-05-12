from microbit import*
import music


pir = pin15.rea_digital()
np = neopixel.NeoPixel(pin13)
led = pin14

while True:
    if pir ==1:
        music.play(music.RINGTONE)
        music.play(music.RINGTONE)
        sleep(500)
        for i in range(5):
            display.show(Image.ANGRY)
            led.write_digital(0)
            np[0] = (0, 0, 0)
            np.show()
            led.write_digital(1)
            np[0] = (0, 255, 0)
            np[1] = (0, 255, 0)
            np.show()
            sleep(500)
            display.clear
            np.clear
            sleep(500)
