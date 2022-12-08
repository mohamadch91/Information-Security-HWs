import nmap
def open_ports(ip, ports):
    nm_scan = nmap.PortScanner()
    scan_range = nm_scan.scan(hosts=ip, ports=ports)
    ports_range = scan_range['scan'][ip]['tcp'].keys()
    for i in ports_range:
        port_state = scan_range['scan'][ip]['tcp'][i]['state']
        if port_state == 'open':
            print(i, '-> open')




ip_inp = input("Enter the remote host IP to scan: ")
start_inp = input("Enter the Start port number: ")
last_inp = input("Enter the Last port number: ")

open_ports(ip_inp, start_inp + '-' + last_inp)

