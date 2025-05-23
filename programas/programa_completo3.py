"""Programa completo da fila 3 para a maqueta domótica. 
Autores:Marta,Asier,Sara M 
"""
#P1 maqueta. Sensor de temperatura#

from microbit import *
import neopixel
import music

pir = pin15.rea_digital()
led = pin14
np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13
np.clear()
rele = pin16  # relé conectado ao pin 16

while True:
    temperatura = temperature()  # gardamos valor da temperatura

    if temperatura > 18:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(0)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        rele.write_digital(1)  # Apagar o LED normal

    sleep(1000)  # Esperar 1 segundo

#P3 maqueta#


while True:
    if button_a.is_pressed():
        pin14.write_digital(1)
        music.play(music.RINGTONE)
        sleep(5000)
        pin14.write_digital(0)

#Programa 4#

from microbit import *
pin2.set_analog_period(20) 
pin2.write_analog(1)
porta=0
While True:
  if button_b.is_pressed():
  if porta==0:
    porta=1
  else:
    porta=0

#Programa 5#

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
            np[1] = (0, 0, 0)
            np.show()
            led.write_digital(1)
            np[0] = (0, 255, 0)
            np[1] = (0, 255, 0)
            np.show()
            sleep(500)
            display.clear
            np.clear
    
