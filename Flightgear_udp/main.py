import socket
import serial
import struct
ser = serial.Serial()
ser.baudrate = 115200
UDP_IP = "127.0.0.1"
ser.port = 'COM15'
UDP_PORT = 6789
vald = 0
file = open("text.txt", "w")
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
ser.open()
while True:
    data, addr = sock.recvfrom(4096) # buffer size is 1024 bytes
    #print("received message: %s" % data)

    val = data[84:86]#
    print("Обороты")
    print(val)
    vald = int.from_bytes(val, byteorder='little')
    print(vald)
    #file.write(vald)
    #file.write('\n')
    #vald = 3

    if vald == 12336:
        #val_str = vald.str().encode('ascii')
        #print(val_str)
        space = " "
        space_ascii = space.__str__().encode('ascii')
        ser.write(b'3')
        ser.write(space_ascii)

    if vald >= 12341:
        #val_str = vald.str().encode('ascii')
        #print(val_str)
        space = " "
        space_ascii = space.__str__().encode('ascii')
        ser.write(b'24')
        ser.write(space_ascii)

    #ser.write("//n")
    file.close()