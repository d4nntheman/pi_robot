import os
import time
import bluetooth
from flask import Flask, render_template, request, send_from_directory
import threading
from multiprocessing import Value
app = Flask(__name__, static_folder='static')

@app.route("/")
def main():
    global msg
    msg = Value('i', 0)
    x = threading.Thread(target=bluetooth_con, args=(msg,))
    x.start()
    
    # Pass the template data into the template main.html and return it to the user
    return render_template('main2.html')


@app.route('/<path:filename>') 
def send_file(filename): 
    print('file',filename)
    return send_from_directory(app.static_folder, filename)


# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<action>")
def action(action):
    print(action)
    # If the action part of the URL is "on," execute the code indented below:
    action_map = {'action': action}
    send(action)

    return render_template('main2.html', **action_map)

def send(action):
    print('send')
    if action == 'forward':
        msg.value = 1
    if action == 'reverse':
        msg.value = 2
    if action == 'left':
        msg.value = 3
    if action == 'right':
        msg.value = 4
    if action == 'stop':
        msg.value = 0


def bluetooth_con(msg):
    port = 1
    serverMACAddress = "B8:27:EB:5C:0B:44"
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    while(1):
        time.sleep(0.1)
        string = b'none\n'
        if msg.value == 1:
            string = b'forward\n'
        if msg.value == 2:
            string = b'reverse\n'
        if msg.value == 3:
            string = b'left\n'
        if msg.value == 4:
            string = b'right\n'
        if msg.value == 0:
            string = b'stop\n'

        print(msg.value)
        print('Try', serverMACAddress, '->', string)
        s.send(string)
        print('sent')
    s.close()
    time.sleep(0.02)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
