import socket
import serial
import struct
ser = serial.Serial()
ser.baudrate = 115200
UDP_IP = "127.0.0.1"
ser.port = 'COM15'
UDP_PORT = 6789
vald = 0
#file = open("text.txt", "w")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
ser.open()
while True:
    data, addr = sock.recvfrom(4096)
    #print("received message: %s" % data)

    val = data[83:85]#
    print("Обороты")
    print(val)

    val_int = int(val)

    output =  -0.0000000201*val_int**5 + 0.0000251929*val_int**4 - 0.0062263101*val_int**3 + 0.6109802929*val_int**2 - 26.2751507531*val_int + 435.3499760973
    output_int = int(output)
    val_str = output_int.str().encode('ascii')
    print(val_str)
    space = " "
    space_ascii = space.str().encode('ascii')
    ser.write(val_str)
    ser.write(space_ascii)

    #ser.write("//n")