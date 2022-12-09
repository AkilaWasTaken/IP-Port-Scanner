import socket
def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print("Port {} is open".format(port))
            with open(filename, "a") as f:
                f.write("Port {} is open\n".format(port))
        except socket.error:
            pass
        s.close()
host = input("Enter the IP address to scan: ")
start_port = int(input("Enter the start port: "))
end_port = int(input("Enter the end port: "))
filename = "{}_port_scan_results.txt".format(host)
scan_ports(host, start_port, end_port)
