import machine ##Asignación pines
import time ## Tiempo
import uos

# Configura los pines RX y TX para la comunicación serial con el módulo GPS
uart = machine.UART(1, baudrate=9600, tx=17, rx=16)  # Pines TX y RX del ESP32
uart1 = machine.UART(2, baudrate=9600, tx=22, rx=23)

while True:
    try:
        # Lee los datos del módulo GPS
        gps_data = uart.readline()
        if gps_data:
            ##Decodificación cadenas
            gps_data = gps_data.decode('utf-8').strip()
            ##Asignación variable y división cadenas
            partes = gps_data.split(',')
            ##consola primera pocisión
            if partes[0] == '$GNRMC':
                print(partes[0])
                long=float(partes[5])
                lat=float(partes[3])
                a=partes[6]
                i=int(long/100)
                d=float(long%100)
                longitud=float(i+(d/60))
                if a=='W':
                    longitud=(-longitud)
                print("Longitud:", longitud,a)
                b=partes[4]
                i1=int(lat/100)
                d1=float(lat%100)
                latitud=float(i1+(d1/60))
                if b=='s':
                    latitud=(-latitud)
                print("Latitud:", latitud,b)
                hora = 246060
                latitud1 = 4.23456
                longitud1 = float(-74.36543)
                altura = 4080
                temperatura = 30
                presion = 750
                uart1.write("G{:.6f} , {:.5f}, H{:} , C{:} , {:} , A{:} , T{:} , P{:}\n".format(latitud, longitud, hora, latitud1, longitud1, altura, temperatura, presion))
                #uart1.write(("{:.6f} , {:.5f}\n".format(latitud, longitud)))

            elif partes[0] == '$GNGLL':
                print(partes[0])
                long=float(partes[3])
                lat=float(partes[1])
                a=partes[4]
                i=int(long/100)
                d=float(long%100)
                longitud=i+(d/60)
                if a=='W':
                    longitud=(-longitud)
                print("Longitud:", longitud,a)
                b=partes[2]
                i1=int(lat/100)
                d1=float(lat%100)
                latitud=i1+(d1/60)
                if b=='s':
                    latitud=(-latitud)
                print("Latitud:", latitud,b)

                hora = 246060
                latitud1 = 4.23456
                longitud1 = float(-74.36543)
                altura = 3080
                temperatura = 35
                presion = 700
                uart1.write("G{:.6f} , {:.5f}, H{:} , C{:} , {:} , A{:} , T{:} , P{:}\n".format(latitud, longitud, hora, latitud1, longitud1, altura, temperatura, presion))
                #uart1.write("{:.6f} , {:.5f}\n".format(latitud, longitud))
            time.sleep(0.03)
    except Exception as e:
        print("Error:", e)
    time.sleep(0.1)

