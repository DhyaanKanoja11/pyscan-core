import socket

def resolve_dns(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        return None

def scan_ports(ip):
    open_ports = []
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 139, 143, 443,
        445, 3306, 3389, 8080
    ]

    for port in common_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except socket.error:
            pass

    return open_ports

def grab_banner(ip, ports):
    banners = {}

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((ip, port))

            if port == 80:
                s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

            banner = s.recv(1024)
            s.close()

            if banner:
                banners[port] = banner.decode(errors="ignore").strip()
            else:
                banners[port] = "No banner"

        except socket.error:
            banners[port] = "Could not grab banner"

    return banners
