import nmap


def active_hosts(network):
    nm_scan = nmap.PortScanner()
    scan_range = nm_scan.scan(hosts=network)

    for x in nm_scan.all_hosts():
        state = scan_range['scan'][x]['status']['state']
        if state == 'up':
            print(x, '-> Live')


def create_network_string(network, start, last):
    network_parts = network.split('.')
    network = network_parts[0] + '.' + network_parts[1] + '.' + network_parts[2] + '.' + start + '-' + last
    print(network)
    return network


network_inp = input("Enter the Network Address: ")
start_inp = input("Enter the Starting Number: ")
last_inp = input("Enter the Last Number: ")

active_hosts(create_network_string(network_inp, start_inp, last_inp))
