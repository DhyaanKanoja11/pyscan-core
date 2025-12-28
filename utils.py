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
    return {}
