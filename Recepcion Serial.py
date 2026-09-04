from machine import Pin,ADC,PWM
import machine
import time
import uos

uart = machine.UART(1, baudrate=115200, tx=17, rx=16)
led = machine.Pin(19,machine.Pin.OUT)
pot2 = ADC(Pin(32))
pot2.atten(ADC.ATTN_11DB)
rojo = PWM(Pin(13), freq=1000)
verde = PWM(Pin(12), freq=1000)
azul = PWM(Pin(14), freq=1000)

led.off()

def rgb():
    print (cadena)
    if cadena == 'verde':
        verde.duty(250)
        rojo.duty(0)
        azul.duty(0)
    elif cadena == 'rojo':
        verde.duty(0)
        rojo.duty(250)
        azul.duty(0)
    elif cadena == 'azul':
        verde.duty(0)
        rojo.duty(0)
        azul.duty(250)
    elif cadena == 'magenta':
        verde.duty(0)
        rojo.duty(200)
        azul.duty(167)

while True:
    datos=uart.readline()
    lectura = (pot2.read()/(4096/3.3))
    if datos:
        cadena=datos.decode('utf-8').strip()
        rgb()
        #print(cadena)
        if cadena == 'L2A':
            led.on()
            uart.write("L2A")
        elif cadena == 'L2O':
            led.off()
            uart.write("L2O")
        elif cadena == 'S2':
            uart.write("@{:.2f}#".format(lectura))
    time.sleep(0.1)

