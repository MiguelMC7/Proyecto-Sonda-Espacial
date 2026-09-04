import machine
from machine import SoftI2C
import utime

# Configura el bus I2C
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

# Dirección del DS1307 en el bus I2C
ds1307_address = 0x68

# Función para configurar la hora en el DS1307 en formato BCD
def set_ds1307_time(year, month, date, hour, minute, second, day):
    year_bcd = ((year % 100) // 10) << 4 | ((year % 100) % 10)
    month_bcd = ((month // 10) << 4 | (month % 10))
    date_bcd = ((date // 10) << 4 | (date % 10))
    hour_bcd = ((hour // 10) << 4 | (hour % 10))
    minute_bcd = ((minute // 10) << 4 | (minute % 10))
    second_bcd = ((second // 10) << 4 | (second % 10))
    i2c.writeto_mem(ds1307_address, 0, bytes([second_bcd, minute_bcd, hour_bcd, day, date_bcd, month_bcd, year_bcd]))

# Configura la hora y la fecha en formato BCD (ajusta los valores según tu necesidad)
set_ds1307_time(23, 11, 14, 19, 11, 1, 2)

# Función para leer la hora del DS1307 y convertirla a decimal
def read_ds1307_time():
    time_data = i2c.readfrom_mem(ds1307_address, 0, 7)

    second = ((time_data[0] >> 4) * 10 + (time_data[0] & 0x0F))
    minute = ((time_data[1] >> 4) * 10 + (time_data[1] & 0x0F))
    hour = ((time_data[2] >> 4) * 10 + (time_data[2] & 0x0F))
    day = time_data[3]  # Elimina esta línea para quitar la parte del día
    date = ((time_data[4] >> 4) * 10 + (time_data[4] & 0x0F))
    month = ((time_data[5] >> 4) * 10 + (time_data[5] & 0x0F))
    year = ((time_data[6] >> 4) * 10 + (time_data[6] & 0x0F)) + 2000

    return year, month, date, hour, minute, second, day

while True:
    year, month, date, hour, minute, second, day= read_ds1307_time()
    if day==1:
        d="L"
    elif day==2:
        d="M"
    elif day==7:
        d="D"
    print("{}/{}/{} Hora: {}:{}:{} {}".format(date, month, year, hour, minute, second,d))
    utime.sleep(1)
