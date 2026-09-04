from machine import Pin,PWM,ADC
import time

foto1 = ADC(Pin(32))
foto2 = ADC(Pin(33))

foto1.atten(ADC.ATTN_11DB)
foto1.width(ADC.WIDTH_10BIT)

foto2.atten(ADC.ATTN_11DB)
foto2.width(ADC.WIDTH_10BIT)

servo = PWM(Pin(13, mode=Pin.OUT))
servo.freq(50)
luminosidad = 30
z=75
def movimiento():
    global z
    if valor > valor1 and valor > luminosidad:
        z=z+1
        if z>=123:
            z=123
    elif valor1 > valor and valor1 > luminosidad:
        z=z-1
        if z<=26:
            z=26

while True:
    dato1 = foto1.read()
    dato2 = foto2.read()

    valor = int(abs(dato1/10))
    valor1 = int(abs(dato2/10))

    if valor <= luminosidad and valor1 <= luminosidad:
        servo.duty(z)
    else:
        movimiento()
    servo.duty(z)
    print(valor)
    print(valor1)
    time.sleep_ms(15)
