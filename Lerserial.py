import serial
ser =serial.Serial('/dev/ttyACM0')
i=0
vacas = []
x=0

Time = 0
while Time !=10 :
    Time = Time +1 
    dados = open('DadosSerial.txt','a')
    s = ser.readline()
    if len(vacas) == 0:
        vacas.append(s)
        i=i+1
    elif len(vacas) > 0:
        if s not in vacas :
            vacas.append(s)
            i=i+1  
    print s
    dados.write(s)
    dados.close()

identidade = open('DadosFiltrados.txt','a')
identidade.write(str(i)) 
identidade.close()
 
for x in range (len(vacas)):
  identidade = open('DadosFiltrados.txt','a')
  y=vacas[x]
  identidade.write(y) 
  identidade.close()       
