import threading
import ipaddress
import subprocess

def ping(ip):
    try:
        print(f" {ip} is online")
        with open('online_devices.txt', 'a') as f:
            f.write(f"{ip}\n")
    except subprocess.CalledProcessError:
        pass

def main():
    network = input("Enter network (CIDR format): ")
    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError:
        print("Invalid CIDR format!")
        return

    threads = []
    for ip in net.hosts():
        t = threading.Thread(target=ping, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Scan complete. Results saved in online_devices.txt")

if __name__ == "__main__":
    main()
