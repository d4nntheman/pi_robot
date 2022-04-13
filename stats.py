import bluetooth, time, sys, struct
import functools
import socket

mode = sys.argv[1]
if mode not in ["client", "server"]:
    usage()

count = 200
interval = 0.2
HOST = "192.168.1.123"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
bt_mac = "B8:27:EB:5C:0B:44"

if mode == "server":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            times_ms = []
            while True:
                start_time_ns = round(time.time_ns())
                data = conn.recv(8)
                if not data:
                    break
                times_ms.append(float((time.time_ns()) - struct.unpack('q',data)[0])/1000000)
                #conn.sendall(data)
            print(times_ms)
            avg_rtt = functools.reduce(lambda x, y: x + y, times_ms) / len(times_ms)
            min_rtt = functools.reduce(lambda x, y: min(x, y), times_ms)
            max_rtt = functools.reduce(lambda x, y: max(x, y), times_ms)
            print(len(times_ms), avg_rtt, min_rtt, max_rtt)

        times_ms = []
        server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
        server_sock.bind(("", 0x1001))
        bluetooth.set_l2cap_mtu(server_sock, 65535)
        server_sock.listen(1)

        print("Waiting for incoming connection...")
        client_sock, address = server_sock.accept()
        print("Accepted connection from", str(address))

        print("Waiting for data...")
        total = 0
        while True:
            try:
                data = client_sock.recv(8)
            except bluetooth.BluetoothError as e:
                break
            if not data:
                break
            times_ms.append(float((time.time_ns()) - struct.unpack('q',data)[0])/1000000)
        client_sock.close()
        server_sock.close()

        print(times_ms)
        avg_rtt = functools.reduce(lambda x, y: x + y, times_ms) / len(times_ms)
        min_rtt = functools.reduce(lambda x, y: min(x, y), times_ms)
        max_rtt = functools.reduce(lambda x, y: max(x, y), times_ms)
        print(len(times_ms), avg_rtt, min_rtt, max_rtt)

else:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(count):
            print(struct.pack('q' ,int(round(time.time_ns()))))
            s.sendall(struct.pack('q' ,int(round(time.time_ns()))))
            time.sleep(interval)

    s = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    bluetooth.set_l2cap_mtu(s, 65535)
    port = 0x1001
    s.connect((bt_mac, port))
    for i in range(count):
        s.send(struct.pack('q',(round(time.time_ns()))))
        time.sleep(interval)

