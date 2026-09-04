from machine import ADC, Pin
from time import sleep

# Configuración del pin analógico
mq135_pin = ADC(Pin(15))  # Conecta AOUT a GPIO34
mq135_pin.atten(ADC.ATTN_11DB)  # Configura el rango de voltaje (0-3.3V)

# Parámetros de calibración
R0 = 147.63  # Resistencia del sensor en aire limpio (ajusta según calibración)
RL = 10.0   # Resistencia de carga en kΩ

# Función para leer el valor del sensor
def read_mq135():
    sensor_value = mq135_pin.read()  # Lee el valor analógico (0-4095 para ESP32)
    voltage = (sensor_value / 4095) * 3.3  # Convierte a voltaje (0-3.3V)
    RS = (3.3 - voltage) / voltage * RL  # Calcula la resistencia del sensor
    ratio = RS / R0  # Calcula la relación RS/R0
    return ratio

# Función para estimar la concentración de CO₂ (en ppm)
def estimate_co2(ratio):
    # Parámetros de la curva de respuesta del MQ-135 para CO₂
    a = 116.6020682
    b = -2.769034857
    co2_ppm = a * (ratio ** b)  # Fórmula para estimar CO₂ en ppm
    return co2_ppm

# Bucle principal
while True:
    ratio = read_mq135()
    co2_ppm = estimate_co2(ratio)
    print("CO₂ estimado: {:.2f} ppm".format(co2_ppm))
    sleep(2)  # Espera 2 segundos antes de la siguiente lectura