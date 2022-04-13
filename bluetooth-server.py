import os
import time
import bluetooth
import socket
import gpio

def receiveMessages():
        server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)
        
        client_sock,address = server_sock.accept()
        print("Accepted connection from " + str(address))
        while(1):
            data = client_sock.recv(1024)
            for msg in data.split(b'\n'):
                print("received [%s]" % msg)
                """
                if data == b'forward':
                    gpio.forward()

                if data == b'reverse':
                    gpio.backwards()

                if data == b'left':
                    gpio.left()

                if data == b'right':
                    gpio.right()

                if data == b'stop':
                    gpio.stop()
                """

            time.sleep(.01)
        client_sock.close()
        server_sock.close()

while(1):
    receiveMessages()
