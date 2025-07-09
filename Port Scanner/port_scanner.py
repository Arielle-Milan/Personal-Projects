import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP or domain: ")
start_port = int(input("Start Port: "))
end_port = int(input("End Port: "))

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target, port))
        print(f"[+] Port {port} is open")
        s.close()
    except:
        pass

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
with ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(start_port, end_port + 1):
        executor.submit(scan, port)
