import nmap

def scan():
    nm = nmap.PortScanner()
    nm.scan(hosts="192.168.1.0/24", arguments="-sV -T4")

    for host in nm.all_hosts():
        print(host, nm[host].state())
        for proto in nm[host].all_protocols():
            for port, info in nm[host][proto].items():
                print(f"  {port}/{proto}  {info['state']}  {info['name']}  {info.get('version', '')}")

if __name__ == "__main__":
    scan()