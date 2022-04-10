import os
import time
import bluetooth

def connect(addr):
 serverMACAddress = addr
 port = 1
 s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
 s.connect((serverMACAddress, port))
 while 1:
     i = 0
     while i < 100:
        text = str(i) + ' DATA blah 01010'  # Note change to the old (Python 2) raw_input
        time.sleep(0.01)
        try:
            s.send(text)
            i += 1
            print(addr, '->', text)
        except:
            pass


 s.close()

addr = "B8:27:EB:5C:0B:44"
while(1):
  print("Starting")
  connect(addr)
  time.sleep(5)
  print("Sleeping")
