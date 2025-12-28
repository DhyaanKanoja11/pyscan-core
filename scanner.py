import sys
from utils import resolve_dns, scan_ports, grab_banner

def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <domain/IP>")
        sys.exit(1)

    target = sys.argv[1]

    ip = resolve_dns(target)
    if not ip:
        print("Could not resolve target")
        sys.exit(1)

    open_ports = scan_ports(ip)
    banners = grab_banner(ip, open_ports)

    print("\nScan Results")
    print("Target:", target)
    print("IP:", ip)
    print("Open Ports:", open_ports)
    print("Banners:", banners)

if __name__ == "__main__":
    main()
