"""Programa 4 para la maqueta de domótica"""
Autor:Sara Miguéns
Data: 7 de mayo de 2025

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
  sleep(100)
