import os
import time
import bluetooth
from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__, static_folder='static')


@app.route("/")
def main():
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
    port = 1
    serverMACAddress = "B8:27:EB:5C:0B:44"
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((serverMACAddress, port))
    time.sleep(0.02)
    print('Try', serverMACAddress, '->', action)
    print(s)
    s.send(action)
    s.close()
    print('sent')
    time.sleep(0.02)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
