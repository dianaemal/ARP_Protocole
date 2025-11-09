import socket

# IP and Port must match the server

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# initiate an empty arp table
ARP_TABLE = {}
print("Initial ARP table: ", ARP_TABLE)

while True:
    # get the ip from terminal
    ip = input("Enter IP for ARP: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # connect to the server
        s.connect((SERVER_IP, SERVER_PORT))

        # sent the ip address
        s.sendall(ip.encode('utf-8'))

        mac = s.recv(1024).decode('utf-8')

        mac = None if mac == "Not Found" else mac

        if mac:
            # add to the arp table
            ARP_TABLE[ip] = mac
            print(f"Recieved ARP reply for {ip} is: {mac}")
        else:
            print(f"No ARP reply for {ip}")

        print("Current ARP table: ", ARP_TABLE)