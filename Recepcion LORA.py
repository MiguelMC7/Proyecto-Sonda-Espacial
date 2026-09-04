from machine import Pin
import machine as mc ##Asignación pines
import time ## Tiempo
import uos

uart = mc.UART(2, baudrate=9600, tx=22, rx=23)
while True:
    try:
        datos=uart.readline()
        if datos:
            cadena=datos.decode('utf-8').strip() #Decodificación de bits a string
            try:
                resultado = cadena[cadena.index('t')]
                try:
                    resultado1 = cadena[cadena.index('D')]
                    subcadena = cadena[cadena.index('H'):cadena.index('L')+1]
                    if subcadena[0]=='H' and subcadena[len(subcadena)-1]=='L':
                        hora=int(subcadena[1:7])
                        subcadena1 = cadena[cadena.index('L'):cadena.index('G')+1]
                        if subcadena1[0]=='L' and subcadena1[len(subcadena1)-1]=='G':
                            latitud = subcadena1[1:9]
                            subcadena2 = cadena[cadena.index('G'):cadena.index('A')+1]
                            if subcadena2[0]=='G' and subcadena2[len(subcadena2)-1]=='A':
                                longitud = subcadena2[1:11]
                                subcadena3 = cadena[cadena.index('A'):cadena.index('t')+1]
                                if subcadena3[0]=='A' and subcadena3[len(subcadena3)-1]=='t':
                                    altura = int(subcadena3[1:5])
                                    subcadena4 = cadena[cadena.index('t'):cadena.index('P')+1]
                                    if subcadena4[0]=='t' and subcadena4[len(subcadena4)-1]=='P':
                                        temperatura = int(subcadena4[1:3])
                                        subcadena5 = cadena[cadena.index('P'):cadena.index('D')+1]
                                        if subcadena5[0]=='P' and subcadena5[len(subcadena5)-1]=='D':
                                            presion = subcadena5[1:4]
                                            subcadena6 = cadena[cadena.index('D'):cadena.index('V')+1]
                                            if subcadena6[0]=='D'and subcadena6[len(subcadena6)-1]=='V':
                                                tem1 = int(subcadena6[1:3])
                                                subcadena7 = cadena[cadena.index('V'):cadena.index('C')+1]
                                                if subcadena7[0]=='V' and subcadena7[len(subcadena7)-1]=='C':
                                                    radiacion = int(subcadena7[1:len(subcadena7)-1])
                                                    print ("La hora es", hora)
                                                    print ("La latitud es", latitud)
                                                    print ("La longitud es", longitud)
                                                    print ("La altura es", altura)
                                                    print ("La temperatura es", -temperatura)
                                                    print ("La presion es", presion)
                                                    print ("La temperatura1 es", tem1)
                                                    print ("La radiacion es", radiacion)
                                                    uart.write("{:} , {:} , {:} , {:} , {:} , {:} , {:} , {:}\n".format(hora, latitud, longitud, altura, -temperatura, presion, tem1, radiacion))
                except ValueError:
                    resultado1 = cadena[cadena.index('d')]
                    subcadena = cadena[cadena.index('H'):cadena.index('L')+1]
                    if subcadena[0]=='H' and subcadena[len(subcadena)-1]=='L':
                        hora=int(subcadena[1:7])
                        subcadena1 = cadena[cadena.index('L'):cadena.index('G')+1]
                        if subcadena1[0]=='L' and subcadena1[len(subcadena1)-1]=='G':
                            latitud = subcadena1[1:9]
                            subcadena2 = cadena[cadena.index('G'):cadena.index('A')+1]
                            if subcadena2[0]=='G' and subcadena2[len(subcadena2)-1]=='A':
                                longitud = subcadena2[1:11]
                                subcadena3 = cadena[cadena.index('A'):cadena.index('t')+1]
                                if subcadena3[0]=='A' and subcadena3[len(subcadena3)-1]=='t':
                                    altura = int(subcadena3[1:5])
                                    subcadena4 = cadena[cadena.index('t'):cadena.index('P')+1]
                                    if subcadena4[0]=='t' and subcadena4[len(subcadena4)-1]=='P':
                                        temperatura = int(subcadena4[1:3])
                                        subcadena5 = cadena[cadena.index('P'):cadena.index('d')+1]
                                        if subcadena5[0]=='P' and subcadena5[len(subcadena5)-1]=='d':
                                            presion = subcadena5[1:4]
                                            subcadena6 = cadena[cadena.index('d'):cadena.index('V')+1]
                                            if subcadena6[0]=='d'and subcadena6[len(subcadena6)-1]=='V':
                                                tem1 = int(subcadena6[1:3])
                                                subcadena7 = cadena[cadena.index('V'):cadena.index('C')+1]
                                                if subcadena7[0]=='V' and subcadena7[len(subcadena7)-1]=='C':
                                                    radiacion = int(subcadena7[1:len(subcadena7)-1])
                                                    print ("La hora es", hora)
                                                    print ("La latitud es", latitud)
                                                    print ("La longitud es", longitud)
                                                    print ("La altura es", altura)
                                                    print ("La temperatura es", -temperatura)
                                                    print ("La presion es", presion)
                                                    print ("La temperatura1 es", -tem1)
                                                    print ("La radiacion es", radiacion)
                                                    uart.write("{:} , {:} , {:} , {:} , {:} , {:} , {:} , {:}\n".format(hora, latitud, longitud, altura, -temperatura, presion, -tem1, radiacion))

            except ValueError:
                resultado = cadena[cadena.index('T')]
                try:
                    resultado1 = cadena[cadena.index('D')]
                    subcadena = cadena[cadena.index('H'):cadena.index('L')+1]
                    if subcadena[0]=='H' and subcadena[len(subcadena)-1]=='L':
                        hora=int(subcadena[1:7])
                        subcadena1 = cadena[cadena.index('L'):cadena.index('G')+1]
                        if subcadena1[0]=='L' and subcadena1[len(subcadena1)-1]=='G':
                            latitud = subcadena1[1:9]
                            subcadena2 = cadena[cadena.index('G'):cadena.index('A')+1]
                            if subcadena2[0]=='G' and subcadena2[len(subcadena2)-1]=='A':
                                longitud = subcadena2[1:11]
                                subcadena3 = cadena[cadena.index('A'):cadena.index('T')+1]
                                if subcadena3[0]=='A' and subcadena3[len(subcadena3)-1]=='T':
                                    altura = int(subcadena3[1:5])
                                    subcadena4 = cadena[cadena.index('T'):cadena.index('P')+1]
                                    if subcadena4[0]=='T' and subcadena4[len(subcadena4)-1]=='P':
                                        temperatura = int(subcadena4[1:3])
                                        subcadena5 = cadena[cadena.index('P'):cadena.index('D')+1]
                                        if subcadena5[0]=='P' and subcadena5[len(subcadena5)-1]=='D':
                                            presion = subcadena5[1:4]
                                            subcadena6 = cadena[cadena.index('D'):cadena.index('V')+1]
                                            if subcadena6[0]=='D' and subcadena6[len(subcadena6)-1]=='V':
                                                tem1 = subcadena6[1:3]
                                                subcadena7 = cadena[cadena.index('V'):cadena.index('C')+1]
                                                if subcadena7[0]=='V' and subcadena7[len(subcadena7)-1]=='C':
                                                    radiacion = int(subcadena7[1:len(subcadena7)-1])
                                                    print ("La hora es", hora)
                                                    print ("La latitud es", latitud)
                                                    print ("La longitud es", longitud)
                                                    print ("La altura es", altura)
                                                    print ("La temperatura es", temperatura)
                                                    print ("La presion es", presion)
                                                    print ("La temperatura1 es", tem1)
                                                    print ("La radiacion es", radiacion)
                                                    uart.write("{:} , {:} , {:} , {:} , {:} , {:} , {:} , {:}\n".format(hora, latitud, longitud, altura, temperatura, presion, tem1, radiacion))

                except ValueError:
                    resultado1 = cadena[cadena.index('d')]
                    subcadena = cadena[cadena.index('H'):cadena.index('L')+1]
                    if subcadena[0]=='H' and subcadena[len(subcadena)-1]=='L':
                        hora=int(subcadena[1:7])
                        subcadena1 = cadena[cadena.index('L'):cadena.index('G')+1]
                        if subcadena1[0]=='L' and subcadena1[len(subcadena1)-1]=='G':
                            latitud = subcadena1[1:9]
                            subcadena2 = cadena[cadena.index('G'):cadena.index('A')+1]
                            if subcadena2[0]=='G' and subcadena2[len(subcadena2)-1]=='A':
                                longitud = subcadena2[1:11]
                                subcadena3 = cadena[cadena.index('A'):cadena.index('T')+1]
                                if subcadena3[0]=='A' and subcadena3[len(subcadena3)-1]=='T':
                                    altura = int(subcadena3[1:5])
                                    subcadena4 = cadena[cadena.index('T'):cadena.index('P')+1]
                                    if subcadena4[0]=='T' and subcadena4[len(subcadena4)-1]=='P':
                                        temperatura = int(subcadena4[1:3])
                                        subcadena5 = cadena[cadena.index('P'):cadena.index('d')+1]
                                        if subcadena5[0]=='P' and subcadena5[len(subcadena5)-1]=='d':
                                            presion = subcadena5[1:4]
                                            subcadena6 = cadena[cadena.index('d'):cadena.index('V')+1]
                                            if subcadena6[0]=='d' and subcadena6[len(subcadena6)-1]=='V':
                                                tem1 = int(subcadena6[1:3])
                                                subcadena7 = cadena[cadena.index('V'):cadena.index('C')+1]
                                                if subcadena7[0]=='V' and subcadena7[len(subcadena7)-1]=='C':
                                                    radiacion = int(subcadena7[1:len(subcadena7)-1])
                                                    print ("La hora es", hora)
                                                    print ("La latitud es", latitud)
                                                    print ("La longitud es", longitud)
                                                    print ("La altura es", altura)
                                                    print ("La temperatura es", temperatura)
                                                    print ("La presion es", presion)
                                                    print ("La temperatura1 es", -tem1)
                                                    print ("La radiacion es", radiacion)
                                                    uart.write("{:} , {:} , {:} , {:} , {:} , {:} , {:} , {:}\n".format(hora, latitud, longitud, altura, temperatura, presion, -tem1, radiacion))
    except Exception as e:
        print("Error:", e)
    time.sleep(0.1)
