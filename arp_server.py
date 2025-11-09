import socket

# network dictionary: key: ip address, value: MAC address
NETWORK = {
    "192.168.1.1": "00:1A:2B:3C:4D:5E",
    "192.168.1.2": "AA:BB:CC:DD:EE:FF",
    "192.168.1.3": "11:22:33:44:55:66",
    "192.168.1.4": "77:88:99:AA:BB:CC" 
}

# setver ip
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

# creat a socket opject s
# socket.AF_INET: Specifies the address family as IPv4
# socket.SOCK_STREAM: Specifies the socket type as a stream socket (TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind the socket to an address and a port
    s.bind((SERVER_IP, SERVER_PORT))
    # listen to incomming connection
    s.listen()
    print("Server listening...")

    # keep the server running
    while True:
        # accept a connection

        conn, addr = s.accept()
        # addr contains client's addres
        # conn is a new socket object for communication with the client
        with conn:
            print(f"connection from: {addr}")

            while True:
                # recieve up to 1024 bytes and decode bytes to string (utf-8)
                ip = conn.recv(1024).decode('utf-8')
                if not ip:
                    break
                # get the MAC address given the IP recieved from NETWORK dict
                mac = NETWORK.get(ip, None)
                
                response = mac if mac else "Not Found"
                print(f"Recieved ARP request for IP: {addr}. Responded with MAC: {response}")
                # send the MAC address 
                conn.sendall(response.encode('utf-8'))

  