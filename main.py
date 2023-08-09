import serial
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=38400, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE)

while True:
    valor = ser.readline()
    show = str(valor, 'UTF-8')
    print(show)
