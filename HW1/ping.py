import subprocess


def ping(host):

    p1 = subprocess.Popen(['ping', '-c 8', host], stdout=subprocess.PIPE)

    output = p1.communicate()[0]

    print(output.decode('utf-8'))


inp = input("Enter the IP or Domain: ")
ping(inp)
