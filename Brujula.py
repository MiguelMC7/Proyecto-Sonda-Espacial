import machine
import time
from machine import SoftI2C, Pin

# Configuración de la comunicación I2C
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
hmc5883l_address = 0x1E

# Función para leer los datos del HMC5883L
def read_hmc5883l():
    i2c.writeto(hmc5883l_address, bytearray([0x00, 0x60]))  # Configuración de modo y ganancia
    time.sleep(0.1)
    data = i2c.readfrom(hmc5883l_address, 6)  # Leer datos X, Z, Y
    x = (data[0] << 8) | data[1]  # Datos X
    z = (data[2] << 8) | data[3]  # Datos Z
    y = (data[4] << 8) | data[5]  # Datos Y
    return x, y, z

# Configuración de los pines RX y TX para la comunicación serial con el módulo GPS
uart = machine.UART(1, baudrate=9600, tx=17, rx=16)  # Pines TX y RX del ESP32
uart1 = machine.UART(2, baudrate=9600, tx=22, rx=23)

while True:
    try:
        # Leer los datos del módulo GPS
        gps_data = uart.readline()
        if gps_data:
            gps_data = gps_data.decode('utf-8').strip()
            partes = gps_data.split(',')

            if partes[0] == '$GNRMC':
                # Leer datos del HMC5883L
                x, y, z = read_hmc5883l()

                print("Datos HMC5883L - X: {}, Y: {}, Z: {}".format(x, y, z))

                long = float(partes[5])
                lat = float(partes[3])
                # Resto del código para procesar los datos del módulo GPS...

            elif partes[0] == '$GNGLL':
                # Leer datos del HMC5883L
                x, y, z = read_hmc5883l()

                print("Datos HMC5883L - X: {}, Y: {}, Z: {}".format(x, y, z))

                long = float(partes[3])
                lat = float(partes[1])
                # Resto del código para procesar los datos del módulo GPS...

            time.sleep(0.03)
    except Exception as e:
        print("Error:", e)
    time.sleep(0.1)
