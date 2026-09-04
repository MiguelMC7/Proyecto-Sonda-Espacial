from machine import Pin, ADC
import machine as mc
import time
import uos

uart = mc.UART(1, baudrate=115200, tx=17, rx=16)
led = mc.Pin(33, mc.Pin.OUT)
pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)

led.off()
x = 0
y = 0

#Variables rgb
z = 0
i = 0
j = 0
m = 0

def rgbenvio(timer):
    global z,i,j,m
    lectura = (pot.read()/(4096/3.3))
    if z == 0 and lectura <= 1:
        uart.write("verde")
        z = 1
        i = 0
        j = 0
        m = 0
    elif i == 0 and lectura > 1 and lectura <= 2:
        uart.write("rojo")
        z = 0
        i = 1
        j = 0
        m = 0
    elif j == 0 and lectura >2 and lectura <= 2.5:
        uart.write("azul")
        z = 0
        i = 0
        j = 1
        m = 0
    elif m == 0 and lectura > 2.5 and lectura <= 3.3:
        uart.write("magenta")
        z = 0
        i = 0
        j = 0
        m = 1
tim=mc.Timer(-1)
tim.init(period=400,mode=mc.Timer.PERIODIC, callback=rgbenvio)

while True:
    datos = uart.readline()
    if x == 0:
        envio = input("Ingrese dato: ")
        y = 1
    if datos:
        cadena = datos.decode('utf-8').strip() #Decodificación de bits a string
        if cadena == 'L2A':
            x=0
            print("Led Encendido")
        elif cadena == 'L2O':
            x=0
            print("Led Apagado")
        #POTENCIOMETRO
        elif cadena[0]=='@' and cadena[len(cadena)-1]=='#':
            voltaje2=float(cadena[1:len(cadena)-1])
            print ("{:} V".format(voltaje2))
            x=0
    #Envío Consola Micro2
    if y==1 and envio == 'L2A':
        uart.write("L2A")
        x=1
        y=0
    elif y==1 and envio == 'L2O':
        uart.write("L2O")
        x=1
        y=0
    elif y==1 and envio == 'S2':
        uart.write("S2")
        x=1
        y=0
    #Micro 1
    elif y==1 and envio == 'L1A':
        print("Led Encendido")
        led.on()
        y=0
    elif y==1 and envio == 'L1O':
        print("Led Apagado")
        led.off()
        y=0
    elif y==1 and envio == 'S1':
        lectura = (pot.read()/(4096/3.3))
        print("{:.2f} V".format(lectura))
        y=0
        time.sleep(0.1)
    time.sleep(0.01)
